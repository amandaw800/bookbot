from stats import count_words, get_book_text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    total_words = count_words(book_text)

    print(total_words)




main()
