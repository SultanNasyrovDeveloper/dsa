from __future__ import annotations
from abc import abstractmethod
from typing import Protocol


NumberArray = list[int]


class Comparable(Protocol):
    @abstractmethod
    def __eq__(self, other: Comparable) -> bool: ...

    @abstractmethod
    def __gt__(self, other: Comparable) -> bool: ...

    @abstractmethod
    def __lt__(self, other: Comparable) -> bool: ...

    @abstractmethod
    def __ge__(self, other: Comparable) -> bool: ...

    @abstractmethod
    def __le__(self, other: Comparable) -> bool: ...
