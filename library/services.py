def check_count_of_book(books):
    for book in books:
        if book.count <= 0:
            return False
    return True
