from dataclasses import dataclass, field
from typing import Dict


@dataclass
class FileMetadata:
    id: str
    user_id: str
    hash: str
    filename: str
    data: Dict = field(default_factory=dict)
    meta: Dict = field(default_factory=dict)
    created_at: int = 0
    updated_at: int = 0
