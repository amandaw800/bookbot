# Takes in a filepath and returns the contents of the file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

#Counts the number of words in a string
def count_words(book_text):
    list_of_words = book_text.split()
    word_count = len(list_of_words)
    return f"Found {word_count} total words"

#Counts the number of times each character appears in the string
def character_counter(book_text):
    counter = {}
    for char in book_text:
        if char.isalpha():
            char = char.lower()
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] +=1
    return counter

#Returns dict with char: key, count: value on a list
def two_key_val_dict(dic):
    named_key_val = {}
    
    list_of_dicts = []
    
    for key in dic:
        named_key_val["char"] = key
        named_key_val["count"] = dic[key]
        list_of_dicts.append(named_key_val)
        named_key_val = {}
    
    return list_of_dicts


def sort_by_count(dict):
    return dict["count"]


def print_character_count(list):
    for index, value in enumerate(list):
        current_dict = list[index]
        current_character = current_dict["char"]
        if current_character.isalpha():
            current_count = current_dict["count"]

            print(f"{current_character}: {current_count}")
