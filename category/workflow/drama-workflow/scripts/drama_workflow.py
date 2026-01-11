"""
情节点戏剧功能分析工作流脚本
基于工作流编排机制，实现情节点戏剧功能分析的完整流程

功能：
1. 输入处理：接收故事文本，支持长文本截断和分割处理
2. 工作流编排：协调情节点戏剧功能分析的完整流程
3. 文本处理：使用文本处理工具进行截断和分割
4. 并行分析：支持多个文本片段的并行分析
5. 结果整合：汇总各个文本片段的分析结果
6. 输出格式化：生成完整的情节点戏剧功能分析报告
7. 质量控制：确保分析结果的准确性和完整性

代码作者：宫凡
创建时间：2025年10月19日
更新时间：2026年01月11日
"""

import sys
import os
from typing import Dict, Any, List, Optional
from datetime import datetime
import uuid

# 添加scripts路径到sys.path以便导入text处理工具
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../text-splitter/scripts'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../text-truncator/scripts'))

from text_splitter import TextSplitter
from text_truncator import TextTruncator


class DramaAnalysisWorkflow:
    """
    情节点戏剧功能分析工作流类

    核心功能：
    1. 工作流编排和协调
    2. 文本处理管理
    3. 并行分析协调
    4. 结果整合和格式化

    工作流程：
    输入处理 -> 文本分割 -> 并行戏剧功能分析 -> 结果整合 -> 输出
    """

    def __init__(
        self,
        max_chunk_size: int = 10000,
        max_parallel_analysis: int = 10,
        max_text_length: int = 50000
    ):
        """
        初始化情节点戏剧功能分析工作流

        Args:
            max_chunk_size: 文本块最大大小
            max_parallel_analysis: 最大并行分析数量
            max_text_length: 最大文本长度
        """
        self.max_chunk_size = max_chunk_size
        self.max_parallel_analysis = max_parallel_analysis
        self.max_text_length = max_text_length

        # 初始化文本处理工具
        self.text_truncator = TextTruncator(default_max_length=max_text_length)
        self.text_splitter = TextSplitter(default_chunk_size=max_chunk_size)

        # 工作流状态管理
        self.workflow_state = {
            "current_step": None,
            "processed_chunks": [],
            "analysis_results": [],
            "start_time": None,
            "end_time": None
        }

        # 可调用的工具映射
        self.available_tools = {
            "text_truncator": "文本截断工具",
            "text_splitter": "文本分割工具",
            "drama_analysis": "戏剧功能分析工具",
            "result_integrator": "结果整合工具"
        }

    def execute_workflow(
        self,
        input_text: str,
        chunk_size: Optional[int] = None,
        max_length: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        执行情节点戏剧功能分析工作流

        Args:
            input_text: 输入文本
            chunk_size: 文本块大小
            max_length: 最大文本长度

        Returns:
            Dict: 工作流执行结果
        """
        # 初始化工作流状态
        self.workflow_state["start_time"] = datetime.now()
        self.workflow_state["current_step"] = "initialization"

        # 生成工作流ID
        workflow_id = str(uuid.uuid4())

        # 事件列表
        events = []

        try:
            # 工作流开始事件
            events.append({
                "type": "workflow_start",
                "message": "开始情节点戏剧功能分析工作流",
                "timestamp": datetime.now().isoformat(),
                "workflow_id": workflow_id
            })

            # 步骤1：输入验证
            validation_result = self._validate_input(input_text)
            if not validation_result["valid"]:
                return {
                    "success": False,
                    "error": validation_result["error"],
                    "events": events
                }
            events.append({
                "type": "input_validated",
                "message": "输入参数验证通过",
                "timestamp": datetime.now().isoformat()
            })

            # 步骤2：文本截断处理
            truncation_result = self._truncate_text(
                input_text,
                max_length or self.max_text_length
            )
            events.extend(truncation_result["events"])
            truncated_text = truncation_result["text"]

            # 步骤3：文本分割处理
            split_result = self._split_text(
                truncated_text,
                chunk_size or self.max_chunk_size
            )
            events.extend(split_result["events"])
            text_chunks = split_result["chunks"]
            self.workflow_state["processed_chunks"] = text_chunks

            # 步骤4：并行情节点分析
            analysis_result = self._parallel_analysis(text_chunks)
            events.extend(analysis_result["events"])
            self.workflow_state["analysis_results"] = analysis_result["results"]

            # 步骤5：结果整合
            integration_result = self._integrate_results(
                analysis_result["results"],
                len(text_chunks)
            )
            events.extend(integration_result["events"])

            # 完成工作流
            self.workflow_state["end_time"] = datetime.now()

            events.append({
                "type": "workflow_complete",
                "message": "情节点戏剧功能分析工作流执行完成",
                "timestamp": datetime.now().isoformat(),
                "processing_time": self._calculate_processing_time()
            })

            return {
                "success": True,
                "workflow_id": workflow_id,
                "result": integration_result["final_result"],
                "events": events,
                "processing_time": self._calculate_processing_time(),
                "processed_chunks": len(analysis_result["results"]),
                "total_chunks": len(text_chunks)
            }

        except Exception as e:
            self.workflow_state["end_time"] = datetime.now()
            events.append({
                "type": "workflow_error",
                "message": f"工作流执行失败: {str(e)}",
                "timestamp": datetime.now().isoformat(),
                "error": str(e)
            })
            return {
                "success": False,
                "error": str(e),
                "events": events
            }

    def _validate_input(self, input_text: str) -> Dict[str, Any]:
        """
        验证输入

        Args:
            input_text: 输入文本

        Returns:
            Dict: 验证结果
        """
        if not input_text or not input_text.strip():
            return {
                "valid": False,
                "error": "输入文本不能为空"
            }
        return {"valid": True}

    def _truncate_text(
        self,
        input_text: str,
        max_length: int
    ) -> Dict[str, Any]:
        """
        文本截断处理

        Args:
            input_text: 输入文本
            max_length: 最大长度

        Returns:
            Dict: 截断结果
        """
        events = []

        events.append({
            "type": "workflow_step",
            "data": {"step": 1, "message": "步骤1: 文本截断处理"},
            "timestamp": datetime.now().isoformat()
        })

        truncation_result = self.text_truncator.truncate_text(input_text, max_length)
        if truncation_result["code"] != 200:
            raise Exception(f"文本截断失败: {truncation_result['msg']}")

        events.append({
            "type": "text_truncated",
            "message": f"文本截断完成，长度: {len(truncation_result['data'])}",
            "timestamp": datetime.now().isoformat()
        })

        return {"text": truncation_result["data"], "events": events}

    def _split_text(
        self,
        text: str,
        chunk_size: int
    ) -> Dict[str, Any]:
        """
        文本分割处理

        Args:
            text: 输入文本
            chunk_size: 文本块大小

        Returns:
            Dict: 分割结果
        """
        events = []

        events.append({
            "type": "workflow_step",
            "data": {"step": 2, "message": "步骤2: 文本分割处理"},
            "timestamp": datetime.now().isoformat()
        })

        chunks = self.text_splitter.split_text(text, chunk_size)

        events.append({
            "type": "text_split_complete",
            "message": f"文本已分割为{len(chunks)}个片段",
            "timestamp": datetime.now().isoformat()
        })

        return {"chunks": chunks, "events": events}

    def _parallel_analysis(self, text_chunks: List[str]) -> Dict[str, Any]:
        """
        并行情节点分析

        Args:
            text_chunks: 文本块列表

        Returns:
            Dict: 分析结果
        """
        events = []

        events.append({
            "type": "workflow_step",
            "data": {"step": 3, "message": "步骤3: 并行情节点分析"},
            "timestamp": datetime.now().isoformat()
        })

        results = []
        # 限制并行分析数量
        chunks_to_analyze = text_chunks[:self.max_parallel_analysis]

        # 这里应该调用实际的戏剧功能分析智能体
        # 由于这是一个脚本框架，我们返回占位结果
        for i, chunk in enumerate(chunks_to_analyze):
            # 在实际使用中，这里应该调用戏剧功能分析智能体
            result = {
                "chunk_index": i,
                "chunk_length": len(chunk),
                "analysis": "戏剧功能分析待执行",
                "status": "pending"
            }
            results.append(result)

        events.append({
            "type": "analysis_complete",
            "message": f"完成{len(results)}个文本片段的分析",
            "timestamp": datetime.now().isoformat()
        })

        return {"results": results, "events": events}

    def _integrate_results(
        self,
        analysis_results: List[Dict[str, Any]],
        total_chunks: int
    ) -> Dict[str, Any]:
        """
        整合分析结果

        Args:
            analysis_results: 分析结果列表
            total_chunks: 总文本块数

        Returns:
            Dict: 整合结果
        """
        events = []

        events.append({
            "type": "workflow_step",
            "data": {"step": 4, "message": "步骤4: 整合分析结果"},
            "timestamp": datetime.now().isoformat()
        })

        # 过滤有效结果
        valid_results = [r for r in analysis_results if r.get("status") != "error"]

        # 构建最终结果
        final_result = {
            "total_plot_points": sum(len(r.get("plot_points", [])) for r in valid_results),
            "analyzed_chunks": len(valid_results),
            "total_chunks": total_chunks,
            "summary": self._generate_summary(valid_results),
            "detailed_analysis": valid_results
        }

        events.append({
            "type": "integration_complete",
            "message": "结果整合完成",
            "timestamp": datetime.now().isoformat()
        })

        return {"final_result": final_result, "events": events}

    def _generate_summary(self, results: List[Dict[str, Any]]) -> str:
        """
        生成分析摘要

        Args:
            results: 分析结果列表

        Returns:
            str: 分析摘要
        """
        if not results:
            return "无有效的分析结果"

        summary_parts = [
            f"共分析{len(results)}个文本片段",
            f"识别出{sum(len(r.get('plot_points', [])) for r in results)}个情节点"
        ]

        return "；".join(summary_parts)

    def _calculate_processing_time(self) -> str:
        """
        计算处理时间

        Returns:
            str: 处理时间（秒）
        """
        if self.workflow_state["start_time"] and self.workflow_state["end_time"]:
            duration = self.workflow_state["end_time"] - self.workflow_state["start_time"]
            return f"{duration.total_seconds():.2f}秒"
        return "未知"

    def get_workflow_info(self) -> Dict[str, Any]:
        """
        获取工作流信息

        Returns:
            Dict: 工作流信息
        """
        return {
            "name": "drama_analysis_workflow",
            "description": "情节点戏剧功能分析工作流",
            "available_tools": self.available_tools,
            "workflow_state": self.workflow_state,
            "configuration": {
                "max_chunk_size": self.max_chunk_size,
                "max_parallel_analysis": self.max_parallel_analysis,
                "max_text_length": self.max_text_length
            }
        }


def execute_drama_workflow(
    input_text: str,
    chunk_size: int = 10000,
    max_length: int = 50000
) -> Dict[str, Any]:
    """
    便捷函数：执行情节点戏剧功能分析工作流

    Args:
        input_text: 输入文本
        chunk_size: 文本块大小
        max_length: 最大文本长度

    Returns:
        Dict: 工作流执行结果
    """
    workflow = DramaAnalysisWorkflow(
        max_chunk_size=chunk_size,
        max_text_length=max_length
    )
    return workflow.execute_workflow(input_text, chunk_size, max_length)


if __name__ == "__main__":
    # 测试代码
    test_text = """
    这是一个戏剧性的故事片段。主角李明站在十字路口，面临艰难的选择。
    一边是他深爱的女友，另一边是他的理想和抱负。这个冲突让他备受煎熬。
    最终，他选择了追逐理想，但也因此失去了爱情。这个情节点展示了理想与现实的冲突。
    """

    workflow = DramaAnalysisWorkflow()
    result = workflow.execute_workflow(test_text)

    print(f"工作流执行状态: {'成功' if result['success'] else '失败'}")
    print(f"工作流ID: {result.get('workflow_id', 'N/A')}")
    print(f"处理时间: {result.get('processing_time', 'N/A')}")
    print(f"处理片段数: {result.get('processed_chunks', 'N/A')}/{result.get('total_chunks', 'N/A')}")

    # 打印工作流信息
    info = workflow.get_workflow_info()
    print(f"\n工作流信息:")
    print(f"名称: {info['name']}")
    print(f"描述: {info['description']}")
    print(f"可用工具: {list(info['available_tools'].keys())}")
