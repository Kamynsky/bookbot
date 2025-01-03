def openbook(book):
    with open(book) as f:
        book_content=f.read()
        return book_content
    
print(openbook("books/frankenstein.txt"))
