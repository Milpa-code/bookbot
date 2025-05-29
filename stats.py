def word_count():
    from main import get_book_text
    counter = 0
    words = get_book_text("books/frankenstein.txt")
    wordds = words.split()
    for word in wordds:
        if word != wordds:
            counter +=1
    print(f"{counter} words found in the document")
def indevidual_characters():
     from main import get_book_text
     import string
     freq = {}
     words = get_book_text("books/frankenstein.txt")
     characters = words.lower()
     for symbol in characters:
        if symbol in freq:
            freq[symbol] += 1
        else:
            freq[symbol] = 1
     print(freq)
indevidual_characters()