"""
文档相关数据模型
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime


class DocumentMetadata(BaseModel):
    """文档元数据"""
    source_file: str = Field(..., description="源文件路径")
    document_id: Optional[str] = Field(None, description="文档ID")
    section: Optional[str] = Field(None, description="章节")
    page_num: Optional[int] = Field(None, description="页码")
    chunk_index: int = Field(0, description="块索引")
    file_type: Optional[str] = Field(None, description="文件类型")
    file_size: Optional[int] = Field(None, description="文件大小")
    created_at: Optional[datetime] = Field(None, description="创建时间")
    
    class Config:
        json_schema_extra = {
            "example": {
                "source_file": "/path/to/document.pdf",
                "document_id": "doc_123",
                "section": "第一章",
                "page_num": 1,
                "chunk_index": 0
            }
        }


class DocumentChunk(BaseModel):
    """文档块模型"""
    chunk_id: str = Field(..., description="块ID")
    content: str = Field(..., description="内容")
    metadata: DocumentMetadata = Field(..., description="元数据")
    embedding: Optional[list[float]] = Field(None, description="嵌入向量")
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            "id": self.chunk_id,
            "content": self.content,
            "metadata": self.metadata.model_dump()
        }
    
    class Config:
        json_schema_extra = {
            "example": {
                "chunk_id": "chunk_123",
                "content": "这是文档内容...",
                "metadata": {
                    "source_file": "/path/to/document.pdf",
                    "section": "第一章"
                }
            }
        }


class DocumentInfo(BaseModel):
    """文档信息模型"""
    document_id: str = Field(..., description="文档ID")
    source_file: str = Field(..., description="源文件路径")
    chunks_count: int = Field(..., description="文档块数量")
    upload_time: Optional[str] = Field(None, description="上传时间")
    parser: Optional[str] = Field(None, description="使用的解析器")
    
    class Config:
        json_schema_extra = {
            "example": {
                "document_id": "doc_123",
                "source_file": "/path/to/document.pdf",
                "chunks_count": 10,
                "upload_time": "2024-01-01T00:00:00",
                "parser": "unstructured"
            }
        }


class DocumentListResponse(BaseModel):
    """文档列表响应模型"""
    documents: list[DocumentInfo] = Field(..., description="文档列表")
    total: int = Field(..., description="文档总数")
    
    class Config:
        json_schema_extra = {
            "example": {
                "documents": [
                    {
                        "document_id": "doc_123",
                        "source_file": "/path/to/document.pdf",
                        "chunks_count": 10,
                        "upload_time": "2024-01-01T00:00:00",
                        "parser": "unstructured"
                    }
                ],
                "total": 1
            }
        }


