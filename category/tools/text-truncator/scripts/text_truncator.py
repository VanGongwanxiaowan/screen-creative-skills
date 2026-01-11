"""
文本截断工具脚本
基于智能截断算法，将长文本截断到指定长度，保持语义完整性

功能：
1. 输入处理：接收文本内容和最大长度参数
2. 智能截断：将文本截断到指定长度
3. 边界优化：尽量在句号处断开，保持语义完整性
4. 避免截断：避免在单词或句子中间截断
5. 长度控制：严格按照指定的最大长度进行截断
6. 内容完整性：确保截断后的文本内容完整

代码作者：宫凡
创建时间：2024年10月19日
更新时间：2026年01月11日
"""

from typing import Dict, Any, Optional


class TextTruncator:
    """
    文本截断器类

    功能：
    1. 将文本截断到指定长度
    2. 支持智能截断，尽量在句号处断开
    3. 返回截断结果和处理信息
    """

    def __init__(self, default_max_length: int = 50000):
        """
        初始化文本截断器

        Args:
            default_max_length: 默认最大长度（字符数）
        """
        self.default_max_length = default_max_length

        # 中文句子结束标记
        self.sentence_endings = ['。', '！', '？', '；', '…', '」', '』']

    def truncate_text(
        self,
        text: str,
        max_length: Optional[int] = None,
        preserve_sentence: bool = True
    ) -> Dict[str, Any]:
        """
        截断文本到指定长度

        Args:
            text: 输入文本
            max_length: 最大长度（字符数），默认使用 default_max_length
            preserve_sentence: 是否保持句子完整性（尽量在句号处断开）

        Returns:
            Dict: 包含截断结果的字典
                - code: 状态码 (200=成功, 500=失败)
                - data: 截断后的文本内容
                - msg: 处理信息
        """
        if not text:
            return {
                "code": 200,
                "data": "",
                "msg": "输入文本为空"
            }

        max_length = max_length or self.default_max_length

        # 如果文本长度小于等于最大长度，直接返回
        if len(text) <= max_length:
            return {
                "code": 200,
                "data": text,
                "msg": "文本长度未超过限制，返回原文本"
            }

        try:
            # 在最大长度处截断
            truncated = text[:max_length]

            # 如果需要保持句子完整性，尝试在句号处断开
            if preserve_sentence:
                truncated = self._preserve_sentence_boundary(truncated, max_length)

            return {
                "code": 200,
                "data": truncated,
                "msg": f"文本已截断，原长度: {len(text)}, 截断后长度: {len(truncated)}"
            }

        except Exception as e:
            return {
                "code": 500,
                "data": "",
                "msg": f"文本截断失败: {str(e)}"
            }

    def _preserve_sentence_boundary(self, text: str, max_length: int) -> str:
        """
        尽量在句子边界处截断文本

        Args:
            text: 已截断的文本
            max_length: 原始最大长度

        Returns:
            str: 在句子边界处截断后的文本
        """
        # 按优先级查找句子结束标记
        for ending in self.sentence_endings:
            last_period = text.rfind(ending)
            # 确保句号位置合理（在文本长度的80%之后）
            if last_period > max_length * 0.8:
                return text[:last_period + 1]

        # 如果没有找到合适的句号，返回原截断文本
        return text

    def truncate_text_from_file(
        self,
        file_path: str,
        max_length: Optional[int] = None,
        encoding: str = 'utf-8'
    ) -> Dict[str, Any]:
        """
        从文件读取文本并截断

        Args:
            file_path: 文件路径
            max_length: 最大长度（字符数）
            encoding: 文件编码，默认为 utf-8

        Returns:
            Dict: 包含截断结果的字典
        """
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                text = f.read()

            return self.truncate_text(text, max_length)

        except FileNotFoundError:
            return {
                "code": 404,
                "data": "",
                "msg": f"文件不存在: {file_path}"
            }
        except UnicodeDecodeError:
            return {
                "code": 400,
                "data": "",
                "msg": f"文件解码失败，请检查文件编码: {file_path}"
            }
        except Exception as e:
            return {
                "code": 500,
                "data": "",
                "msg": f"文件读取失败: {str(e)}"
            }

    def batch_truncate_text(
        self,
        texts: list,
        max_length: Optional[int] = None
    ) -> list:
        """
        批量截断文本

        Args:
            texts: 文本列表
            max_length: 最大长度（字符数）

        Returns:
            list: 截断结果列表
        """
        results = []
        for text in texts:
            result = self.truncate_text(text, max_length)
            results.append(result)

        return results

    def get_truncation_info(self, original_text: str, truncated_text: str) -> Dict[str, Any]:
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
            "removed_chars": len(original_text) - len(truncated_text)
        }


def truncate_text(
    text: str,
    max_length: int = 50000,
    preserve_sentence: bool = True
) -> Dict[str, Any]:
    """
    便捷函数：截断文本

    Args:
        text: 输入文本
        max_length: 最大长度
        preserve_sentence: 是否保持句子完整性

    Returns:
        Dict: 包含截断结果的字典
    """
    truncator = TextTruncator(default_max_length=max_length)
    return truncator.truncate_text(text, max_length, preserve_sentence)


if __name__ == "__main__":
    # 测试代码
    test_text = "这是一个测试文本。这是第二句话。这是第三句话。这是第四句话。这是第五句话。这是第六句话。"

    truncator = TextTruncator()
    result = truncator.truncate_text(test_text, max_length=30)

    print(f"状态码: {result['code']}")
    print(f"信息: {result['msg']}")
    print(f"截断后文本: {result['data']}")

    # 打印截断信息
    info = truncator.get_truncation_info(test_text, result['data'])
    print(f"\n截断信息: {info}")

    # 测试批量截断
    print("\n批量截断测试:")
    texts = [
        "这是第一个文本。包含两个句子。",
        "这是第二个文本。包含三个句子。这是第三句。",
        "短文本"
    ]
    batch_results = truncator.batch_truncate_text(texts, max_length=20)
    for i, res in enumerate(batch_results, 1):
        print(f"文本{i}: {res['msg']}")
