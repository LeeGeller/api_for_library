def check_count_of_book(books: list) -> bool | str:
    for book in books:
        if book['count'] > 0:
            return True
    return False
