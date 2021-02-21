from typing import Any, Type, TypeVar, Generic

T = TypeVar("T")

class Decoder(Generic[T]):
    def __init__(self, type: Type[T]):
        ...

    def decode(self, data: bytes) -> T:
        ...


class Encoder:
    def __init__(self, *, write_buffer_size : int = ...):
        ...

    def encode(self, obj: Any) -> bytes:
        ...