def openbook(book):
    with open(book) as f:
        book_content=()
        book_content=f.read()
        content_list=[]
        content_list=book_content.split()
        word_count=len(content_list)
        
        return book_content, word_count
    
print(openbook("books/frankenstein.txt"))
