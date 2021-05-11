# Andrew Niemann, 5/11/21, Module 12

import mysql.connector
from mysql.connector import errorcode

config = {
  "user": "whatabook_user",
  "password": "MySQL8IsGreat!",
  "host": "127.0.0.1",
  "database": "whatabook",
  "raise_on_warnings": True
}

def show_menu():
  print("\n\n\t- Main Menu -\n")
  print("\t1. View Books")
  print("\t2. View Store Locations")
  print("\t3. My Account")
  print("\t4. Exit program")
  try:
    choice = int(input("\nEnter a number to navigate the menu: "))
    return choice
  except ValueError:
    print("Please ensure you are entering an integer.")

def show_books(_cursor):
  _cursor.execute("SELECT * FROM book")
  books = cursor.fetchall()
  print("\nList of Available Books:")
  for book in books:
    print(f"\t{book[0]}. {book[1]}, by {book[3]}")
  # see_details = input("\nEnter a book's number to see a brief description,\nor press 'Enter' to return to the Main Menu: ")
  input("\nPress 'Enter' to return to the Main Menu...")
  
def show_locations(_cursor):
  _cursor.execute("SELECT locale FROM store")
  locations = cursor.fetchall()
  print("\nList of Whatabook Branches:")
  for location in locations:
    print(f"\tLocation: {location[0]}")
  input("\nPress 'Enter' to return to the Main Menu...")

def validate_user(_cursor):
  _cursor.execute("SELECT * FROM user")
  user_fetch = _cursor.fetchall() # returns list of tuples
  userlist = [] # creates regular list that will be used
  for row in user_fetch:
    userlist.append(int(row[0])) # adds first element of each SQL tuple to new list
  login = int(input("Please enter your user ID: "))
  if login in userlist: # checks user input against list of user_ids
    print(f"\nWelcome back, {user_fetch[login-1][1]}!")
    input("Press 'Enter' to continue...")
    show_account_menu(_cursor, login)
  else:
    input("User not found. Please try again.\n")
    validate_user(_cursor)

def show_account_menu(_cursor, _user_id):
  while True:
    print("\n\n  - My Account -\n")
    print("  1. View Wishlist")
    print("  2. Add Book")
    print("  3. Main Menu")
    try:
      choice = int(input("\nEnter a number to navigate the menu: "))
    except ValueError:
      print("Please ensure you are entering an integer.")
    if choice == 1:
      show_wishlist(_cursor, _user_id)
    if choice == 2:
      show_books_to_add(_cursor, _user_id)
    if choice == 3:
      break
    else:
      input("Invalid option entered. Press 'Enter' to continue...")

def show_wishlist(_cursor, _user_id):
  _cursor.execute("SELECT user.user_id, book.book_id, book_name FROM wishlist JOIN user ON user.user_id = wishlist.user_id JOIN book ON book.book_id = wishlist.book_id WHERE wishlist.user_id = {}".format(_user_id))
  wishlist_books = cursor.fetchall()
  print("\nWishlist items:")
  for book in wishlist_books:
    print("  " + book[2])
  input("\nPress 'Enter' to return to the account menu...")

def show_books_to_add(_cursor, _user_id):
  while True:
    _cursor.execute("SELECT book_id, book_name FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    wishlist_books = cursor.fetchall()
    print("\nList of books NOT on your wishlist:")
    booklist = [] # same trick as validating user_id
    for book in wishlist_books:
      print(f"  {book[0]}. {book[1]}")
      booklist.append(book[0])
    book_to_add = input("\nPress 'Enter' to return to the previous menu,\nor enter a book's ID number to add it to your wishlist: ")
    if book_to_add == "":
      break
    elif int(book_to_add) not in booklist:
      print(booklist)
      input("Invalid book ID entered. Press 'Enter' to continue...")
    elif int(book_to_add) in booklist:
      add_book_to_wishlist(_cursor, _user_id, book_to_add)

def add_book_to_wishlist(_cursor, _user_id, _book_id):
  _cursor.execute(f"INSERT INTO wishlist(user_id, book_id) VALUES({_user_id}, {_book_id})")
  db.commit()
  input(f"\nBook #{_book_id} added! Press 'Enter' to continue...")


db = mysql.connector.connect(**config)
cursor = db.cursor()
while True:
  choice = show_menu()
  if choice == 1: # book list and back
    show_books(cursor)
  elif choice == 2: # location and back
    show_locations(cursor)
  elif choice == 3: # valid user_id directs to account menu
    validate_user(cursor)
  elif choice == 4:
    break
  else:
    input("Invalid input: Press 'Enter' to try again.")