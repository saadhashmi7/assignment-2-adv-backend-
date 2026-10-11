class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def _find_title(self, book_title):
        wanted = book_title.strip().lower()

        for title in self.books:
            if title.lower() == wanted:
                return title

        return None

    def add_book(self, book):
        if not isinstance(book, str) or not book.strip():
            print("Cannot add a book without a valid title.")
            return False

        title = book.strip()

        if self._find_title(title) is not None:
            print(f'"{title}" is already in the collection.')
            return False

        self.books.append(title)
        print(f'Added: "{title}"')
        return True

    def remove_book(self, book_title):
        if not isinstance(book_title, str):
            print("Cannot remove a book without a valid title.")
            return False

        title = self._find_title(book_title)

        if title is None:
            print(f'"{book_title}" was not found in the collection.')
            return False

        self.books.remove(title)
        print(f'Removed: "{title}"')
        return True

    def search_book(self, keyword):
        if not isinstance(keyword, str) or not keyword.strip():
            return []

        keyword = keyword.strip().lower()
        return [title for title in self.books if keyword in title.lower()]

    def display_books(self):
        print(f"\nBooks in {self.name} ({len(self.books)} in total)")
        print("-" * 50)

        if not self.books:
            print("The collection is empty.")
            return

        for number, title in enumerate(self.books, start=1):
            print(f"{number}. {title}")


def main():
    print("Question # 03: Library Management System\n")

    library = Library("City Central Library")

    library.add_book("Python Crash Course")
    library.add_book("Clean Code")
    library.add_book("Learning Python")
    library.add_book("Database System Concepts")
    library.add_book("Fluent Python")
    library.add_book("clean code")

    library.display_books()

    print('\nSearch results for "python":', library.search_book("python"))
    print('Search results for "java"  :', library.search_book("java"))
    print()

    library.remove_book("Clean Code")
    library.remove_book("Operating Systems")

    library.display_books()


if __name__ == "__main__":
    main()