import datetime

# Initial library book inventory
library_books = {
    "Harry Potter": {"quantity": 5, "author": "J.K. Rowling", "genre": "Fantasy"},
    "Sherlock Holmes": {"quantity": 3, "author": "Arthur Conan Doyle", "genre": "Mystery"},
    "Python Basics": {"quantity": 2, "author": "John Doe", "genre": "Programming"}
}

# Library member data
members = {}

# Book borrowing history for members
borrowed_books = {}

# Fine details
fine_per_day = 2  # Charge 2 units per day for late return

# Function to add a book to the library inventory
def add_book(book_name, quantity, author, genre):
    if book_name in library_books:
        library_books[book_name]["quantity"] += quantity
    else:
        library_books[book_name] = {"quantity": quantity, "author": author, "genre": genre}
    print(f"Added {quantity} copies of {book_name} by {author} ({genre})")

# Function to issue a book to a member
def issue_book(member_id, book_name):
    if book_name in library_books and library_books[book_name]["quantity"] > 0:
        library_books[book_name]["quantity"] -= 1
        if member_id not in borrowed_books:
            borrowed_books[member_id] = []
        borrowed_books[member_id].append({
            "book_name": book_name,
            "issue_date": datetime.date.today()
        })
        print(f"Issued {book_name} to member {member_id}")
    else:
        print(f"Sorry, {book_name} is unavailable")

# Function to return a book and calculate fine if applicable
def return_book(member_id, book_name):
    if member_id in borrowed_books:
        borrowed = [book for book in borrowed_books[member_id] if book["book_name"] == book_name]
        if borrowed:
            borrowed_books[member_id].remove(borrowed[0])
            issue_date = borrowed[0]["issue_date"]
            return_date = datetime.date.today()
            days_borrowed = (return_date - issue_date).days
            
            if days_borrowed > 14:  # Assuming 14 days borrowing period
                fine = (days_borrowed - 14) * fine_per_day
                print(f"Book returned late. You have a fine of {fine} units.")
            else:
                print("Book returned on time. No fine.")
            
            # Add book back to inventory
            library_books[book_name]["quantity"] += 1
        else:
            print(f"No record of {book_name} being borrowed by member {member_id}")
    else:
        print(f"No record of member {member_id}")

# Function to view available books
def view_books():
    print("Available Books:")
    for book, details in library_books.items():
        print(f"{book}: {details['quantity']} copies | Author: {details['author']} | Genre: {details['genre']}")

# Function to search for a book by name or author
def search_books(query):
    print(f"Search results for '{query}':")
    found = False
    for book, details in library_books.items():
        if query.lower() in book.lower() or query.lower() in details['author'].lower():
            print(f"{book}: {details['quantity']} copies | Author: {details['author']} | Genre: {details['genre']}")
            found = True
    if not found:
        print("No matching books found.")

# Function to register a new member
def register_member(member_id, member_name):
    if member_id not in members:
        members[member_id] = {"name": member_name, "joined": datetime.date.today()}
        print(f"Member {member_name} registered with ID {member_id}")
    else:
        print(f"Member ID {member_id} is already registered.")

# Function to view members
def view_members():
    print("Registered Members:")
    for member_id, details in members.items():
        print(f"ID: {member_id} | Name: {details['name']} | Joined: {details['joined']}")

# Main Library System Menu
def library_system():
    while True:
        print("\n---- LIBRARY SYSTEM ----")
        print("1. View Books")
        print("2. Add a Book")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. Search for a Book")
        print("6. Register a New Member")
        print("7. View Members")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_books()
        elif choice == "2":
            book_name = input("Enter book name: ")
            quantity = int(input("Enter quantity: "))
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            add_book(book_name, quantity, author, genre)
        elif choice == "3":
            member_id = input("Enter member ID: ")
            book_name = input("Enter book name: ")
            issue_book(member_id, book_name)
        elif choice == "4":
            member_id = input("Enter member ID: ")
            book_name = input("Enter book name to return: ")
            return_book(member_id, book_name)
        elif choice == "5":
            query = input("Enter book name or author to search: ")
            search_books(query)
        elif choice == "6":
            member_id = input("Enter new member ID: ")
            member_name = input("Enter member name: ")
            register_member(member_id, member_name)
        elif choice == "7":
            view_members()
        elif choice == "8":
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the Library System
if __name__ == "__main__":
    library_system()
