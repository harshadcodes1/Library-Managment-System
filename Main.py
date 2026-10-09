import json
from datetime import datetime


# Book Class

class Book:

    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def display(self):

        print("\n-----------------------------")
        print("Book ID   :", self.book_id)
        print("Title     :", self.title)
        print("Author    :", self.author)
        print("Quantity  :", self.quantity)


# Student Class

class Student:

    def __init__(self, student_id, name, branch):
        self.student_id = student_id
        self.name = name
        self.branch = branch

    def display(self):

        print("\n-----------------------------")
        print("Student ID:", self.student_id)
        print("Name      :", self.name)
        print("Branch    :", self.branch)


# File Handling Functions

def load_data(filename):

    try:

        with open("D:\INTERNSHIP SEM _ IV\Harshad.txt", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):

        return []


def save_data(filename, data):

    with open("D:\INTERNSHIP SEM _ IV\Harshad.txt", "w") as file:

        json.dump(data, file, indent=4)


# Add Book

def add_book():

    books = load_data("books.json")

    print("\n========== ADD BOOK ==========")

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    try:

        quantity = int(input("Enter Quantity: "))

    except ValueError:

        print("Please enter a valid quantity.")
        return

    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity
    }

    books.append(book)

    save_data("books.json", books)

    print("\nBook added successfully!")


# Display Books

def display_books():

    books = load_data("books.json")

    print("\n========== BOOK LIST ==========")

    if not books:

        print("No books available.")
        return

    for data in books:

        book = Book(
            data["book_id"],
            data["title"],
            data["author"],
            data["quantity"]
        )

        book.display()


# Search Book

def search_book():

    books = load_data("books.json")

    keyword = input("\nEnter book title or author: ")

    found = False

    for data in books:

        if (
            keyword.lower() in data["title"].lower()
            or
            keyword.lower() in data["author"].lower()
        ):

            book = Book(
                data["book_id"],
                data["title"],
                data["author"],
                data["quantity"]
            )

            book.display()

            found = True

    if not found:

        print("\nBook not found.")


# Add Student

def add_student():

    students = load_data("students.json")

    print("\n========== ADD STUDENT ==========")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")

    student = {
        "student_id": student_id,
        "name": name,
        "branch": branch
    }

    students.append(student)

    save_data("students.json", students)

    print("\nStudent added successfully!")


# Display Students

def display_students():

    students = load_data("students.json")

    print("\n========== STUDENT LIST ==========")

    if not students:

        print("No students registered.")
        return

    for data in students:

        student = Student(
            data["student_id"],
            data["name"],
            data["branch"]
        )

        student.display()

# Issue Book

def issue_book():

    books = load_data("books.json")
    students = load_data("students.json")
    issued = load_data("issued_books.json")

    print("\n========== ISSUE BOOK ==========")

    book_id = input("Enter Book ID: ")
    student_id = input("Enter Student ID: ")

    # Find book

    book = None

    for b in books:

        if b["book_id"] == book_id:
            book = b
            break

    if book is None:

        print("Book not found.")
        return

    # Check quantity

    if book["quantity"] <= 0:

        print("Book is currently unavailable.")
        return

    # Find student

    student = None

    for s in students:

        if s["student_id"] == student_id:
            student = s
            break

    if student is None:

        print("Student not found.")
        return

    # Reduce book quantity

    book["quantity"] -= 1

    issue_data = {

        "book_id": book_id,
        "book_title": book["title"],
        "student_id": student_id,
        "student_name": student["name"],
        "issue_date": datetime.now().strftime("%d-%m-%Y")

    }

    issued.append(issue_data)

    save_data("books.json", books)
    save_data("issued_books.json", issued)

    print("\nBook issued successfully!")


# Return Book

def return_book():

    books = load_data("books.json")
    issued = load_data("issued_books.json")

    print("\n========== RETURN BOOK ==========")

    book_id = input("Enter Book ID: ")
    student_id = input("Enter Student ID: ")

    record = None

    for item in issued:

        if (
            item["book_id"] == book_id
            and
            item["student_id"] == student_id
        ):

            record = item
            break

    if record is None:

        print("Issued book record not found.")
        return

    # Increase quantity

    for book in books:

        if book["book_id"] == book_id:

            book["quantity"] += 1
            break

    # Remove issue record

    issued.remove(record)

    save_data("books.json", books)
    save_data("issued_books.json", issued)

    print("\nBook returned successfully!")


# View Issued Books

def view_issued_books():

    issued = load_data("issued_books.json")

    print("\n========== ISSUED BOOKS ==========")

    if not issued:

        print("No books are currently issued.")
        return

    for item in issued:

        print("\nBook ID     :", item["book_id"])
        print("Book Title  :", item["book_title"])
        print("Student ID  :", item["student_id"])
        print("Student Name:", item["student_name"])
        print("Issue Date  :", item["issue_date"])



# Delete Book

def delete_book():

    books = load_data("books.json")

    book_id = input("\nEnter Book ID to delete: ")

    for book in books:

        if book["book_id"] == book_id:

            books.remove(book)

            save_data("books.json", books)

            print("\nBook deleted successfully!")
            return

    print("\nBook not found.")


# Main Menu

def main():

    while True:

        print("\n")
        print("==========================================")
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("==========================================")

        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Add Student")
        print("5. Display Students")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. View Issued Books")
        print("9. Delete Book")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            add_book()

        elif choice == "2":

            display_books()

        elif choice == "3":

            search_book()

        elif choice == "4":

            add_student()

        elif choice == "5":

            display_students()

        elif choice == "6":

            issue_book()

        elif choice == "7":

            return_book()

        elif choice == "8":

            view_issued_books()

        elif choice == "9":

            delete_book()

        elif choice == "10":

            print("\nThank you for using Library Management System!")
            break

        else:

            print("\nInvalid choice. Please try again.")


# Program Start

if __name__ == "__main__":

    main()