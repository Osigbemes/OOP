from services import AuthService, LibraryService
from user import User


class CLIController:
    def __init__(self):
        self.auth = AuthService()
        self.library = LibraryService()
        self.current_user = None

    def run(self):
        while True:
            if not self.current_user:
                self.auth_menu()
            else:
                if self.current_user.role == "admin":
                    self.admin_menu()
                else:
                    self.member_menu()

    # ------------- MENUS ----------------

    def auth_menu(self):
        print("\n=== LIBRARY SYSTEM ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            self.login()
        elif choice == "2":
            self.register()
        elif choice == "3":
            exit()

    def login(self):
        uid = input("User ID: ")
        pw = input("Password: ")
        user : User = self.auth.login(uid, pw)
        if user:
            print(f"Welcome {user.username}!")
            self.current_user = user

    def register(self):
        uid = input("User ID: ")
        name = input("Full Name: ")
        email = input("Email: ")
        pw = input("Password: ")

        user : User = self.auth.register(uid, name, email, pw)
        if user:
            self.current_user = user

    # ============ ADMIN MENU ============
    def admin_menu(self):
        print("\n=== ADMIN MENU ===")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. View Books")
        print("5. Logout")

        choice = input("Choose: ")

        match choice:
            case "1":
                self.add_book()
            case "2":
                self.update_book()
            case "3":
                self.delete_book()
            case "4":
                self.library.list_books()
            case "5":
                self.current_user = None

    # Admin Actions
    def add_book(self):
        bid = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        qty = int(input("Quantity: "))

        self.library.add_book(bid, title, author, qty)

    def update_book(self):
        bid = input("Book ID: ")
        title = input("New Title (Enter to skip): ")
        author = input("New Author (Enter to skip): ")
        qty = input("New Quantity (Enter to skip): ")

        self.library.update_book(
            bid,
            title or None,
            author or None,
            int(qty) if qty else None
        )

    def delete_book(self):
        bid = input("Book ID to delete: ")
        self.library.delete_book(bid)

    # ============ MEMBER MENU ============
    def member_menu(self):
        print("\n=== MEMBER MENU ===")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View My Borrowed Books")
        print("5. Logout")

        choice = input("Choose: ")

        match choice:
            case "1":
                self.library.list_books()
            case "2":
                self.borrow_book()
            case "3":
                self.return_book()
            case "4":
                self.library.list_borrowed(self.current_user.user_id)
            case "5":
                self.current_user = None

    # Member Actions
    def borrow_book(self):
        bid = input("Book ID: ")
        self.library.borrow_book(self.current_user.user_id, bid)

    def return_book(self):
        rid = int(input("Borrow Record ID: "))
        self.library.return_book(rid)


# =============================
# RUN THE APPLICATION
# =============================
if __name__ == "__main__":
    CLIController().run()