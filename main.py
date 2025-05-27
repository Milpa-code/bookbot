def get_book_text(filepath):
    with open(filepath) as f:
        read_text = f.read()
    return read_text
def main():
    result = get_book_text("books/frankenstein.txt")
    print(result)
def word_count():
    counter = 0
    words = get_book_text("books/frankenstein.txt")
    wordds = words.split()
    for word in wordds:
        if word != wordds:
            counter +=1
    print(f"{counter} words found in the document")
word_count()