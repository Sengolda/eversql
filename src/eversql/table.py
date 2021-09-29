from __future__ import annotations  # for type-hints.

from typing import *  # type: ignore

from . import *  # type: ignore
from .columns import Column


class Columns:
    def __init__(self, table: Table):
        self.table: Table = table
        self._columns: dict = dict()

    def __bool__(self):
        return bool(self._columns)

    def __iter__(self):
        return iter(self._columns.values())

    def __getitem__(self, item: str) -> Column:
        return self._columns[item]

    def __setitem__(self, key: str, value: Column):
        self._columns[key] = value

    def __getattr__(self, item):
        return self._columns[item]


class Table:
    def __init__(self, name: str):
        self.columns: Columns = Columns(self)
        self.constraints: set = set()
        self.name = name
        self._sql: Optional[str] = None

    def query_sql(self, exists_ok: bool = True) -> str:
        """Create the table in the database."""
        if not self.columns:
            raise RuntimeError("Table creation failed: No columns.")
        exists = "IF NOT EXISTS " if exists_ok else ""
        cols = [col.definition for col in self.columns]
        schema = ", ".join(cols)
        sql = f"CREATE TABLE {exists}{self.name} ({schema});"
        self.sql = sql
        return sql

    def add_column(self, column: Column):
        self.columns[column.name] = column

    def __repr__(self) -> str:
        return self.sql
