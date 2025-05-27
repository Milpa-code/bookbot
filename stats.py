def word_count():
    from main import get_book_text
    counter = 0
    words = get_book_text("books/frankenstein.txt")
    wordds = words.split()
    for word in wordds:
        if word != wordds:
            counter +=1
    print(f"{counter} words found in the document")
word_count()