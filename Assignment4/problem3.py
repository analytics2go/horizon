# ----------------------------------------------
# CPSC-442-11/Python  - Assignment 4 Problem 3
# Author:  Wofford, Juana 1014901
#
#
#-------------------------
import os
import csv

# display program menu
def display_menu():
    print('Library Manager Menu')
    print('i.    Add Books')
    print('ii.   Remove Books')
    print('iii.  Add Membership')
    print('iv.   Remove Membership')
    print('v.    Rent Book')
    print('vi.   List Books')
    print('vii.  List Members')
    print('viii. Exit')


# load program information from files
# when program starts
FILENAME = "books.txt"

# use the global constant FILENAME to store the filename of text file

# book information create file that holds books
def write_books(books):
    try:
        with open (FILENAME, 'w') as file:
             for book in books:
                file.write(book + '\n')
    except FileNotFoundError:
        print("Could not find the file named "+ FILENAME)


# create file that holds rented books
def write_rentedbooks(books):
    try:
        with open ("rented_books.txt", 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(books)
    except FileNotFoundError:
        print('Could not find the file named rented)books.txt')

# adds new books, calls the function
# to write the newly added book
def add_books(books):
    book = input('Book Name: ')
    books.append(book)
    write_books(books)
    print(book + ' was added . \n')

# this loads the books
# into the system, if there are no books
# calls the add books function to add
def read_books():
    books = []
    try:
        if not os.path.exists('books.txt'):
            print('No Books are added...please add. ')
            add_books(books)
        elif print(''):
            with open(FILENAME) as file:
                 for line in file:
                     line = line.replace('\n','')
                     books.append(line)
    except FileNotFoundError as e:
        print("FileNotFoundError: ", e)
    return books

# lists the books
def list_books(books):
    for i in range(len(books)):
        book = books[i]
        print(str(i+1) + '. ' + book)
    print()

# deletes the book selected
def delete_books(books):
    list_books(books)
    index = int(input('Enter the number '
                      ' for the book you want to delete:'))
    book = books.pop(index-1)
    write_books(books)
    print(book + ' was deleted. \n')

# rent the book
def rent_book(books):
     list_books(books)
     index = int(input('Select the number of the book '
                      'you want to rent: '))
     book_name = books[index]
     book_rented = 'Rented'
     books.pop(index -1)
     book = []
     book.append(book_name)
     book.append(book_rented)
     write_rentedbooks(books)
     print('Book Rented: ')

# membership information
def create_member():
    member_name = get_membername()
    print(member_name)
    try:
        with open("members.txt","a") as file:
             file.write(member_name+'\n')
    except FileNotFoundError:
        print('Could not find file members.txt')

# gets member name
def get_membername():
    while True:
        name= input('Enter Member Name:   ').strip()
        if '' in name:
            return name
        else:
            print('Please enter Member Name:')

# lists members
def list_members():
    with open("members.txt")as file:
        for line in file:
            print(line, end="")
        print()


# menu main program
def main():
    books = read_books()    # read the books into the system
    display_menu()  #display the menu
    while True:
        select = input("\n Menu: ")
        if select =='i':
            print('Add Books...')
            add_books(books)
        elif select =='ii':
            print('Remove A Book...' )
            delete_books(books)
        elif select =='iii':
            print('Create Membership ')
            create_member()
        elif select=='v':
            print('Rent A Book...')
            rent_book(books)
        elif select =='vi':
            print('List Books...')
            list_books(books)
        elif select =="vii":
            list_members()
            print('List Members...')
        elif select =='viii':
            print('Good Bye....')
            break
        else:
            print('select valid selection, try again')


if __name__ == "__main__":
    main()


