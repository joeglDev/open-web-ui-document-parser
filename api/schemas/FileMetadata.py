from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Metadata(dict):
    name: str
    content_type: str
    size: int


@dataclass
class Data(dict):
    status: str
    content: str


@dataclass
class FileMetadata(dict):
    id: str
    user_id: str
    hash: str
    filename: str
    data: Dict = field(default_factory=Data)
    meta: Dict = field(default_factory=Metadata)
    created_at: int = 0
    updated_at: int = 0
