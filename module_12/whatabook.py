# Andrew Niemann, 5/12/21, Module 12

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
  while True:
    print("\n\n\t- Main Menu -\n")
    print("\t1. View Books")
    print("\t2. View Store Locations")
    print("\t3. My Account")
    print("\t4. Exit program")
    choice = 0
    try:
      choice = int(input("\nEnter a number to navigate the menu: "))
    except ValueError:
      input("Invalid input. Press 'Enter' to try again...")
      continue
    if choice == 1:
      show_books(cursor) # book list and back
    elif choice == 2: 
      show_locations(cursor) # location and back
    elif choice == 3:
      validate_user(cursor) # valid user_id directs to account menu, else returns
    elif choice == 4:
      break # exits loop/function/program
    else:
      input("Invalid input. Press 'Enter' to try again...") # repeats loop/function

def show_books(_cursor):
  _cursor.execute("SELECT * FROM book")
  books = cursor.fetchall()
  print("\nList of Available Books:")
  for book in books:
    print(f"\t{book[0]}. {book[1]}, by {book[3]}") # print(book_id. book_name, by author)
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
  # the below technique to check input against SQL query results is also used in show_books_to_add()
  # inspiration came from https://stackoverflow.com/questions/1553275/how-to-strip-a-list-of-tuple-with-python
  userlist = [] # creates regular list that will be used
  for row in user_fetch:
    userlist.append(int(row[0])) # adds first element of each SQL tuple to new list
  try:
    login = int(input("Please enter your user ID: "))
  except:
    login_invalid = input("Invalid input. Enter '1' to try again, or press 'Enter' to return to the Main Menu: ")
    if login_invalid == "1":
      validate_user(_cursor) # restarts user_id prompt
    else:
      return None # exits loop/function, returns to main menu
  if login in userlist: # checks user input against list of user_ids
    print(f"\nWelcome back, {user_fetch[login-1][1]}!")
    input("Press 'Enter' to continue...")
    show_account_menu(_cursor, login)
  else:
    print("User not found. Please try again.\n")
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
      input("Invalid input. Press 'Enter' to continue...")
      continue
    if choice == 1: # wishlist and back
      show_wishlist(_cursor, _user_id)
    elif choice == 2: # books to add. from there, "add" function will be called repeatedly until input directs flow back here
      show_books_to_add(_cursor, _user_id)
    elif choice == 3: # exits loop/function, returns to main menu
      break
    else:
      input("Invalid input. Press 'Enter' to continue...")

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
    booklist = [] # same trick as user_id validation, this time we will make sure book is not already in wishlist
    for book in wishlist_books:
      print(f"  {book[0]}. {book[1]}")
      booklist.append(book[0]) # add the book_id to the list we created
    book_to_add = input("\nPress 'Enter' to return to the previous menu,\nor enter a book's ID number to add it to your wishlist: ")
    if book_to_add == "":
      break # exits loop/function, returns to account menu
    elif int(book_to_add) not in booklist: # check input against list we created
      print(booklist)
      input("Invalid book ID entered. Press 'Enter' to continue...")
    elif int(book_to_add) in booklist:
      add_book_to_wishlist(_cursor, _user_id, book_to_add) # adds book, restarts show_books_to_add()

def add_book_to_wishlist(_cursor, _user_id, _book_id):
  _cursor.execute(f"INSERT INTO wishlist(user_id, book_id) VALUES({_user_id}, {_book_id})")
  db.commit()
  input(f"\nBook #{_book_id} added! Press 'Enter' to continue...")


db = mysql.connector.connect(**config)
cursor = db.cursor()
show_menu()
