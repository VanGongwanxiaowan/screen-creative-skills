"""
人物小传生成和处理工具脚本
用于生成、验证和格式化人物小传

功能：
1. 人物识别：从故事文本中识别主要人物和重要配角
2. 小传生成：生成300-500字的详细人物小传
3. 信息提取：提取人物基本信息、性格特征、背景故事
4. 格式验证：验证人物小传格式和长度
5. 数据结构化：将人物小传转换为结构化数据
6. 关系分析：分析人物之间的关系
7. 质量控制：确保人物小传的准确性和完整性

代码作者：宫凡
创建时间：2025年10月19日
更新时间：2026年01月11日
"""

import re
from typing import Dict, Any, List, Optional
from datetime import datetime


class CharacterProfile:
    """
    人物小传类

    功能：
    1. 存储人物信息
    2. 验证人物小传
    3. 格式化输出
    4. 关系管理
    """

    def __init__(
        self,
        name: str,
        introduction: str = "",
        basic_info: Optional[Dict[str, Any]] = None,
        personality: Optional[List[str]] = None,
        relationships: Optional[List[Dict[str, str]]] = None,
        goals: Optional[str] = None,
        obstacles: Optional[str] = None
    ):
        """
        初始化人物小传

        Args:
            name: 人物姓名
            introduction: 人物介绍
            basic_info: 基本信息
            personality: 性格特征列表
            relationships: 人物关系列表
            goals: 人物目标
            obstacles: 人物困境
        """
        self.name = name
        self.introduction = introduction
        self.basic_info = basic_info or {}
        self.personality = personality or []
        self.relationships = relationships or []
        self.goals = goals
        self.obstacles = obstacles

    def validate(self) -> Dict[str, Any]:
        """
        验证人物小传

        Returns:
            Dict: 验证结果
        """
        errors = []
        warnings = []

        # 验证姓名
        if not self.name or not self.name.strip():
            errors.append("人物姓名不能为空")

        # 验证介绍长度
        intro_length = len(self.introduction)
        if intro_length < 300:
            warnings.append(f"人物介绍过短（{intro_length}字），建议300-500字")
        elif intro_length > 500:
            warnings.append(f"人物介绍过长（{intro_length}字），建议300-500字")

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }

    def to_dict(self) -> Dict[str, Any]:
        """
        转换为字典格式

        Returns:
            Dict: 人物小传字典
        """
        return {
            "name": self.name,
            "introduction": self.introduction,
            "basic_info": self.basic_info,
            "personality": self.personality,
            "relationships": self.relationships,
            "goals": self.goals,
            "obstacles": self.obstacles
        }

    def to_formatted_string(self) -> str:
        """
        转换为格式化字符串

        Returns:
            str: 格式化的人物小传
        """
        lines = [
            f"【人物】：{self.name}",
            f"【介绍】：{self.introduction}"
        ]

        if self.basic_info:
            lines.append(f"\n【基本信息】：")
            for key, value in self.basic_info.items():
                lines.append(f"  {key}: {value}")

        if self.personality:
            lines.append(f"\n【性格特征】：")
            for trait in self.personality:
                lines.append(f"  - {trait}")

        if self.relationships:
            lines.append(f"\n【人物关系】：")
            for rel in self.relationships:
                lines.append(f"  - {rel.get('character', '未知')}: {rel.get('type', '未知关系')}")

        if self.goals:
            lines.append(f"\n【人物目标】：{self.goals}")

        if self.obstacles:
            lines.append(f"\n【人物困境】：{self.obstacles}")

        return "\n".join(lines)


class CharacterProfileProcessor:
    """
    人物小传处理器类

    功能：
    1. 从文本中解析人物小传
    2. 验证人物小传质量
    3. 批量处理人物小传
    4. 生成统计报告
    """

    def __init__(self, min_characters: int = 8, profile_length_range: tuple = (300, 500)):
        """
        初始化人物小传处理器

        Args:
            min_characters: 最少人物数量
            profile_length_range: 人物介绍长度范围
        """
        self.min_characters = min_characters
        self.profile_length_range = profile_length_range

        # 人物识别模式
        self.character_patterns = [
            r'【人物】[：:]\s*([^\n]+)',  # 【人物】格式
            r'人物[：:]\s*([^\n]+)',  # 人物：格式
            r'角色[：:]\s*([^\n]+)',  # 角色：格式
        ]

        # 人物介绍模式
        self.introduction_patterns = [
            r'【介绍】[：:]\s*([^\n【]+)',  # 【介绍】格式
            r'介绍[：:]\s*([^\n【]+)',  # 介绍：格式
            r'人物小传[：:]\s*([^\n【]+)',  # 人物小传：格式
        ]

    def parse_profiles(self, text: str) -> List[CharacterProfile]:
        """
        从文本中解析人物小传

        Args:
            text: 包含人物小传的文本

        Returns:
            List[CharacterProfile]: 人物小传列表
        """
        profiles = []

        # 使用【人物】格式解析
        character_pattern = r'【人物】[：:]\s*[^\n]+\n【介绍】[：:]\s*[^\n]+(?:\n(?:?!【人物】).*)*'

        matches = re.finditer(character_pattern, text, re.MULTILINE)

        for match in matches:
            profile_text = match.group(0)
            profile = self._parse_single_profile(profile_text)
            if profile:
                profiles.append(profile)

        return profiles

    def _parse_single_profile(self, profile_text: str) -> Optional[CharacterProfile]:
        """
        解析单个人物小传

        Args:
            profile_text: 人物小传文本

        Returns:
            CharacterProfile: 人物小传对象
        """
        # 提取姓名
        name_match = re.search(r'【人物】[：:]\s*([^\n]+)', profile_text)
        name = name_match.group(1).strip() if name_match else "未知"

        # 提取介绍（匹配到下一个【】或文本结束）
        intro_match = re.search(r'【介绍】[：:]\s*', profile_text)
        if intro_match:
            intro_start = intro_match.end()
            # 找到下一个【】的位置
            next_bracket = profile_text.find('【', intro_start)
            if next_bracket == -1:
                introduction = profile_text[intro_start:].strip()
            else:
                introduction = profile_text[intro_start:next_bracket].strip()
        else:
            introduction = ""

        # 提取基本信息
        basic_info = {}
        info_pattern = r'【([^\u4e00-\u9fa5]+?)】[：:]\s*([^\n【]+)'
        for match in re.finditer(info_pattern, profile_text):
            key = match.group(1)
            value = match.group(2).strip()
            if key not in ["人物", "介绍"]:
                basic_info[key] = value

        # 提取性格特征
        personality = []
        personality_pattern = r'【性格特征】[：:]\s*\n((?:\s*[-·•]\s*[^\n]+\n?)*)'
        personality_match = re.search(personality_pattern, profile_text)
        if personality_match:
            personality_text = personality_match.group(1)
            personality = [
                line.strip().lstrip('-·•').strip()
                for line in personality_text.split('\n')
                if line.strip() and line.strip()[0] in '-·•'
            ]

        return CharacterProfile(
            name=name,
            introduction=introduction,
            basic_info=basic_info,
            personality=personality
        )

    def validate_profiles(self, profiles: List[CharacterProfile]) -> Dict[str, Any]:
        """
        验证人物小传列表

        Args:
            profiles: 人物小传列表

        Returns:
            Dict: 验证结果
        """
        results = {
            "valid": True,
            "total_count": len(profiles),
            "valid_count": 0,
            "invalid_count": 0,
            "min_characters_met": len(profiles) >= self.min_characters,
            "errors": [],
            "warnings": [],
            "details": []
        }

        for profile in profiles:
            validation = profile.validate()
            results["details"].append({
                "name": profile.name,
                "validation": validation
            })

            if validation["valid"]:
                results["valid_count"] += 1
            else:
                results["invalid_count"] += 1
                results["valid"] = False

            results["errors"].extend(validation["errors"])
            results["warnings"].extend(validation["warnings"])

        if not results["min_characters_met"]:
            results["errors"].append(
                f"人物数量不足，需要至少{self.min_characters}个人物，当前只有{len(profiles)}个"
            )
            results["valid"] = False

        return results

    def batch_process(self, texts: List[str]) -> List[Dict[str, Any]]:
        """
        批量处理人物小传文本

        Args:
            texts: 人物小传文本列表

        Returns:
            List[Dict]: 处理结果列表
        """
        results = []
        for i, text in enumerate(texts):
            profiles = self.parse_profiles(text)
            validation = self.validate_profiles(profiles)

            results.append({
                "index": i,
                "profiles": [p.to_dict() for p in profiles],
                "validation": validation,
                "profile_count": len(profiles)
            })

        return results

    def generate_statistics(self, profiles: List[CharacterProfile]) -> Dict[str, Any]:
        """
        生成人物小传统计信息

        Args:
            profiles: 人物小传列表

        Returns:
            Dict: 统计信息
        """
        total_intro_length = sum(len(p.introduction) for p in profiles)
        avg_intro_length = total_intro_length / len(profiles) if profiles else 0

        # 统计性格特征
        all_personality = []
        for p in profiles:
            all_personality.extend(p.personality)

        # 统计关系
        all_relationships = []
        for p in profiles:
            all_relationships.extend(p.relationships)

        return {
            "total_characters": len(profiles),
            "average_intro_length": avg_intro_length,
            "min_intro_length": min((len(p.introduction) for p in profiles), default=0),
            "max_intro_length": max((len(p.introduction) for p in profiles), default=0),
            "total_personality_traits": len(all_personality),
            "unique_personality_traits": len(set(all_personality)),
            "total_relationships": len(all_relationships)
        }

    def get_processor_info(self) -> Dict[str, Any]:
        """获取处理器信息"""
        return {
            "name": "character_profile_processor",
            "description": "人物小传处理器，用于生成、验证和格式化人物小传",
            "configuration": {
                "min_characters": self.min_characters,
                "profile_length_range": self.profile_length_range
            }
        }


def parse_character_profiles(text: str) -> List[Dict[str, Any]]:
    """
    便捷函数：解析人物小传

    Args:
        text: 包含人物小传的文本

    Returns:
        List[Dict]: 人物小传字典列表
    """
    processor = CharacterProfileProcessor()
    profiles = processor.parse_profiles(text)
    return [p.to_dict() for p in profiles]


def validate_character_profiles(profiles_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    便捷函数：验证人物小传

    Args:
        profiles_data: 人物小传数据列表

    Returns:
        Dict: 验证结果
    """
    processor = CharacterProfileProcessor()

    # 转换为CharacterProfile对象
    profiles = []
    for data in profiles_data:
        profile = CharacterProfile(
            name=data.get("name", ""),
            introduction=data.get("introduction", ""),
            basic_info=data.get("basic_info", {}),
            personality=data.get("personality", []),
            relationships=data.get("relationships", []),
            goals=data.get("goals"),
            obstacles=data.get("obstacles")
        )
        profiles.append(profile)

    return processor.validate_profiles(profiles)


if __name__ == "__main__":
    # 测试代码
    test_text = """
    【人物】：林浅
    【介绍】：林浅是一个25岁的年轻女性，出生于普通家庭。她性格坚强勇敢，有着不平凡的梦想。在追求梦想的过程中，她遇到了许多挑战和困难，但凭借着坚强的意志和朋友的帮助，最终实现了自己的目标。她相信只要努力，就一定能够成功。

    【人物】：李明
    【介绍】：李明是林浅的青梅竹马，从小和她一起长大。他温柔体贴，总是在林浅需要帮助的时候出现。虽然他也喜欢林浅，但看到林浅追求梦想的样子，他选择默默支持她。

    【人物】：张华
    【介绍】：张华是林浅在公司认识的同事，也是她的竞争对手。他能力出众，但也因此有些傲慢。在工作中，他和林浅经常发生冲突，但也逐渐对她产生了敬佩之情。

    【人物】：王芳
    【介绍】：王芳是林浅的闺蜜，两人从大学开始就是好朋友。她性格开朗活泼，是林浅的情感支柱。每当林浅遇到困难时，她总是第一个站出来支持她。

    【人物】：陈强
    【介绍】：陈强是公司的部门经理，是林浅的直属上司。他工作严谨认真，对下属要求很高。虽然一开始对林浅不太满意，但看到她的努力和进步后，也逐渐认可了她。

    【人物】：赵敏
    【介绍】：赵敏是公司的HR经理，负责招聘和员工关系。她善于观察，很快就发现了林浅的潜力。她经常给林浅提供职业发展的建议和机会。

    【人物】：孙丽
    【介绍】：孙丽是公司的老员工，工作经验丰富。她看到年轻时的林浅，想起了自己刚入职时的样子。她主动帮助林浅，教她很多工作技巧和职场经验。

    【人物】：周杰
    【介绍】：周杰是公司的客户，也是林浅的重要合作伙伴。他欣赏林浅的工作能力和职业态度，多次与她合作完成重要项目。
    """

    processor = CharacterProfileProcessor()

    # 解析人物小传
    profiles = processor.parse_profiles(test_text)
    print(f"解析到 {len(profiles)} 个人物小传")

    # 验证人物小传
    validation = processor.validate_profiles(profiles)
    print(f"\n验证结果:")
    print(f"有效: {validation['valid']}")
    print(f"总人数: {validation['total_count']}")
    print(f"有效人数: {validation['valid_count']}")
    print(f"无效人数: {validation['invalid_count']}")
    print(f"达到最少人数要求: {validation['min_characters_met']}")
    print(f"错误: {validation['errors']}")
    print(f"警告数量: {len(validation['warnings'])}")

    # 生成统计信息
    stats = processor.generate_statistics(profiles)
    print(f"\n统计信息:")
    print(f"总人数: {stats['total_characters']}")
    print(f"平均介绍长度: {stats['average_intro_length']:.0f}字")
    print(f"最短介绍: {stats['min_intro_length']}字")
    print(f"最长介绍: {stats['max_intro_length']}字")
    print(f"性格特征总数: {stats['total_personality_traits']}")
    print(f"关系总数: {stats['total_relationships']}")

    # 打印第一个人物小传
    if profiles:
        print("\n第一个人物小传:")
        print(profiles[0].to_formatted_string())
