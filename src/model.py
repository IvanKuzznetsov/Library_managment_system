from typing import Dict


class Book:
    """Класс, представляющий книгу в библиотеке"""

    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии"):
        """
        Инициализирует объект Book.

        :param id: Уникальный идентификатор книги
        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания
        """
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> Dict:
        """Преобразует объект Book в словарь"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Book':
        """Создает объект Book из словаря"""
        return cls(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"]
        )
