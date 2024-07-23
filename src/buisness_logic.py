import json
from typing import List, Optional

from model import Book


def load_books_from_library() -> List[Book]:
    """Загружает данные о книгах из файла библиотеки"""
    library_path = "../data/library.json"
    try:
        with open(library_path, "r") as file:
            data = json.load(file)
            return [Book.from_dict(book) for book in data]
    except FileNotFoundError:
        return []


def save_data(books: List[Book]):
    """
    Сохраняет данные в файл

    :param books: список с книгами
    """
    library_path = "../data/library.json"
    with open(library_path, "w") as file:
        json.dump([book.to_dict() for book in books], file, indent=4)


def add_book(books: List[Book], title: str, author: str, year: int) -> None:
    """
    Добавляет новую книгу в библиотеку

    :param books: список с книгами
    :param title: название книги
    :param author: автор книги
    :param year: год издания
    """
    new_id = max([book.id for book in books], default=0) + 1
    new_book = Book(new_id, title, author, year)
    books.append(new_book)
    save_data(books)
    print(f"Книга '{title}' успешно добавлена")


def remove_book(books: List[Book], book_id: int) -> None:
    """
    Удаляет книгу из библиотеки по ID

    :param books: список с книгами
    :param book_id: ID книги для удаления
    """
    book = _find_book_by_id(books, book_id)
    if book:
        books.remove(book)
        save_data(books)
        print(f"Книга с ID {book_id} успешно удалена")
    else:
        print(f"Книга с ID {book_id} не найдена")


def search_books(books: List[Book], query: str) -> List[Book]:
    """,
    Ищет книги по заданному запросу

    :param books: список с книгами
    :param query: поисковый запрос
    :return: список найденных книг
    """
    query = query.lower()
    return [book for book in books
            if query in book.title.lower()
            or query in book.author.lower()
            or query == str(book.year)]


def display_all_books(books: List[Book]) -> None:
    """Отображает все книги в библиотеке"""
    if not books:
        print("Библиотека пуста")
    else:
        for book in books:
            print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, "
                  f"Статус: {book.status}")


def change_book_status(books: List[Book], book_id: int, new_status: str) -> None:
    """
    Изменяет статус книги

    :param books: список с книгами
    :param book_id: ID книги
    :param new_status: новый статус книги
    """

    book = _find_book_by_id(books, book_id)
    if book:
        if new_status in ["в наличии", "выдана"]:
            book.status = new_status
            save_data(books)
            print(f"Статус книги с ID {book_id} изменен на '{new_status}'")
        else:
            print("Неверный статус. Используйте 'в наличии' или 'выдана'")
    else:
        print(f"Книга с ID {book_id} не найдена")


def _find_book_by_id(books: List[Book], book_id: int) -> Optional[Book]:
    """
    Ищет книгу по ID

    :param books: список с книгами
    :param book_id: ID книги
    :return: найденная книга
    """
    for book in books:
        if book.id == book_id:
            return book            
