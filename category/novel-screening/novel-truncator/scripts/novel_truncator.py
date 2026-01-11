"""
小说文本截断工具脚本
专门用于处理小说类长文本的智能截断

功能：
1. 输入处理：接收小说文本内容和最大长度参数
2. 智能截断：将小说文本截断到指定长度，保持情节完整性
3. 章节识别：识别章节边界，优先在章节处截断
4. 情节保留：尽量保留完整的情节段落
5. 避免截断：避免在句子或段落中间截断
6. 长度控制：严格按照指定的最大长度进行截断
7. 内容完整性：确保截断后的文本内容完整且可读

代码作者：宫凡
创建时间：2025年10月19日
更新时间：2026年01月11日
"""

import re
from typing import Dict, Any, Optional, List


class NovelTruncator:
    """
    小说文本截断器类

    功能：
    1. 将小说文本截断到指定长度
    2. 支持章节边界识别
    3. 保持情节完整性
    4. 返回截断结果和处理信息
    """

    def __init__(self, default_max_length: int = 50000):
        """
        初始化小说文本截断器

        Args:
            default_max_length: 默认最大长度（字符数）
        """
        self.default_max_length = default_max_length

        # 章节标题模式（常见于网络小说）
        self.chapter_patterns = [
            r'第[一二三四五六七八九十百千万零\d]+章[^\n]*',  # 第X章
            r'第[一二三四五六七八九十百千万零\d]+节[^\n]*',  # 第X节
            r'第[一二三四五六七八九十百千万零\d]+回[^\n]*',  # 第X回
            r'Chapter\s*\d+[^\n]*',  # Chapter X
            r'卷[一二三四五六七八九十百千万零\d]+[^\n]*',  # 卷X
            r'楔子[^\n]*',  # 楔子
            r'序章[^\n]*',  # 序章
            r'终章[^\n]*',  # 终章
            r'尾声[^\n]*',  # 尾声
        ]

        # 中文句子结束标记
        self.sentence_endings = ['。', '！', '？', '；', '…', '」', '』']

        # 段落标记
        self.paragraph_markers = ['\n\n', '\n\r\n', '\r\n\r\n']

    def truncate_novel(
        self,
        novel_text: str,
        max_length: Optional[int] = None,
        preserve_chapter: bool = True,
        preserve_sentence: bool = True
    ) -> Dict[str, Any]:
        """
        截断小说文本到指定长度

        Args:
            novel_text: 输入的小说文本
            max_length: 最大长度（字符数），默认使用 default_max_length
            preserve_chapter: 是否优先在章节边界处截断
            preserve_sentence: 是否保持句子完整性

        Returns:
            Dict: 包含截断结果的字典
                - code: 状态码 (200=成功, 400=输入错误, 500=失败)
                - data: 截断后的小说文本内容
                - msg: 处理信息
                - metadata: 元数据信息
        """
        if not novel_text:
            return {
                "code": 400,
                "data": "",
                "msg": "输入小说文本为空",
                "metadata": {}
            }

        max_length = max_length or self.default_max_length

        # 如果文本长度小于等于最大长度，直接返回
        if len(novel_text) <= max_length:
            return {
                "code": 200,
                "data": novel_text,
                "msg": "小说文本长度未超过限制，返回原文本",
                "metadata": {
                    "original_length": len(novel_text),
                    "truncated_length": len(novel_text),
                    "truncated": False
                }
            }

        try:
            # 优先尝试在章节边界处截断
            if preserve_chapter:
                truncated = self._truncate_at_chapter_boundary(novel_text, max_length)
            elif preserve_sentence:
                truncated = self._truncate_at_sentence_boundary(novel_text, max_length)
            else:
                truncated = novel_text[:max_length]

            return {
                "code": 200,
                "data": truncated,
                "msg": f"小说文本已截断，原长度: {len(novel_text)}, 截断后长度: {len(truncated)}",
                "metadata": {
                    "original_length": len(novel_text),
                    "truncated_length": len(truncated),
                    "truncated": True,
                    "truncation_ratio": len(truncated) / len(novel_text)
                }
            }

        except Exception as e:
            return {
                "code": 500,
                "data": "",
                "msg": f"小说文本截断失败: {str(e)}",
                "metadata": {}
            }

    def _truncate_at_chapter_boundary(self, text: str, max_length: int) -> str:
        """
        在章节边界处截断文本

        Args:
            text: 完整文本
            max_length: 最大长度

        Returns:
            str: 截断后的文本
        """
        # 在 max_length * 0.9 到 max_length 范围内查找章节标题
        search_start = max(0, int(max_length * 0.7))
        search_end = min(len(text), max_length + 1000)

        # 查找所有章节标题
        chapter_positions = []
        for pattern in self.chapter_patterns:
            for match in re.finditer(pattern, text[search_start:search_end]):
                chapter_positions.append(search_start + match.start())

        # 按位置排序
        chapter_positions.sort()

        # 找到最接近 max_length 的章节位置
        for pos in reversed(chapter_positions):
            if pos < max_length and pos > search_start:
                # 返回到该章节开始的位置
                return text[:pos].rstrip() + "\n\n[内容过长，已截断]"

        # 如果没有找到合适的章节边界，使用句子边界
        return self._truncate_at_sentence_boundary(text, max_length)

    def _truncate_at_sentence_boundary(self, text: str, max_length: int) -> str:
        """
        在句子边界处截断文本

        Args:
            text: 完整文本
            max_length: 最大长度

        Returns:
            str: 截断后的文本
        """
        # 在 max_length * 0.8 到 max_length 范围内查找句子结束标记
        search_start = max(0, int(max_length * 0.8))
        search_text = text[search_start:max_length]

        # 按优先级查找句子结束标记
        for ending in self.sentence_endings:
            last_pos = search_text.rfind(ending)
            if last_pos > 0:
                actual_pos = search_start + last_pos
                if actual_pos > max_length * 0.8:
                    return text[:actual_pos + 1]

        # 如果没有找到合适的句子结束标记，查找段落标记
        for marker in self.paragraph_markers:
            last_pos = text.rfind(marker, 0, max_length)
            if last_pos > max_length * 0.7:
                return text[:last_pos]

        # 如果都没有找到，就在 max_length 处截断
        return text[:max_length]

    def truncate_novel_from_file(
        self,
        file_path: str,
        max_length: Optional[int] = None,
        encoding: str = 'utf-8'
    ) -> Dict[str, Any]:
        """
        从文件读取小说文本并截断

        Args:
            file_path: 文件路径
            max_length: 最大长度（字符数）
            encoding: 文件编码，默认为 utf-8

        Returns:
            Dict: 包含截断结果的字典
        """
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                novel_text = f.read()

            return self.truncate_novel(novel_text, max_length)

        except FileNotFoundError:
            return {
                "code": 404,
                "data": "",
                "msg": f"文件不存在: {file_path}",
                "metadata": {}
            }
        except UnicodeDecodeError:
            return {
                "code": 400,
                "data": "",
                "msg": f"文件解码失败，请检查文件编码: {file_path}",
                "metadata": {}
            }
        except Exception as e:
            return {
                "code": 500,
                "data": "",
                "msg": f"文件读取失败: {str(e)}",
                "metadata": {}
            }

    def extract_chapters(
        self,
        novel_text: str,
        max_chapters: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        提取小说中的章节

        Args:
            novel_text: 小说文本
            max_chapters: 最大章节数量

        Returns:
            List[Dict]: 章节列表
        """
        chapters = []

        # 合并所有章节模式
        combined_pattern = '|'.join(f'({pattern})' for pattern in self.chapter_patterns)

        # 查找所有章节标题
        for match in re.finditer(combined_pattern, novel_text):
            chapter_title = match.group(0).strip()
            chapter_start = match.start()

            chapters.append({
                "title": chapter_title,
                "start": chapter_start,
                "type": "chapter"
            })

        # 计算每章的结束位置
        for i in range(len(chapters)):
            if i < len(chapters) - 1:
                chapters[i]["end"] = chapters[i + 1]["start"]
            else:
                chapters[i]["end"] = len(novel_text)

            # 提取章节内容（限制长度）
            content_length = min(5000, chapters[i]["end"] - chapters[i]["start"])
            chapters[i]["content_preview"] = novel_text[
                chapters[i]["start"]:chapters[i]["start"] + content_length
            ]

        if max_chapters:
            chapters = chapters[:max_chapters]

        return chapters

    def batch_truncate_novels(
        self,
        novels: List[str],
        max_length: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        批量截断小说文本

        Args:
            novels: 小说文本列表
            max_length: 最大长度

        Returns:
            List[Dict]: 截断结果列表
        """
        results = []
        for i, novel in enumerate(novels):
            result = self.truncate_novel(novel, max_length)
            result["index"] = i
            results.append(result)

        return results

    def get_truncation_info(
        self,
        original_text: str,
        truncated_text: str
    ) -> Dict[str, Any]:
        """
        获取截断信息统计

        Args:
            original_text: 原始文本
            truncated_text: 截断后的文本

        Returns:
            Dict: 截断信息统计
        """
        return {
            "original_length": len(original_text),
            "truncated_length": len(truncated_text),
            "truncated_ratio": len(truncated_text) / len(original_text) if original_text else 0,
            "removed_chars": len(original_text) - len(truncated_text),
            "original_chapters": len(self.extract_chapters(original_text)),
            "truncated_chapters": len(self.extract_chapters(truncated_text))
        }

    def get_truncator_info(self) -> Dict[str, Any]:
        """获取截断器信息"""
        return {
            "name": "novel_truncator",
            "description": "小说文本截断器，支持章节边界识别",
            "supported_patterns": self.chapter_patterns,
            "configuration": {
                "default_max_length": self.default_max_length
            }
        }


def truncate_novel(
    novel_text: str,
    max_length: int = 50000,
    preserve_chapter: bool = True,
    preserve_sentence: bool = True
) -> Dict[str, Any]:
    """
    便捷函数：截断小说文本

    Args:
        novel_text: 输入的小说文本
        max_length: 最大长度
        preserve_chapter: 是否优先在章节边界处截断
        preserve_sentence: 是否保持句子完整性

    Returns:
        Dict: 包含截断结果的字典
    """
    truncator = NovelTruncator(default_max_length=max_length)
    return truncator.truncate_novel(novel_text, max_length, preserve_chapter, preserve_sentence)


if __name__ == "__main__":
    # 测试代码
    test_novel = """
    第一章 相遇

    这是一个阳光明媚的早晨。林浅走在去图书馆的路上，她今天有一个重要的面试。

    第一章 初识

    在图书馆门口，林浅遇到了一个神秘的男子。他看起来很有礼貌，但眼神中带着一丝忧郁。

    第一章 相知

    两人开始聊天，发现彼此有很多共同点。他们谈论着文学、艺术和人生理想。

    第一章 相爱

    随着时间的推移，两人之间的感情越来越深。他们开始了一段美好的恋情。

    第一章 分别

    然而，好景不长。男子因为工作原因需要离开这座城市。他们在机场深情告别。

    第一章 重逢

    三年后，他们在一次偶然的机会下重逢了。这次，他们决定不再分开。

    第一章 结局

    最终，他们走到了一起，开始了幸福的生活。这是一个关于爱情、成长和坚持的故事。
    """ * 100  # 重复多次以测试截断

    truncator = NovelTruncator()
    result = truncator.truncate_novel(test_novel, max_length=1000)

    print(f"状态码: {result['code']}")
    print(f"信息: {result['msg']}")
    print(f"截断后长度: {result['metadata']['truncated_length']}")
    print(f"是否截断: {result['metadata']['truncated']}")

    # 打印截断信息
    info = truncator.get_truncation_info(test_novel, result['data'])
    print(f"\n截断信息:")
    print(f"原始长度: {info['original_length']}")
    print(f"截断长度: {info['truncated_length']}")
    print(f"截断比例: {info['truncated_ratio']:.2%}")
    print(f"原始章节数: {info['original_chapters']}")
    print(f"截断后章节数: {info['truncated_chapters']}")

    # 测试章节提取
    print("\n章节提取测试:")
    chapters = truncator.extract_chapters(test_novel)
    print(f"提取到 {len(chapters)} 个章节:")
    for i, chapter in enumerate(chapters[:5], 1):
        print(f"  {i}. {chapter['title']}")
