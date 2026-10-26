class Chapter:
    def __init__(self, title: str):
        self.title = title

class Book:
    def __init__(self):
        # The Book creates and owns these Chapter objects directly
        self.chapters = [Chapter("Introduction"), Chapter("Conclusion")]


# --- Running the code ---
# 1. Instantiate the parent object (Book)
my_book = Book()

# 2. Iterate through the tightly coupled child objects (Chapters) created inside it
for chapter in my_book.chapters:
    print(f"Chapter created: {chapter.title}")

# If the Book object is deleted, self.chapters is also deleted from memory
