from .buisness_logic import (
    load_books_from_library,
    add_book,
    remove_book,
    search_books,
    display_all_books,
    change_book_status,
    )


def main():
    """Основная функция для взаимодействия с пользователем"""

    books = load_books_from_library()

    while True:
        print("\n1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            try:
                year = int(year)
                add_book(books, title, author, year)
            except ValueError:
                print("Ошибка: Год должен быть числом")

        elif choice == "2":
            book_id = input("Введите ID книги для удаления: ")
            try:
                book_id = int(book_id)
                remove_book(books, book_id)
            except ValueError:
                print("Ошибка: ID должен быть числом")

        elif choice == "3":
            query = input("Введите название книги, автора или год издания: ")
            results = search_books(books, query)
            if results:
                print("Результаты поиска:")
                for book in results:
                    print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, "
                          f"Год: {book.year}, Статус: {book.status}")
            else:
                print("Книги не найдены")

        elif choice == "4":
            display_all_books(books)

        elif choice == "5":
            book_id = input("Введите ID книги: ")
            new_status = input("Введите новый статус (в наличии/выдана): ")
            try:
                book_id = int(book_id)
                change_book_status(books, book_id, new_status)
            except ValueError:
                print("Ошибка: ID должен быть числом")

        elif choice == "6":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите число от 1 до 6")


if __name__ == "__main__":
    main()
