"""
文本分割工具脚本
基于智能分割算法，将长文本分割成指定大小的块，保持语义完整性

功能：
1. 输入处理：接收文本内容和分割块大小参数
2. 智能分割：将文本分割成指定大小的块
3. 边界优化：尽量在句号处断开，保持语义完整性
4. 避免截断：避免在单词或句子中间截断
5. 块大小控制：严格按照指定的块大小进行分割
6. 内容完整性：确保分割后的文本块内容完整

代码作者：宫凡
创建时间：2024年10月19日
更新时间：2026年01月11日
"""

import re
from typing import List, Dict, Any, Optional


class TextSplitter:
    """
    文本分割器类

    功能：
    1. 将文本分割成指定大小的块
    2. 支持智能分割，尽量在句号处断开
    3. 返回分割后的文本片段列表
    """

    def __init__(self, default_chunk_size: int = 10000):
        """
        初始化文本分割器

        Args:
            default_chunk_size: 默认块大小（字符数）
        """
        self.default_chunk_size = default_chunk_size

        # 中文句子结束标记
        self.sentence_endings = ['。', '！', '？', '；', '…', '」', '』']

        # 段落结束标记
        self.paragraph_endings = ['\n', '\r\n']

    def split_text(
        self,
        text: str,
        chunk_size: Optional[int] = None,
        split_by_paragraph: bool = False
    ) -> List[str]:
        """
        将文本分割成指定大小的块

        Args:
            text: 输入文本
            chunk_size: 每块的大小（字符数），默认使用 default_chunk_size
            split_by_paragraph: 是否按段落分割，优先在段落边界处断开

        Returns:
            List[str]: 分割后的文本块列表
        """
        if not text:
            return []

        chunk_size = chunk_size or self.default_chunk_size

        # 如果文本长度小于等于块大小，直接返回
        if len(text) <= chunk_size:
            return [text]

        # 根据分割策略选择不同的分割方法
        if split_by_paragraph:
            return self._split_by_paragraph(text, chunk_size)
        else:
            return self._split_by_sentence(text, chunk_size)

    def _split_by_sentence(self, text: str, chunk_size: int) -> List[str]:
        """
        按句子边界分割文本

        Args:
            text: 输入文本
            chunk_size: 每块的大小

        Returns:
            List[str]: 分割后的文本块列表
        """
        chunks = []
        start = 0

        while start < len(text):
            # 计算当前块的结束位置
            end = min(start + chunk_size, len(text))

            # 如果不是最后一块，尝试在句子边界处断开
            if end < len(text):
                # 在 chunk_size 范围内寻找最后一个合适的句子结束位置
                best_break = self._find_best_break_position(text, start, end)

                if best_break > start + chunk_size * 0.5:  # 确保断点位置合理
                    end = best_break + 1

            # 提取文本块
            chunk = text[start:end].strip()
            if chunk:  # 只添加非空的文本块
                chunks.append(chunk)

            # 移动到下一个位置
            start = end

        return chunks

    def _split_by_paragraph(self, text: str, chunk_size: int) -> List[str]:
        """
        按段落边界分割文本

        Args:
            text: 输入文本
            chunk_size: 每块的大小

        Returns:
            List[str]: 分割后的文本块列表
        """
        # 先按段落分割文本
        paragraphs = re.split(r'\n+', text.strip())

        chunks = []
        current_chunk = ""
        current_length = 0

        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if not paragraph:
                continue

            para_length = len(paragraph)

            # 如果当前段落加上后不超过块大小，直接添加
            if current_length + para_length <= chunk_size:
                if current_chunk:
                    current_chunk += "\n\n" + paragraph
                else:
                    current_chunk = paragraph
                current_length += para_length + (2 if current_chunk != paragraph else 0)
            else:
                # 如果当前段落加上后超过块大小
                if current_chunk:
                    chunks.append(current_chunk)

                # 如果单个段落超过块大小，需要进一步分割
                if para_length > chunk_size:
                    # 按句子分割这个大段落
                    sub_chunks = self._split_by_sentence(paragraph, chunk_size)
                    chunks.extend(sub_chunks)
                    current_chunk = ""
                    current_length = 0
                else:
                    current_chunk = paragraph
                    current_length = para_length

        # 添加最后一个块
        if current_chunk:
            chunks.append(current_chunk)

        return chunks

    def _find_best_break_position(self, text: str, start: int, end: int) -> int:
        """
        在指定范围内查找最佳的断开位置

        Args:
            text: 完整文本
            start: 起始位置
            end: 结束位置

        Returns:
            int: 最佳断开位置
        """
        # 优先级：句子结束 > 标点符号 > 段落结束 > 逗号

        # 1. 查找句子结束标记
        for ending in self.sentence_endings:
            pos = text.rfind(ending, start, end)
            if pos > start + (end - start) * 0.5:
                return pos

        # 2. 查找段落结束标记
        for ending in self.paragraph_endings:
            pos = text.rfind(ending, start, end)
            if pos > start + (end - start) * 0.5:
                return pos

        # 3. 查找逗号（权重较低）
        comma_pos = text.rfind('，', start, end)
        if comma_pos > start + (end - start) * 0.7:
            return comma_pos

        # 4. 如果没有找到合适的断点，就在 end 处断开
        return end

    def split_text_by_ratio(
        self,
        text: str,
        ratio: float = 0.5
    ) -> List[str]:
        """
        按比例分割文本（用于将文本分成两部分）

        Args:
            text: 输入文本
            ratio: 第一部分的比例（0-1）

        Returns:
            List[str]: 分割后的文本块列表
        """
        if not text:
            return []

        split_pos = int(len(text) * ratio)

        # 尽量在句子边界处断开
        best_break = self._find_best_break_position(text, 0, split_pos)

        if best_break > 0:
            split_pos = best_break + 1

        part1 = text[:split_pos].strip()
        part2 = text[split_pos:].strip()

        return [part1, part2]

    def get_split_info(self, text: str, chunks: List[str]) -> Dict[str, Any]:
        """
        获取分割信息统计

        Args:
            text: 原始文本
            chunks: 分割后的文本块

        Returns:
            Dict: 分割信息统计
        """
        return {
            "original_length": len(text),
            "total_chunks": len(chunks),
            "chunk_sizes": [len(chunk) for chunk in chunks],
            "average_chunk_size": sum(len(chunk) for chunk in chunks) / len(chunks) if chunks else 0,
            "min_chunk_size": min(len(chunk) for chunk in chunks) if chunks else 0,
            "max_chunk_size": max(len(chunk) for chunk in chunks) if chunks else 0
        }


def split_text(
    text: str,
    chunk_size: int = 10000,
    split_by_paragraph: bool = False
) -> List[str]:
    """
    便捷函数：分割文本

    Args:
        text: 输入文本
        chunk_size: 每块的大小
        split_by_paragraph: 是否按段落分割

    Returns:
        List[str]: 分割后的文本块列表
    """
    splitter = TextSplitter(default_chunk_size=chunk_size)
    return splitter.split_text(text, chunk_size, split_by_paragraph)


if __name__ == "__main__":
    # 测试代码
    test_text = "这是一个测试文本。这是第二句话。这是第三句话。这是第四句话。这是第五句话。"

    splitter = TextSplitter()
    chunks = splitter.split_text(test_text, chunk_size=20)

    print(f"原始文本长度: {len(test_text)}")
    print(f"分割块数: {len(chunks)}")
    for i, chunk in enumerate(chunks, 1):
        print(f"块{i} (长度{len(chunk)}): {chunk}")

    # 打印分割信息
    info = splitter.get_split_info(test_text, chunks)
    print(f"\n分割信息: {info}")
