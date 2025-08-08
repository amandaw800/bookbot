# Takes in a filepath and returns the contents of the file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

#Counts the number of words in a string
def count_words(book_text):
    list_of_words = book_text.split()
    word_count = 0

    for word in list_of_words:
        word_count +=1
    return f"{word_count} words found in the document"



def main():
    book_text = get_book_text("books/frankenstein.txt")
    total_words = count_words(book_text)




main()
