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
    def __init__(self, name: str, type, default=Missing):
        self._name = name
        self.type = type
        self.alias = None
        self._table = None
        self._default = default

    @property
    def name(self) -> str:
        return self.alias or self._name

    @property
    def table(self) -> Any:
        return self._table

    @property
    def definition(self) -> str:
        sql = f"{self._name} {self.type}"
        self.sql = sql
        return sql
