
class Book:

    def __init__(self, title: str, author: str, year_published: int, isbn: str) -> None:
        self.__title = title
        self.__author = author
        self.__year_published = year_published
        self.__isbn = isbn

    def set_title(self, title: str) -> None:
        self.__title = title

    def get_title(self) -> str:
        return self.__title

    def set_author(self, author: str) -> None:
        self.__author = author

    def get_author(self) -> str:
        return self.__author

    def set_year_published(self, year_published: int) -> None:
        self.__year_published = year_published

    def get_year_published(self) -> int:
        return self.__year_published

    def set_isbn(self, isbn: str) -> None:
        self.__isbn = isbn

    def get_isbn(self) -> str:
        return self.__isbn
