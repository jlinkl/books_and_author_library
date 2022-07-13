import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Charles Dickens")
author_repository.save(author1)
author2 = Author("Emily Brontee")
author_repository.save(author2)

# author_repository.select_all()

book1 = Book("A Christmas Carol", "Classic", author1)
book_repository.save(book1)

book2 = Book("Wuthering Heights", "Classic", author2)
book_repository.save(book2)

results = book_repository.select_all()


pdb.set_trace()