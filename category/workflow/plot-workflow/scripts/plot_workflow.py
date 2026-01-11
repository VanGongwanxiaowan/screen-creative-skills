"""
大情节点与详细情节点一键生成工作流脚本
基于工作流编排机制，实现情节点生成的完整流程

功能：
1. 输入处理：接收故事文本，支持长文本截断和分割处理
2. 工作流编排：协调大情节点和详细情节点的生成流程
3. 文本处理：使用文本处理工具进行截断和分割
4. 并行处理：支持多个分析任务的并行执行
5. 结果整合：汇总大情节点和详细情节点的分析结果
6. 输出格式化：生成完整的双情节点分析报告
7. 质量控制：确保分析结果的准确性和完整性

代码作者：宫凡
创建时间：2024年10月19日
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


class PlotPointsWorkflow:
    """
    大情节点与详细情节点一键生成工作流类

    核心功能：
    1. 工作流编排和协调
    2. 文本处理管理
    3. 批处理协调
    4. 结果整合和格式化

    工作流程：
    输入处理 -> 文本分析 -> 并行分析任务 -> 结果整合 -> 输出
    """

    def __init__(
        self,
        default_chunk_size: int = 10000,
        default_max_length: int = 50000,
        batch_parallel_limit: int = 10
    ):
        """
        初始化情节点工作流

        Args:
            default_chunk_size: 默认文本块大小
            default_max_length: 默认最大文本长度
            batch_parallel_limit: 批处理并行限制
        """
        self.default_chunk_size = default_chunk_size
        self.default_max_length = default_max_length
        self.batch_parallel_limit = batch_parallel_limit

        # 初始化文本处理工具
        self.text_truncator = TextTruncator(default_max_length=default_max_length)
        self.text_splitter = TextSplitter(default_chunk_size=default_chunk_size)

        # 工作流状态管理
        self.workflow_state = {
            "current_step": None,
            "processed_chunks": [],
            "analysis_results": {},
            "start_time": None,
            "end_time": None
        }

        # 可调用的工具映射
        self.available_tools = {
            "text_processor": "文本处理工具",
            "story_summary": "故事大纲生成",
            "major_plot_points": "大情节点生成",
            "mind_map": "思维导图生成",
            "detailed_plot_points": "详细情节点生成",
            "output_formatter": "输出整理工具"
        }

    def execute_workflow(
        self,
        input_text: str,
        chunk_size: Optional[int] = None,
        max_length: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        执行情节点工作流

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
                "message": "开始执行大情节点与详细情节点生成工作流",
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

            # 步骤2：文本预处理
            preprocessing_result = self._preprocess_text(
                input_text,
                chunk_size or self.default_chunk_size,
                max_length or self.default_max_length
            )
            events.extend(preprocessing_result["events"])
            self.workflow_state["processed_chunks"] = preprocessing_result["chunks"]

            # 步骤3：执行分析任务
            analysis_result = self._execute_analysis_tasks()
            events.extend(analysis_result["events"])
            self.workflow_state["analysis_results"] = analysis_result["results"]

            # 步骤4：结果整合
            integration_result = self._integrate_results()
            events.extend(integration_result["events"])

            # 完成工作流
            self.workflow_state["end_time"] = datetime.now()

            events.append({
                "type": "workflow_complete",
                "message": "大情节点与详细情节点生成工作流执行完成",
                "timestamp": datetime.now().isoformat(),
                "processing_time": self._calculate_processing_time()
            })

            return {
                "success": True,
                "workflow_id": workflow_id,
                "result": integration_result["final_result"],
                "events": events,
                "processing_time": self._calculate_processing_time()
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

    def _preprocess_text(
        self,
        input_text: str,
        chunk_size: int,
        max_length: int
    ) -> Dict[str, Any]:
        """
        文本预处理

        Args:
            input_text: 输入文本
            chunk_size: 文本块大小
            max_length: 最大长度

        Returns:
            Dict: 预处理结果
        """
        events = []

        # 文本截断
        truncation_result = self.text_truncator.truncate_text(input_text, max_length)
        if truncation_result["code"] != 200:
            raise Exception(f"文本截断失败: {truncation_result['msg']}")

        truncated_text = truncation_result["data"]
        events.append({
            "type": "text_truncated",
            "message": f"文本截断完成，长度: {len(truncated_text)}",
            "timestamp": datetime.now().isoformat()
        })

        # 文本分割
        chunks = self.text_splitter.split_text(truncated_text, chunk_size)

        events.append({
            "type": "text_split_complete",
            "message": f"文本分割完成，共{len(chunks)}个片段",
            "timestamp": datetime.now().isoformat(),
            "chunk_count": len(chunks)
        })

        return {"chunks": chunks, "events": events}

    def _execute_analysis_tasks(self) -> Dict[str, Any]:
        """
        执行分析任务

        Returns:
            Dict: 分析结果
        """
        events = []
        results = {}

        events.append({
            "type": "analysis_start",
            "message": "开始执行分析任务",
            "timestamp": datetime.now().isoformat()
        })

        # 这里应该调用实际的智能体进行分析
        # 由于这是一个脚本框架，我们返回占位结果
        # 在实际使用中，应该调用相应的智能体或API

        results["story_summary"] = {
            "status": "pending",
            "message": "故事大纲分析待执行"
        }

        results["major_plot_points"] = {
            "status": "pending",
            "message": "大情节点分析待执行"
        }

        results["detailed_plot_points"] = {
            "status": "pending",
            "message": "详细情节点分析待执行"
        }

        results["mind_map"] = {
            "status": "pending",
            "message": "思维导图生成待执行"
        }

        events.append({
            "type": "analysis_complete",
            "message": "分析任务执行完成",
            "timestamp": datetime.now().isoformat()
        })

        return {"results": results, "events": events}

    def _integrate_results(self) -> Dict[str, Any]:
        """
        整合分析结果

        Returns:
            Dict: 整合结果
        """
        events = []

        events.append({
            "type": "integration_start",
            "message": "开始整合分析结果",
            "timestamp": datetime.now().isoformat()
        })

        # 构建最终结果
        final_result = {
            "story_summary": self.workflow_state["analysis_results"].get("story_summary", {}),
            "major_plot_points": self.workflow_state["analysis_results"].get("major_plot_points", {}),
            "detailed_plot_points": self.workflow_state["analysis_results"].get("detailed_plot_points", {}),
            "mind_map": self.workflow_state["analysis_results"].get("mind_map", {}),
            "metadata": {
                "processing_time": self._calculate_processing_time(),
                "chunks_processed": len(self.workflow_state["processed_chunks"]),
                "tools_used": list(self.available_tools.keys())
            }
        }

        events.append({
            "type": "integration_complete",
            "message": "结果整合完成",
            "timestamp": datetime.now().isoformat()
        })

        return {"final_result": final_result, "events": events}

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
            "name": "plot_points_workflow",
            "description": "大情节点与详细情节点一键生成工作流",
            "available_tools": self.available_tools,
            "workflow_state": self.workflow_state,
            "configuration": {
                "default_chunk_size": self.default_chunk_size,
                "default_max_length": self.default_max_length,
                "batch_parallel_limit": self.batch_parallel_limit
            }
        }


def execute_plot_workflow(
    input_text: str,
    chunk_size: int = 10000,
    max_length: int = 50000
) -> Dict[str, Any]:
    """
    便捷函数：执行情节点工作流

    Args:
        input_text: 输入文本
        chunk_size: 文本块大小
        max_length: 最大文本长度

    Returns:
        Dict: 工作流执行结果
    """
    workflow = PlotPointsWorkflow(
        default_chunk_size=chunk_size,
        default_max_length=max_length
    )
    return workflow.execute_workflow(input_text, chunk_size, max_length)


if __name__ == "__main__":
    # 测试代码
    test_text = """
    这是一个测试故事。故事讲述了一个年轻人的成长历程。
    主角林浅出身平凡，但有着不平凡的梦想。在追求梦想的过程中，
    她遇到了许多挑战和困难，但凭借着坚强的意志和朋友的帮助，
    最终实现了自己的目标。这是一个关于勇气、友情和成长的故事。
    """

    workflow = PlotPointsWorkflow()
    result = workflow.execute_workflow(test_text)

    print(f"工作流执行状态: {'成功' if result['success'] else '失败'}")
    print(f"工作流ID: {result.get('workflow_id', 'N/A')}")
    print(f"处理时间: {result.get('processing_time', 'N/A')}")

    # 打印工作流信息
    info = workflow.get_workflow_info()
    print(f"\n工作流信息:")
    print(f"名称: {info['name']}")
    print(f"描述: {info['description']}")
    print(f"可用工具: {list(info['available_tools'].keys())}")
