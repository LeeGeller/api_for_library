def check_count_of_book(books: list) -> bool | str:
    for book in books:
        if book['count'] > 0:
            return True
        else:
            return f'Книга {book} закончилась'
