import unittest
from unittest.mock import patch, mock_open

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.model import Book
from src.buisness_logic import (
    load_books_from_library,
    add_book,
    remove_book,
    search_books,
    display_all_books,
    change_book_status,
)


class TestLibraryFunctions(unittest.TestCase):

    def setUp(self):
        """Создание тестового набора книг"""
        self.books = [
            Book(1, "1984", "Джордж Оруэлл", 1949),
            Book(2, "Братья Карамазовы", "Фёдор Достоевский", 1880),
            Book(3, "Мастер и Маргарита", "Михаил Булгаков", 1967)
        ]

    def test_add_book(self):
        """Тест на добавление книги"""
        with patch('src.buisness_logic.save_data') as mock_save:
            add_book(self.books, "Новая книга", "Автор", 2024)
            self.assertEqual(len(self.books), 4)
            self.assertEqual(self.books[-1].title, "Новая книга")
            mock_save.assert_called_once()

    def test_remove_book(self):
        """Тест на удаление книги"""
        with patch('src.buisness_logic.save_data') as mock_save:
            remove_book(self.books, 2)
            self.assertEqual(len(self.books), 2)
            self.assertIsNone(next((book for book in self.books if book.id == 2), None))
            mock_save.assert_called_once()

    def test_search_books(self):
        """Тест на поиск книг"""
        results = search_books(self.books, "1984")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "1984")

        results = search_books(self.books, "Достоевский")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Братья Карамазовы")

        results = search_books(self.books, "1967")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Мастер и Маргарита")

        results = search_books(self.books, "неизвестная книга")
        self.assertEqual(len(results), 0)

    def test_change_book_status(self):
        """Тест на изменение статуса книги"""
        with patch('src.buisness_logic.save_data') as mock_save:
            change_book_status(self.books, 1, "выдана")
            self.assertEqual(self.books[0].status, "выдана")
            mock_save.assert_called_once()

            change_book_status(self.books, 1, "в наличии")
            self.assertEqual(self.books[0].status, "в наличии")
            mock_save.assert_called_with(self.books)

    def test_display_all_books(self):
        """Тест на отображение всех книг"""
        with patch('builtins.print') as mock_print:
            display_all_books(self.books)
            mock_print.assert_any_call("ID: 1, Название: 1984, Автор: Джордж Оруэлл, Год: 1949, Статус: в наличии")
            mock_print.assert_any_call(
                "ID: 2, Название: Братья Карамазовы, Автор: Фёдор Достоевский, Год: 1880, Статус: в наличии")
            mock_print.assert_any_call(
                "ID: 3, Название: Мастер и Маргарита, Автор: Михаил Булгаков, Год: 1967, Статус: в наличии")

    @patch("builtins.open", new_callable=mock_open,
           read_data='[{"id": 1, "title": "1984", "author": "Джордж Оруэлл", "year": 1949, "status": "в наличии"}]')
    def test_load_books_from_library(self, mock_file):
        """Тест на загрузку книг из библиотеки"""
        books = load_books_from_library()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "1984")


if __name__ == "__main__":
    unittest.main()
