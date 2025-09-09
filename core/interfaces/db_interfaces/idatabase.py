from abc import ABC, abstractmethod
from typing import Optional
from pandas import DataFrame


class IDatabaseWriter(ABC):
    @abstractmethod
    def create_db(self, replace: bool = False):
        pass

    @abstractmethod
    def create_tables(self, replace: bool = False):
        pass

    @abstractmethod
    def upload_data(
        self,
        data: DataFrame,
        exclude: list[int],
        include: list[int],
        primary_key: int = 0,
    ):
        """Uploads data from pandas dataframe into a database"""
        pass

    @abstractmethod
    def create_hash_index(self, col_number: int):
        """Creates a hash index for id"""


class IDatabaseReader(ABC):
    @abstractmethod
    def __find_by_column_number(self, col_number: int):
        """searches by id"""

    @abstractmethod
    def __find_by_column_name(self, col_name: str):
        """searches by id"""

    @abstractmethod
    def get_data(
        self, col: Optional[int | str], value: Optional[str | int], include: list = []
    ):
        """Gets selected data"""
        if type(col) == int:
            self.__find_by_column_number(col)
        elif type(col) == str:
            self.__find_by_column_name(col)
        else:
            pass


class IDatabase(IDatabaseReader, IDatabaseWriter):
    pass
