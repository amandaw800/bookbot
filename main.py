from stats import count_words, get_book_text, character_counter, two_key_val_dict, sort_by_count, print_character_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]




    book_text = get_book_text(book_path)

    total_words = count_words(book_text)
    character_counts = character_counter(book_text)


    list_to_sort = two_key_val_dict(character_counts)

    list_to_sort.sort(reverse=True, key=sort_by_count)
   

    ################################################

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(total_words)
    print("--------- Character Count -------")
    print_character_count(list_to_sort)
    print("============= END ===============")








main()
