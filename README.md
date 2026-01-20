# FastAPI tutorial from [cource](https://www.udemy.com/course/fastapi-the-complete-course/)

## books.py

A RESTful API for managing a book collection built with FastAPI. Implements full CRUD operations with multiple filtering capabilities:

**Features:**

- `GET /books` - Retrieve all books
- `GET /books/{book_title}` - Get a specific book by title (case-insensitive)
- `GET /books/` - Filter books by category (query parameter)
- `GET /books/{book_author}/` - Filter books by author and category combination
- `GET /books/author/{author}` - Get all books by a specific author
- `POST /books/create_book` - Add a new book to the collection
- `PUT /books/update_book` - Update an existing book by title
- `DELETE /books/delete_book/{book_title}` - Remove a book by title

All search operations use case-insensitive matching. The API manages an in-memory list of books with fields: title, author, and category.
