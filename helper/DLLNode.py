from typing import Any, Generic, Optional, TypeVar

T = TypeVar('T')
#T = TypeVar('T', bound=str)


class DLLNode(Generic[T]):
    data: T
    prev: Optional['DLLNode']
    next: Optional['DLLNode']

    def __init__(self, data: T):
        self.data = data
        self.prev, self.next = None, None
