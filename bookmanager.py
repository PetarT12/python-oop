from book import Book
from typing import List
import json
import pandas as pd


class BookManager:

    def __init__(self):
        self.__books: List[Book] = []

    def set_books(self, books: List[Book]) -> None:
        self.__books = books

    def get_books(self) -> List:
        return self.__books

    def add_book(self, new_book: Book) -> bool:
        for book in self.__books:
            if book.get_isbn() == new_book.get_isbn():
                return False
        self.__books.append(new_book)
        return True

    def get_book(self, find_book: str) -> Book:
        for book in self.__books:
            if find_book == book.get_isbn():
                return book
        return None

    def update_book(self, isbn: str, updated_book: Book) -> bool:
        for book in self.__books:
            if isbn == book.get_isbn():
                book.set_title(updated_book.get_title())
                book.set_author(updated_book.get_author())
                book.set_isbn(updated_book.get_year_published())
                book.set_isbn(updated_book.get_isbn())
            else:
                return False

    def remove_book(self, isbn: str) -> bool:
        for book in self.__books:
            if isbn == book.get_isbn():
                self.__books.remove(book)
                return True
        return False

    def list_books(self) -> List:
        for book in self.__books:
            print("Title: " + book.get_title())
            print("Author: " + book.get_author())
            print("Year published: " + book.get_year_published())
            print("ISBN: " + book.get_isbn())

    def save_books_to_json(self) -> List:
        save_json = []
        for book in self.__books:
            save_title = book.get_title()
            save_author = book.get_author()
            save_year_published = book.get_year_published()
            save_isbn = book.get_isbn()
            save_json.append({"title": save_title, "author": save_author,
                             "year_published": save_year_published, "isbn": save_isbn})
        with open('books.json', 'w') as file:
            json.dump(save_json, file)

    def load_books_from_json(self) -> List:
        with open('books.json', 'r') as books:
            load_books = json.load(books)
        return load_books

    def save_books_to_csv(self) -> List:
        save_csv = {}
        for book in self.__books:
            for k, v in book.__dict__.items():
                save_csv[k] = save_csv.get(k, []) + [v]
            df = pd.DataFrame(save_csv)
            df.to_csv('save_csv.csv', encoding='utf-8', index=False)

    def load_books_from_csv(self) -> List:
        pd.options.display.max_rows = 9999
        books = pd.read_csv('save_csv.csv')
        return books
