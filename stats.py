# Takes in a filepath and returns the contents of the file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

#Counts the number of words in a string
def count_words(book_text):
    list_of_words = book_text.split()
    word_count = len(list_of_words)
    return f"{word_count} words found in the document"


def character_counter(book_text):
    
