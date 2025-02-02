"""Библиотека для управления коллекцией книг."""
class Book:
    def __init__(self, title: str, author: str, year: int, genre: str,  pages: int) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if Book.checking_the_string(value, error="Название должно быть не пустой строкой"):
            self._title = value

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str):
        if Book.checking_the_string(value, error="Имя автора должно быть строкой"):
            self._author = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int):
        if Book.checking_the_integer(value, error="Год должен быть положительным числом"):
            self._year = value

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    def genre(self, value: str):
        if Book.checking_the_string(value, error="Жанр должен быть строкой"):
            self._genre = value

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if Book.checking_the_integer(value, error="Страница должна быть положительным числом"):
            self._pages = value

    @staticmethod
    def checking_the_integer(value: int, error: str) -> bool or str:
        if isinstance(value, int) and value >= 0:
            return True
        else:
            raise ValueError(error)

    @staticmethod
    def checking_the_string(value: str, error: str) -> bool or str:
        if isinstance(value, str):
            return True
        else:
            raise ValueError(error)

    def __str__(self) -> str:
        return f'{self.title}, {self.author}, {self.year}, {self.genre}, {self.pages}'

    def __repr__(self) -> str:
        return (f'Book(title={self.title}), Book(author={self.author}), Book(year={self.year}),'
                f' Book(genre={self.genre}), Book(pages={self.pages})')


class Library:

    def __init__(self) -> None:
        self.bookshelf = []

    def add_book(self, book) -> None:
        self.bookshelf.append(book)

    def search_by_title(self, title):
        """Поиск книги по навзанию."""
        for i in self.bookshelf:
            if i.title == title:
                return i
        return "Книга отсутствует в библиотеке"

    def get_books_by_author(self, author: str) -> list:
        """Список всех книг автора."""
        return [i for i in self.bookshelf if i.author == author]

    def get_books_sorted_by_year(self) -> list:
        """Отсортированый список по году выпуска."""
        return sorted(self.bookshelf, key=lambda x: x.year)

    def remove_book(self, book: str) -> None or str:
        if book in self.bookshelf:
            list(self.bookshelf).remove(book)
        else:
            return "Книга отсутсвует в библиотеке"

    def __len__(self) -> int:
        return len(self.bookshelf)

    def __repr__(self):
        return f"Library({self.bookshelf})"


library = Library()
book1 = Book("Title1", "Author1", 2001, "Genre1", 300)
book2 = Book("Title2", "Author2", 1999, "Genre2", 150)
book3 = Book("Title3", "Author1", 2010, "Genre3", 400)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.search_by_title("Title1"))
print(library.get_books_by_author("Author1"))
print(library.get_books_sorted_by_year())
