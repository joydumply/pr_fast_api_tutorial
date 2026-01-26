from fastapi import FastAPI, Path, Query, HTTPException, status
from models import Book, BookRequest

app = FastAPI()

BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby", "A very nice book", 5, 2012),
    Book(2, "Be fast with FastAPI", "codingwithroby", "A very nice book", 4, 2013),
    Book(
        3,
        "Naruto: Shippuden",
        "Massashi Kishimoto",
        "The Legendary Manga Book",
        5,
        2008,
    ),
    Book(4, "Boruto", "Massashi Kishimoto", "A piece of dog shit", 1, 2022),
    Book(
        5,
        "Harry Potter And The Philosopher's Stone",
        "J. Rowling",
        "A great book",
        4,
        1997,
    ),
    Book(
        6,
        "Harry Potter And The Chamber of Secrets",
        "J. Rowling",
        "The best book",
        5,
        1998,
    ),
    Book(
        7,
        "Harry Potter And The Prisoner of Azkaban ",
        "J. Rowling",
        "Nice book",
        4,
        1999,
    ),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def get_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def get_book(book_id: int = Path(gt=0)):
    # Junior level
    # for book in BOOKS:
    #     if book.id == book_id:
    #         return book

    # Middle level
    book = next((b for b in BOOKS if b.id == book_id), None)

    if book is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return book


@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    return [b for b in BOOKS if b.rating == book_rating]


@app.get("/books/year/", status_code=status.HTTP_200_OK)
async def get_books_by_year(published_year: int = Query(gt=-1, lt=2026)):
    return [b for b in BOOKS if b.published_year == published_year]


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
def create_book(book_request: BookRequest):
    new_book = find_book_id(Book(**book_request.model_dump()))
    BOOKS.append(new_book)


def find_book_id(book: Book):
    # if len(BOOKS) > 0:
    # 	book.id = BOOKS[-1].id + 1
    # else:
    # 	book.id = 1

    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1  # Тернарный оператор

    return book


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    change_flag = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            change_flag = True

    if not change_flag:
        raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    global BOOKS

    book_exists = next((b for b in BOOKS if b.id == book_id), None)

    if not book_exists:
        raise HTTPException(status_code=404, detail="Item not found")

    BOOKS = [b for b in BOOKS if b.id != book_id]
