from fastapi import FastAPI

app = FastAPI()

BOOKS = [
	{'title': 'Title One', 'author': 'Author One', 'category': 'science'},
	{'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
	{'title': 'Title Three', 'author': 'Author Three', 'category': 'science'},
	{'title': 'Title Four', 'author': 'Author Four', 'category': 'science'},
]

@app.get("/books/")
async def read_all_books():
	return BOOKS