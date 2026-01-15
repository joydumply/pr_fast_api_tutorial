from fastapi import FastAPI

app = FastAPI() # creating a new app FastAPI

BOOKS = [
	{'title': 'Title One', 'author': 'Author One', 'category': 'science'},
	{'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
	{'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
	{'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
	{'title': 'Naruto', 'author': 'Massasi Kishimoto', 'category': 'legend'},
]

@app.get("/books")
async def read_all_books():
	return BOOKS

# Dynamic parameter
@app.get("/books/{book_title}")
async def read_book(book_title: str):
	for book in BOOKS:
		if book.get('title').casefold() == book_title.casefold(): #casefold() - is lowercase() analogue
			return book