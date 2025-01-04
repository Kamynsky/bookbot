def openbook(book):
    with open(book) as f:
        book_content=f.read()
        print(book_content)  
        return book_content
def wordcounts(book_content):
    word_count=len(book_content.split())
    print("word count :",word_count)
def words
    

    
book_content=openbook("books/frankenstein.txt")
wordcounts(book_content)

# Add a new function to your script that takes the text from the book as a string, and returns the number of times each character appears in the string. Convert any character to lowercase, we don't want duplicates.
# use dict to count number of words
# use def for each function
