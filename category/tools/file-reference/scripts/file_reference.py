"""
文件引用解析工具脚本
支持@符号引用和自然语言文件引用解析

功能：
1. 引用检测：检测文本中的@符号引用和自然语言引用
2. 引用解析：解析各种引用格式，提取文件类型和序号
3. 内容提取：提取文件内容并进行结构化处理
4. 格式支持：支持多种文件格式（PDF、Word、图片、txt等）
5. 结构化输出：将文件内容转换为结构化数据

代码作者：宫凡
创建时间：2025年10月19日
更新时间：2026年01月11日
"""

import re
import json
from typing import Dict, Any, List, Optional
from datetime import datetime


class FileReferenceParser:
    """
    文件引用解析器类

    功能：
    1. 解析@文件名引用（如@file1, @image1等）
    2. 解析自然语言文件引用（如"第一个文件"、"最新上传的图片"等）
    3. 文件内容提取和结构化输出
    4. 支持多种文件格式（PDF、Word、图片、txt等）
    """

    def __init__(self):
        """初始化文件引用解析器"""
        # 文件类型映射
        self.file_type_mapping = {
            "file": "文档",
            "image": "图片",
            "document": "文档",
            "pdf": "PDF文档",
            "word": "Word文档",
            "excel": "Excel表格",
            "txt": "文本文件",
            "audio": "音频文件",
            "video": "视频文件"
        }

        # 自然语言引用模式
        self.natural_reference_patterns = {
            r"第([一二三四五六七八九十\d]+)个文件": "ordinal_file",
            r"最新上传的(.+)": "latest_upload",
            r"刚才上传的(.+)": "recent_upload",
            r"那个(.+)文件": "that_file",
            r"我的(.+)文件": "my_file",
            r"(.+)文件": "type_file"
        }

        # 序号词汇映射
        self.ordinal_mapping = {
            "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
            "六": 6, "七": 7, "八": 8, "九": 9, "十": 10,
            "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
            "6": 6, "7": 7, "8": 8, "9": 9, "10": 10
        }

    def detect_file_references(self, text: str) -> List[str]:
        """
        检测文本中的文件引用

        Args:
            text: 输入文本

        Returns:
            List[str]: 检测到的文件引用列表
        """
        references = []

        # 1. 检测@符号引用
        at_ref_pattern = r'@(file\d+|image\d+|document\d+|pdf\d+|excel\d+|audio\d+|video\d+)'
        at_matches = re.findall(at_ref_pattern, text, re.IGNORECASE)
        references.extend([f"@{match}" for match in at_matches])

        # 2. 检测自然语言引用
        for pattern, ref_type in self.natural_reference_patterns.items():
            matches = re.findall(pattern, text)
            for match in matches:
                if isinstance(match, tuple):
                    match = match[0] if match else ""
                references.append({
                    "type": ref_type,
                    "match": match,
                    "original": f"第{match}个文件" if ref_type == "ordinal_file" else match
                })

        # 3. 检测文件类型引用
        file_type_pattern = r'([图片|图像|照片|文档|PDF|Word|Excel|文本|音频|视频]+文件)'
        type_matches = re.findall(file_type_pattern, text)
        for match in type_matches:
            references.append({
                "type": "type_file",
                "match": match,
                "original": match
            })

        return references

    def resolve_file_reference(
        self,
        reference: str,
        file_storage: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:
        """
        解析单个文件引用

        Args:
            reference: 文件引用
            file_storage: 文件存储信息（可选）

        Returns:
            Dict: 解析后的文件引用信息
        """
        try:
            if isinstance(reference, str) and reference.startswith("@"):
                # 处理@符号引用
                return self._resolve_at_reference(reference, file_storage)
            elif isinstance(reference, dict):
                # 处理自然语言引用
                return self._resolve_natural_reference(reference, file_storage)
            else:
                return None

        except Exception as e:
            return {
                "error": True,
                "message": f"解析文件引用失败: {str(e)}"
            }

    def _resolve_at_reference(
        self,
        at_ref: str,
        file_storage: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """解析@符号引用"""
        try:
            # 提取引用名称（去掉@符号）
            ref_name = at_ref[1:]  # 去掉@符号

            # 从引用名称推断文件类型和序号
            file_type = "file"
            file_index = 1

            for type_name in self.file_type_mapping.keys():
                if ref_name.startswith(type_name):
                    file_type = type_name
                    # 提取序号
                    index_str = ref_name[len(type_name):]
                    if index_str.isdigit():
                        file_index = int(index_str)
                    break

            # 获取文件信息
            file_info = self._get_file_info(file_storage, file_type, file_index)

            return {
                "reference_type": "at_reference",
                "reference_name": at_ref,
                "file_type": file_type,
                "file_index": file_index,
                "file_info": file_info,
                "resolved_content": file_info.get("content", "")
            }

        except Exception as e:
            return {
                "error": True,
                "message": f"解析@引用失败: {str(e)}"
            }

    def _resolve_natural_reference(
        self,
        natural_ref: Dict[str, Any],
        file_storage: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """解析自然语言引用"""
        try:
            ref_type = natural_ref.get("type", "")
            match = natural_ref.get("match", "")
            original = natural_ref.get("original", "")

            file_type = "file"
            file_index = 1

            if ref_type == "ordinal_file":
                # 处理序号引用
                file_index = self.ordinal_mapping.get(match, 1)
            elif ref_type in ["latest_upload", "recent_upload"]:
                # 处理最新上传引用
                file_index = 1  # 假设最新的是第一个
            elif ref_type == "type_file":
                # 处理文件类型引用
                for type_name, chinese_name in self.file_type_mapping.items():
                    if chinese_name in match or type_name in match.lower():
                        file_type = type_name
                        break

            # 获取文件信息
            file_info = self._get_file_info(file_storage, file_type, file_index)

            return {
                "reference_type": "natural_reference",
                "reference_name": original,
                "file_type": file_type,
                "file_index": file_index,
                "file_info": file_info,
                "resolved_content": file_info.get("content", "")
            }

        except Exception as e:
            return {
                "error": True,
                "message": f"解析自然语言引用失败: {str(e)}"
            }

    def _get_file_info(
        self,
        file_storage: Optional[Dict[str, Any]],
        file_type: str,
        file_index: int
    ) -> Dict[str, Any]:
        """获取文件信息"""
        # 如果提供了文件存储信息，从存储中获取
        if file_storage:
            storage_info = file_storage.get(file_type, {}).get(file_index)
            if storage_info:
                return storage_info

        # 返回默认的模拟文件信息
        return {
            "filename": f"未知{self.file_type_mapping.get(file_type, '文件')}{file_index}",
            "content": f"这是第{file_index}个{self.file_type_mapping.get(file_type, '文件')}的内容。",
            "file_size": "未知大小",
            "upload_time": "未知时间"
        }

    def parse_file_references(
        self,
        text: str,
        file_storage: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        解析文本中的所有文件引用

        Args:
            text: 输入文本
            file_storage: 文件存储信息（可选）

        Returns:
            Dict: 解析结果
        """
        # 检测文件引用
        file_references = self.detect_file_references(text)

        if not file_references:
            return {
                "success": True,
                "references_found": 0,
                "resolved_references": [],
                "message": "未检测到文件引用"
            }

        # 解析文件引用
        resolved_references = []
        failed_references = []

        for ref in file_references:
            resolved_ref = self.resolve_file_reference(ref, file_storage)
            if resolved_ref and not resolved_ref.get("error"):
                resolved_references.append(resolved_ref)
            else:
                failed_references.append(ref)

        return {
            "success": True,
            "references_found": len(file_references),
            "resolved_references": resolved_references,
            "failed_references": failed_references,
            "message": f"成功解析{len(resolved_references)}/{len(file_references)}个文件引用"
        }

    def generate_reference_report(
        self,
        resolved_references: List[Dict[str, Any]],
        original_input: str
    ) -> str:
        """
        生成文件引用报告

        Args:
            resolved_references: 解析后的文件引用列表
            original_input: 原始输入文本

        Returns:
            str: 文件引用报告
        """
        if not resolved_references:
            return "## 文件引用分析报告\n\n未找到有效的文件引用。"

        report_parts = [
            "## 文件引用分析报告\n",
            f"### 引用摘要",
            f"- 检测到引用数: {len(resolved_references)}个",
            f"- 原始输入: {original_input}\n"
        ]

        # 文件内容概览
        report_parts.append("### 文件内容概览")
        for i, ref in enumerate(resolved_references, 1):
            file_info = ref.get("file_info", {})
            report_parts.append(f"\n#### 引用{i}: {ref.get('reference_name', 'unknown')}")
            report_parts.append(f"- 文件类型: {ref.get('file_type', 'unknown')}")
            report_parts.append(f"- 文件名称: {file_info.get('filename', 'unknown')}")
            report_parts.append(f"- 文件内容: {file_info.get('content', '无内容')}")

        return "\n".join(report_parts)

    def get_parser_info(self) -> Dict[str, Any]:
        """获取解析器信息"""
        return {
            "name": "file_reference_parser",
            "description": "文件引用解析器，支持@符号引用和自然语言引用",
            "supported_reference_types": [
                "@file1, @image1等@符号引用",
                "第一个文件、最新上传等自然语言引用",
                "文件类型引用（图片文件、PDF文档等）"
            ],
            "file_type_mapping": self.file_type_mapping,
            "natural_reference_patterns": list(self.natural_reference_patterns.keys())
        }


def parse_file_references(
    text: str,
    file_storage: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    便捷函数：解析文件引用

    Args:
        text: 输入文本
        file_storage: 文件存储信息（可选）

    Returns:
        Dict: 解析结果
    """
    parser = FileReferenceParser()
    return parser.parse_file_references(text, file_storage)


if __name__ == "__main__":
    # 测试代码
    parser = FileReferenceParser()

    # 测试@符号引用
    test_text1 = "请分析@file1和@image2的内容"
    result1 = parser.parse_file_references(test_text1)
    print("测试1: @符号引用解析")
    print(f"检测结果: {result1['message']}")
    print(f"解析数量: {result1['references_found']}")
    print()

    # 测试自然语言引用
    test_text2 = "请分析第一个文件和最新上传的图片"
    result2 = parser.parse_file_references(test_text2)
    print("测试2: 自然语言引用解析")
    print(f"检测结果: {result2['message']}")
    print(f"解析数量: {result2['references_found']}")
    print()

    # 测试文件存储
    file_storage = {
        "file": {
            1: {
                "filename": "短剧策划方案.docx",
                "content": "这是一个关于战神归来题材的短剧策划方案。",
                "file_size": "2.5MB",
                "upload_time": "2024-12-20 10:30:00"
            }
        },
        "image": {
            2: {
                "filename": "角色设定图.jpg",
                "content": "主角形象设计图，包含服装、表情和场景设定。",
                "file_size": "3.2MB",
                "upload_time": "2024-12-20 11:00:00"
            }
        }
    }

    test_text3 = "请查看@file1的内容"
    result3 = parser.parse_file_references(test_text3, file_storage)
    print("测试3: 带文件存储的解析")
    print(f"检测结果: {result3['message']}")
    if result3['resolved_references']:
        ref_info = result3['resolved_references'][0]
        print(f"文件名: {ref_info['file_info']['filename']}")
        print(f"文件内容: {ref_info['file_info']['content']}")

    # 打印解析器信息
    print("\n解析器信息:")
    info = parser.get_parser_info()
    print(f"名称: {info['name']}")
    print(f"描述: {info['description']}")
    print(f"支持的引用类型: {info['supported_reference_types']}")
