from fastapi import FastAPI
from models import Book, BookRequest

app = FastAPI()

BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby", "A very nice book", 5),
    Book(2, "Be fast with FastAPI", "codingwithroby", "A very nice book", 4),
    Book(3, "Naruto: Shippuden", "Massashi Kishimoto", "The Legendary Manga Book", 5),
    Book(4, "Boruto", "Massashi Kishimoto", "A piece of dog shit", 1),
    Book(
        5, "Harry Potter And The Philosopher's Stone", "J. Rowling", "A great book", 4
    ),
    Book(
        6, "Harry Potter And The Chamber of Secrets", "J. Rowling", "The best book", 5
    ),
    Book(7, "Harry Potter And The Prisoner of Azkaban ", "J. Rowling", "Nice book", 4),
]


@app.get("/books")
async def get_all_books():
    return BOOKS


@app.post("/create-book")
def create_book(book_request: BookRequest):
	new_book = find_book_id(Book(**book_request.model_dump()))
	BOOKS.append(new_book)

def find_book_id(book: Book):
	
	# if len(BOOKS) > 0:
	# 	book.id = BOOKS[-1].id + 1
	# else:
	# 	book.id = 1

	book.id = 1  if len(BOOKS) == 0 else BOOKS[-1].id + 1 # Тернарный оператор
	
	return book
		