def get_book_text():
    with open("/home/milpa/git/bookbot/books/frankenstein.txt", 'w', encoding="utf-8") as f:
       print(f.read())
