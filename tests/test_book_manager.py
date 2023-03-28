from typing import List
import unittest
from bookmanager import BookManager, Book
import os


class TestIfa(unittest.TestCase):
    def test_add_book(self):
        book_manager = BookManager()
        book_manager.add_book(Book("1", "1", "2023", "1"))
        book_manager.add_book(Book("2", "2", "2023", "2"))
        books: List[Book] = book_manager.get_books()
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].get_isbn(), "1")
        self.assertEqual(books[1].get_isbn(), "2")

    def test_get_book(self):
        book_manager = BookManager()
        book_manager.add_book(Book("1", "1", "2023", "1"))
        b = book_manager.get_book("1")
        self.assertEqual(b.get_isbn(), "1")

    def test_remove_book(self):
        book_manager = BookManager()
        book_manager.add_book(Book("1", "1", "2023", "1"))
        book_manager.remove_book("1")
        book: List[Book] = book_manager.get_book("1")
        self.assertEqual(book, None)

    def test_list_books(self):
        book_manager = BookManager()
        book_manager.add_book(Book("1", "1", "2023", "1"))
        book_manager.add_book(Book("2", "2", "2023", "2"))
        book_manager.list_books()

    def test_update_book(self):
        book_manager = BookManager()
        book_manager.add_book(Book("1", "1", "2023", "1"))
        b = book_manager.update_book("1", Book("2", "2", "2023", "1"))
        self.assertEqual(b, None)

    def test_save_books_to_json(self):
        book_manager = BookManager()
        book_manager.add_book(Book("1", "1", "2023", "1"))
        book_manager.save_books_to_json()
        self.assertTrue(os.path.exists("books.json"))

    def test_load_books_to_json(self):
        book_manager = BookManager()
        book_manager.add_book(Book("1", "1", "2023", "1"))
        book_manager.save_books_to_json()
        book_manager.load_books_from_json()
        self.assertEqual(book_manager.get_book("1").get_author(), "1")

    def test_save_books_from_csv(self):
        book_manager = BookManager()
        book_manager.add_book(Book("1", "1", "2023", "1"))
        book_manager.save_books_to_csv()
        self.assertTrue(os.path.exists('save_csv.csv'))

    def test_load_books_from_csv(self):
        book_manager = BookManager()
        book_manager.add_book(Book("1", "1", "2023", "1"))
        book_manager.save_books_to_csv()
        book_manager.load_books_from_csv()
        self.assertEqual(book_manager.get_book("1").get_author(), "1")
