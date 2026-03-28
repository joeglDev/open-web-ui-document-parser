from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class SourceType:
    type: str
    id: str


@dataclass
class Source:
    source: SourceType
    document: List[str]
    distances: List[float]


@dataclass
class MessageType:
    role: str
    content: str


@dataclass
class ChoicesType:
    index: int
    logprobs: Any
    finish_reason: str
    message: List[MessageType]


@dataclass
class ChatCompletions:
    id: str
    created: int
    model: str
    choices: List[ChoicesType]
    object: str
    usage: Dict[str, float]
