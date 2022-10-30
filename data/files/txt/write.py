"""Docstring."""


def search(path):
    """Filter lines and add to string."""
    print("Searching...")
    sections = ""
    books = "Books:\n"
    with open(path, encoding="utf8") as file:
        for line in file:
            if line[:7] == "Section":
                sections += line
            else:
                books += line
    print("Done!")
    print(sections)
    print(books)
    return f"{sections}\n\n{books}"


def save(path, data):
    """Write data to file at path."""
    print("Saving...")
    with open(path, "w", encoding="utf-8") as file:
        file.write(data)
    print("Done!")


def run():
    """Run the program."""
    data = search("/home/sam/mygit/com411/data/files/txt/books.txt")
    save("/home/sam/mygit/com411/data/files/txt/section-books.txt", data)


if __name__ == "__main__":
    run()
