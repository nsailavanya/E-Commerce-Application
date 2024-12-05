import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 

class LibraryManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("500x700")
        self.master.config(bg='#f0f8ff')
        self.books = []
        self.lend_list = []
        self.librarians = []

        # Title Label with animation
        self.login_label = tk.Label(self.master, text="Library Management System", font=("Arial", 18, "bold"), bg='#f0f8ff', fg='#2F4F4F')
        self.login_label.pack(pady=20)
        self.animate_index = 0
        self.animate_colors = ["#2F4F4F", "#4169E1", "#32CD32", "#FFD700", "#FF6347"]
        self.animation_running = True
        self.animate_title()

        # Username Entry
        self.username_label = tk.Label(self.master, text="Username", font=("Arial", 12), bg='#f0f8ff', fg='#2F4F4F')
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.master, font=("Arial", 12), bd=2, relief="solid", highlightthickness=2, highlightbackground="#4169E1")
        self.username_entry.pack(pady=5, padx=20, fill='x')

        # Password Entry
        self.password_label = tk.Label(self.master, text="Password", font=("Arial", 12), bg='#f0f8ff', fg='#2F4F4F')
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.master, font=("Arial", 12), show="*", bd=2, relief="solid", highlightthickness=2, highlightbackground="#4169E1")
        self.password_entry.pack(pady=5, padx=20, fill='x')

        # Buttons
        self.login_button = tk.Button(self.master, text="Login", command=self.login, font=("Arial", 12), bg="#32CD32", fg="white", relief="raised")
        self.login_button.pack(pady=10)
        self.register_button = tk.Button(self.master, text="Register", command=self.register, font=("Arial", 12), bg="#FFD700", fg="black", relief="raised")
        self.register_button.pack(pady=10)

        # Book Image
        try:
            self.book_image = Image.open("book.jpg")
            self.book_image = self.book_image.resize((500, 500), Image.LANCZOS)  # Updated method
            self.book_photo = ImageTk.PhotoImage(self.book_image)
            self.image_label = tk.Label(self.master, image=self.book_photo, bg='#f0f8ff')
            self.image_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading book image: {e}")

    def animate_title(self):
        if self.animation_running and self.login_label.winfo_exists():
            self.login_label.config(fg=self.animate_colors[self.animate_index])
            self.animate_index = (self.animate_index + 1) % len(self.animate_colors)
            self.master.after(500, self.animate_title)

    def stop_animation(self):
        self.animation_running = False

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if [username, password] in self.librarians:
            self.stop_animation()
            self.clear_screen()
            self.library_management_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            self.librarians.append([username, password])
            messagebox.showinfo("Success", "Registration successful")
        else:
            messagebox.showerror("Error", "Please enter valid credentials")

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def library_management_screen(self):
        self.add_book_label = tk.Label(self.master, text="Add Book", font=("Arial", 16), bg='#f0f8ff', fg='#2F4F4F')
        self.add_book_label.pack(pady=10)
        self.add_book_entry = tk.Entry(self.master, font=("Arial", 12), bd=2, relief="solid", highlightthickness=2, highlightbackground="#4169E1")
        self.add_book_entry.pack(pady=5, padx=20, fill='x')
        self.add_book_button = tk.Button(self.master, text="Add Book", command=self.add_book, font=("Arial", 12), bg="#32CD32", fg="white", relief="raised")
        self.add_book_button.pack(pady=10)

        self.remove_book_label = tk.Label(self.master, text="Remove Book", font=("Arial", 16), bg='#f0f8ff', fg='#2F4F4F')
        self.remove_book_label.pack(pady=10)
        self.remove_book_entry = tk.Entry(self.master, font=("Arial", 12), bd=2, relief="solid", highlightthickness=2, highlightbackground="#4169E1")
        self.remove_book_entry.pack(pady=5, padx=20, fill='x')
        self.remove_book_button = tk.Button(self.master, text="Remove Book", command=self.remove_book, font=("Arial", 12), bg="#FF6347", fg="white", relief="raised")
        self.remove_book_button.pack(pady=10)

        self.issue_book_label = tk.Label(self.master, text="Issue Book", font=("Arial", 16), bg='#f0f8ff', fg='#2F4F4F')
        self.issue_book_label.pack(pady=10)
        self.issue_book_entry = tk.Entry(self.master, font=("Arial", 12), bd=2, relief="solid", highlightthickness=2, highlightbackground="#4169E1")
        self.issue_book_entry.pack(pady=5, padx=20, fill='x')
        self.issue_book_button = tk.Button(self.master, text="Issue Book", command=self.issue_book, font=("Arial", 12), bg="#4169E1", fg="white", relief="raised")
        self.issue_book_button.pack(pady=10)

        self.view_books_button = tk.Button(self.master, text="View Books", command=self.view_books, font=("Arial", 12), bg="#FFD700", fg="black", relief="raised")
        self.view_books_button.pack(pady=20)

    def add_book(self):
        book = self.add_book_entry.get()
        if book:
            self.books.append(book)
            messagebox.showinfo("Success", f"Book '{book}' added successfully")
        else:
            messagebox.showerror("Error", "Please enter a book name")
        self.add_book_entry.delete(0, tk.END)

    def remove_book(self):
        book = self.remove_book_entry.get()
        if book in self.books:
            self.books.remove(book)
            messagebox.showinfo("Success", f"Book '{book}' removed successfully")
        else:
            messagebox.showerror("Error", f"Book '{book}' not found")
        self.remove_book_entry.delete(0, tk.END)

    def issue_book(self):
        book = self.issue_book_entry.get()
        if book in self.books:
            self.books.remove(book)
            self.lend_list.append(book)
            messagebox.showinfo("Success", f"Book '{book}' issued successfully")
        else:
            messagebox.showerror("Error", f"Book '{book}' not found")
        self.issue_book_entry.delete(0, tk.END)

    def view_books(self):
        if self.books:
            message = "\n".join(self.books)
            messagebox.showinfo("Books", message)
        else:
            messagebox.showinfo("Books", "No books available")


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagement(root)
    root.mainloop()
