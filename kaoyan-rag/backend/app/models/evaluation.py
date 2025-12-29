"""
评估相关数据模型
"""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class EvaluationRequest(BaseModel):
    """评估请求模型"""
    dataset: List[Dict[str, Any]] = Field(..., description="评估数据集")
    framework: str = Field("ragas", description="评估框架: ragas或llamaindex")
    metrics: Optional[List[str]] = Field(None, description="评估指标")
    
    class Config:
        json_schema_extra = {
            "example": {
                "dataset": [
                    {
                        "question": "什么是线性代数？",
                        "answer": "线性代数是...",
                        "contexts": ["上下文1", "上下文2"],
                        "ground_truth": "参考答案"
                    }
                ],
                "framework": "ragas"
            }
        }


class EvaluationResponse(BaseModel):
    """评估响应模型"""
    framework: str = Field(..., description="使用的评估框架")
    metrics: Dict[str, float] = Field(..., description="评估指标分数")
    total_samples: int = Field(..., description="评估样本数")
    details: Optional[Dict[str, Any]] = Field(None, description="详细信息")
    
    class Config:
        json_schema_extra = {
            "example": {
                "framework": "ragas",
                "metrics": {
                    "faithfulness": 0.95,
                    "answer_relevancy": 0.88
                },
                "total_samples": 10
            }
        }


