def openbook(book):
    with open(book) as f:
        book_content=f.read()
        print(book_content)  
        return book_content
def wordcounts(book_content):
    word_count=len(book_content.split())
    print(word_count,"words found in the document")
def charcount(book_content):
    lower_string=book_content.lower()
    char_dict={}
    for k in lower_string:
        if k.islower():
            if k not in char_dict:
                char_dict[k]=1
            else:
                char_dict[k]+=1
        else:
            continue
    sorted_char_dict=dict(sorted(char_dict.items(),key=lambda item: item[1],reverse=True))
    for item in sorted_char_dict:
        print(f"The '{item}' character was found {sorted_char_dict[item]} times")
            
    

    
book_content=openbook("books/frankenstein.txt")
wordcounts(book_content)
charcount(book_content)

