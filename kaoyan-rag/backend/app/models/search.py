"""
搜索相关数据模型
"""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    """搜索请求模型"""
    query: str = Field(..., description="查询文本", min_length=1)
    use_reranker: bool = Field(True, description="是否使用重排序")
    use_kg: bool = Field(False, description="是否使用知识图谱增强")
    top_k: Optional[int] = Field(None, description="返回Top-K结果", ge=1, le=50)
    filter_dict: Optional[Dict[str, Any]] = Field(None, description="过滤条件")
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "什么是线性代数？",
                "use_reranker": True,
                "use_kg": False,
                "top_k": 5
            }
        }


class SearchResult(BaseModel):
    """搜索结果项"""
    id: str = Field(..., description="文档块ID")
    content: str = Field(..., description="内容")
    score: float = Field(..., description="相似度分数", ge=0.0, le=1.0)
    metadata: Dict[str, Any] = Field(default_factory=dict, description="元数据")
    kg_entities: Optional[List[Dict[str, Any]]] = Field(None, description="知识图谱实体")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "chunk_123",
                "content": "线性代数是数学的一个分支...",
                "score": 0.95,
                "metadata": {
                    "source_file": "document.pdf",
                    "section": "第一章"
                }
            }
        }


class SearchResponse(BaseModel):
    """搜索响应模型"""
    query: str = Field(..., description="查询文本")
    results: List[SearchResult] = Field(default_factory=list, description="搜索结果")
    total: int = Field(..., description="结果总数", ge=0)
    retrieval_time: Optional[float] = Field(None, description="检索耗时(秒)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "什么是线性代数？",
                "results": [],
                "total": 0,
                "retrieval_time": 0.123
            }
        }


