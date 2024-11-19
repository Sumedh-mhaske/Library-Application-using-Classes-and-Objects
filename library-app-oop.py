# Creating a Library Application using Classes and Objects (Storing data in lists)

import datetime

# Function to get current time
def get_date():
    date = datetime.date.today()
    
    full_date = str(date.day) + '/' + str(date.month) + '/' + str(date.year)
    return full_date

# Initial lists to add the data 
all_books = []
all_student = []
all_issued = []

getStudEnr = lambda : input('Enter Student Enrollment Number : ')
getBookEnr = lambda : input('Enter Book Number : ')

# Student class for student info
class Student():
       pass

# Book class for book info
class Book():
       pass

# Issue class for book issue info
class Issue():
       pass


# Functions to do operations for Library
def issue_book():
        pass

def return_book():
        pass

def view_not_ret():
        pass

def search_stud():
        pass

def search_book():
        pass

def stud_history():
        pass

def book_history():
        pass

def add_new_book():
        pass

def add_new_stud():
        pass


while True:
    input()
    print('Select operation')
    print('1 - Issue Book')
    print('2 - Return Book')
    print('3 - View Not Returned Book')
    print('4 - Search Student')   
    print('5 - Search Book')
    print('6 - Student History')
    print('7 - Book History')
    print('8 - Add New Book')
    print('9 - Add New Student')
    print('0 - Exit')

    ch = int(input('Enter Your Choice : '))

    if ch == 1: issue_book()
    elif ch == 2: return_book()
    elif ch == 3: view_not_ret()
    elif ch == 4: search_stud()
    elif ch == 5: search_book()
    elif ch == 6: stud_history()
    elif ch == 7: book_history()
    elif ch == 8: add_new_book()
    elif ch == 9: add_new_stud()
    elif ch == 0: exit(0)
