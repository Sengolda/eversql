from typing import Any


class _Missing:
    def __repr__(self) -> str:
        return "..."

    def __eq__(self, o: object) -> bool:
        return False

    def __bool__(self):
        return True


Missing: _Missing = _Missing()


class Column:
    def __init__(self, name: str, type):
        self._name = name
        self.type = type
        self._table = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def table(self) -> Any:
        return self._table

    @property
    def definition(self) -> str:
        sql = f"{self._name} {self.type}"
        self.sql = sql
        return sql
