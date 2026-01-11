"""
思维导图生成工具脚本
支持将文本内容转换为结构化的思维导图数据

功能：
1. 内容分析：分析输入内容，提取关键信息和层次结构
2. 结构设计：设计思维导图的层次结构和节点关系
3. 数据生成：生成结构化的思维导图数据
4. 格式支持：支持Markdown、JSON等多种输出格式
5. 层级控制：控制思维导图的层级深度和节点数量
6. 数据验证：验证思维导图数据的完整性和准确性

代码作者：宫凡 VanGong
创建时间：2025年10月19日
更新时间：2026年01月11日
"""

import re
import json
from typing import Dict, Any, List, Optional
from datetime import datetime


class MindMapGenerator:
    """
    思维导图生成器类

    功能：
    1. 将文本内容转换为思维导图结构
    2. 支持多种内容格式（故事大纲、人物关系、情节结构等）
    3. 生成结构化的节点数据
    4. 支持多种输出格式（JSON、Markdown等）
    """

    def __init__(self, max_depth: int = 5, max_nodes: int = 100):
        """
        初始化思维导图生成器

        Args:
            max_depth: 最大层级深度
            max_nodes: 最大节点数量
        """
        self.max_depth = max_depth
        self.max_nodes = max_nodes

        # 支持的内容类型
        self.content_types = {
            "story": "故事大纲",
            "characters": "人物关系",
            "plot": "情节结构",
            "analysis": "分析报告",
            "general": "通用内容"
        }

        # 节点类型
        self.node_types = {
            "root": "根节点",
            "branch": "分支节点",
            "leaf": "叶子节点"
        }

    def generate_mind_map(
        self,
        content: str,
        content_type: str = "general",
        output_format: str = "json"
    ) -> Dict[str, Any]:
        """
        生成思维导图

        Args:
            content: 输入内容
            content_type: 内容类型
            output_format: 输出格式 (json, markdown)

        Returns:
            Dict: 生成结果
        """
        if not content or not content.strip():
            return {
                "success": False,
                "error": "输入内容不能为空"
            }

        try:
            # 分析内容，提取结构
            structure = self._analyze_content(content, content_type)

            # 构建思维导图数据
            mind_map_data = self._build_mind_map(structure, content_type)

            # 格式化输出
            if output_format == "markdown":
                output = self._to_markdown(mind_map_data)
            else:
                output = json.dumps(mind_map_data, ensure_ascii=False, indent=2)

            return {
                "success": True,
                "data": mind_map_data,
                "output": output,
                "format": output_format,
                "node_count": self._count_nodes(mind_map_data),
                "max_depth": self._get_depth(mind_map_data),
                "message": "思维导图生成成功"
            }

        except Exception as e:
            return {
                "success": False,
                "error": f"思维导图生成失败: {str(e)}"
            }

    def _analyze_content(
        self,
        content: str,
        content_type: str
    ) -> List[Dict[str, Any]]:
        """
        分析内容，提取结构

        Args:
            content: 输入内容
            content_type: 内容类型

        Returns:
            List[Dict]: 结构化数据
        """
        # 根据内容类型使用不同的解析策略
        if content_type == "story":
            return self._analyze_story(content)
        elif content_type == "characters":
            return self._analyze_characters(content)
        elif content_type == "plot":
            return self._analyze_plot(content)
        else:
            return self._analyze_general(content)

    def _analyze_story(self, content: str) -> List[Dict[str, Any]]:
        """
        分析故事大纲

        Args:
            content: 故事内容

        Returns:
            List[Dict]: 故事结构
        """
        structure = []

        # 提取故事主要元素
        sections = re.split(r'\n#{1,3}\s+', content)

        for section in sections:
            if not section.strip():
                continue

            lines = section.strip().split('\n')
            title = lines[0] if lines else "未知章节"

            # 提取子节点
            children = []
            for line in lines[1:]:
                line = line.strip()
                if line and (line.startswith('-') or line.startswith('•') or line.startswith('·')):
                    children.append({
                        "type": "leaf",
                        "content": line.lstrip('-•·').strip()
                    })

            structure.append({
                "type": "branch",
                "content": title,
                "children": children
            })

        return structure

    def _analyze_characters(self, content: str) -> List[Dict[str, Any]]:
        """
        分析人物关系

        Args:
            content: 人物关系内容

        Returns:
            List[Dict]: 人物关系结构
        """
        structure = []

        # 按人物分割
        character_pattern = r'【人物】[：:]\s*([^\n]+)'
        characters = re.findall(character_pattern, content)

        for character in characters:
            # 查找人物介绍
            intro_pattern = rf'【人物】[：:]\s*{re.escape(character)}\s*\n【介绍】[：:]\s*([^\n]+)'
            intro_match = re.search(intro_pattern, content)

            structure.append({
                "type": "branch",
                "content": character.strip(),
                "children": [
                    {
                        "type": "leaf",
                        "content": intro_match.group(1) if intro_match else "暂无介绍"
                    }
                ]
            })

        return structure

    def _analyze_plot(self, content: str) -> List[Dict[str, Any]]:
        """
        分析情节结构

        Args:
            content: 情节内容

        Returns:
            List[Dict]: 情节结构
        """
        structure = []

        # 按阶段分割
        stage_pattern = r'【阶段[一二三四五六七八九十]+[：:]\s*([^\n]+)'
        stages = re.findall(stage_pattern, content)

        for i, stage in enumerate(stages):
            # 提取该阶段的情节点
            stage_section = re.split(r'【阶段', content)[i + 1] if i < len(stages) else ""

            plot_points = []
            for line in stage_section.split('\n'):
                line = line.strip()
                if line and line.startswith(('-')):
                    plot_points.append({
                        "type": "leaf",
                        "content": line.lstrip('-•·').strip()
                    })

            structure.append({
                "type": "branch",
                "content": stage.strip(),
                "children": plot_points
            })

        return structure

    def _analyze_general(self, content: str) -> List[Dict[str, Any]]:
        """
        分析通用内容

        Args:
            content: 通用内容

        Returns:
            List[Dict]: 通用结构
        """
        structure = []

        # 按段落分割
        paragraphs = re.split(r'\n\n+', content.strip())

        for para in paragraphs:
            if not para.strip():
                continue

            lines = para.strip().split('\n')
            title = lines[0] if lines else "章节"

            # 提取子节点
            children = []
            for line in lines[1:]:
                line = line.strip()
                if line:
                    children.append({
                        "type": "leaf",
                        "content": line
                    })

            structure.append({
                "type": "branch",
                "content": title,
                "children": children
            })

        return structure

    def _build_mind_map(
        self,
        structure: List[Dict[str, Any]],
        content_type: str
    ) -> Dict[str, Any]:
        """
        构建思维导图数据

        Args:
            structure: 结构化数据
            content_type: 内容类型

        Returns:
            Dict: 思维导图数据
        """
        return {
            "title": self.content_types.get(content_type, "思维导图"),
            "type": content_type,
            "created_at": datetime.now().isoformat(),
            "root": {
                "id": "root",
                "type": "root",
                "content": self.content_types.get(content_type, "思维导图"),
                "children": [
                    self._build_node(item, 1)
                    for item in structure[:self.max_nodes]
                ]
            }
        }

    def _build_node(
        self,
        item: Dict[str, Any],
        depth: int
    ) -> Dict[str, Any]:
        """
        构建节点

        Args:
            item: 节点数据
            depth: 当前深度

        Returns:
            Dict: 节点数据
        """
        node = {
            "id": f"node_{depth}_{hash(item['content'])}",
            "type": item.get("type", "branch"),
            "content": item["content"]
        }

        # 递归构建子节点
        if depth < self.max_depth and "children" in item:
            node["children"] = [
                self._build_node(child, depth + 1)
                for child in item["children"][:self.max_nodes]
            ]

        return node

    def _to_markdown(self, mind_map_data: Dict[str, Any]) -> str:
        """
        转换为Markdown格式

        Args:
            mind_map_data: 思维导图数据

        Returns:
            str: Markdown格式文本
        """
        lines = [f"# {mind_map_data['title']}\n"]

        def add_node(node: Dict[str, Any], level: int):
            prefix = "  " * level + "-"
            lines.append(f"{prefix} {node['content']}")

            if "children" in node:
                for child in node["children"]:
                    add_node(child, level + 1)

        add_node(mind_map_data["root"], 0)

        return "\n".join(lines)

    def _count_nodes(self, mind_map_data: Dict[str, Any]) -> int:
        """
        统计节点数量

        Args:
            mind_map_data: 思维导图数据

        Returns:
            int: 节点数量
        """
        def count(node: Dict[str, Any]) -> int:
            total = 1
            if "children" in node:
                total += sum(count(child) for child in node["children"])
            return total

        return count(mind_map_data["root"]) - 1  # 不包括根节点

    def _get_depth(self, mind_map_data: Dict[str, Any]) -> int:
        """
        获取最大深度

        Args:
            mind_map_data: 思维导图数据

        Returns:
            int: 最大深度
        """
        def get_depth(node: Dict[str, Any]) -> int:
            if "children" not in node or not node["children"]:
                return 0
            return 1 + max(get_depth(child) for child in node["children"])

        return get_depth(mind_map_data["root"])

    def validate_mind_map(self, mind_map_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        验证思维导图数据

        Args:
            mind_map_data: 思维导图数据

        Returns:
            Dict: 验证结果
        """
        errors = []
        warnings = []

        # 检查必需字段
        if "root" not in mind_map_data:
            errors.append("缺少根节点")
        elif "content" not in mind_map_data["root"]:
            errors.append("根节点缺少内容")

        # 检查深度
        depth = self._get_depth(mind_map_data)
        if depth > self.max_depth:
            warnings.append(f"思维导图深度({depth})超过最大限制({self.max_depth})")

        # 检查节点数量
        node_count = self._count_nodes(mind_map_data)
        if node_count > self.max_nodes:
            warnings.append(f"节点数量({node_count})超过最大限制({self.max_nodes})")

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "node_count": node_count,
            "depth": depth
        }

    def get_generator_info(self) -> Dict[str, Any]:
        """获取生成器信息"""
        return {
            "name": "mind_map_generator",
            "description": "思维导图生成器，支持多种内容格式",
            "supported_content_types": list(self.content_types.values()),
            "supported_output_formats": ["json", "markdown"],
            "configuration": {
                "max_depth": self.max_depth,
                "max_nodes": self.max_nodes
            }
        }


def generate_mind_map(
    content: str,
    content_type: str = "general",
    output_format: str = "json",
    max_depth: int = 5,
    max_nodes: int = 100
) -> Dict[str, Any]:
    """
    便捷函数：生成思维导图

    Args:
        content: 输入内容
        content_type: 内容类型
        output_format: 输出格式
        max_depth: 最大深度
        max_nodes: 最大节点数

    Returns:
        Dict: 生成结果
    """
    generator = MindMapGenerator(max_depth=max_depth, max_nodes=max_nodes)
    return generator.generate_mind_map(content, content_type, output_format)


if __name__ == "__main__":
    # 测试代码
    test_content = """
    # 故事大纲

    ## 主角设定
    - 姓名：林浅
    - 性格：坚强勇敢
    - 目标：追求梦想

    ## 情节发展
    - 起始：林浅出身平凡
    - 发展：遇到挑战和困难
    - 高潮：凭借意志克服困难
    - 结局：实现目标
    """

    generator = MindMapGenerator()
    result = generator.generate_mind_map(test_content, "story", "json")

    print(f"生成状态: {'成功' if result['success'] else '失败'}")
    print(f"信息: {result.get('message', 'N/A')}")
    print(f"节点数量: {result.get('node_count', 'N/A')}")
    print(f"最大深度: {result.get('max_depth', 'N/A')}")

    if result['success']:
        # 验证数据
        validation = generator.validate_mind_map(result['data'])
        print(f"\n验证结果:")
        print(f"有效: {validation['valid']}")
        print(f"错误: {validation['errors']}")
        print(f"警告: {validation['warnings']}")

    # 生成器信息
    print("\n生成器信息:")
    info = generator.get_generator_info()
    print(f"名称: {info['name']}")
    print(f"描述: {info['description']}")
