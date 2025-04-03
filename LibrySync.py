# My log for LMS
print('''
 __       __  .______   .______       __       _______.____    ____ .__   __.   ______ 
|  |     |  | |   _  \  |   _  \     |  |     /       |\   \  /   / |  \ |  |  /      |
|  |     |  | |  |_)  | |  |_)  |    |  |    |   (----` \   \/   /  |   \|  | |  ,----'
|  |     |  | |   _  <  |      /     |  |     \   \      \_    _/   |  . `  | |  |     
|  `----.|  | |  |_)  | |  |\  \----.|  | .----)   |       |  |     |  |\   | |  `----.
|_______||__| |______/  | _| `._____||__| |_______/        |__|     |__| \__|  \______|
                                                                                                             
''')








# Gettings Inputs user name
name_start = input("Please Enter Your Name to Get Started : ")
print("Hello, ", name_start)

# All storage location for resources
booklist = [
 {'ISBN': 1001, 'title': 'The Origin of Species', 'format': 'Hardcover', 'subject': 'Science', 'rental_price': 550.0,
     'num_copies': 0},
{'ISBN': 1002, 'title': 'The Great Gatsby', 'format': 'Paperback', 'subject': 'Literature', 'rental_price': 450.0,
     'num_copies': 50},
    {'ISBN': 1003, 'title': 'A Brief History of Time', 'format': 'Hardcover', 'subject': 'Science',
     'rental_price': 600.0, 'num_copies': 90}]

magazineList = [
    {'magazine_number': 1004, 'title': 'Scientific American', 'print_format': 'Color', 'subject': 'Science',
                 'rental_price': 230.0, 'num_copies': 75},
            {'magazine_number': 1005, 'title': 'Wired', 'print_format': 'Black & White', 'subject': 'Technology',
                 'rental_price': 250.0, 'num_copies': 85},
            {'magazine_number': 1006, 'title': 'Sports Illustrated', 'print_format': 'Color', 'subject': 'Sports',
                 'rental_price': 200.0, 'num_copies': 0}]

dvdList = [
    {'dvd_number': 1007, 'title': 'The Martian', 'subject': 'Astronomy', 'rental_price': 100.0, 'num_copies': 80},
    {'dvd_number': 1008, 'title': 'The Imitation Game', 'subject': 'Technology', 'rental_price': 120.0,
     'num_copies': 70},
    {'dvd_number': 1009, 'title': 'Hidden Figures', 'subject': 'Math', 'rental_price': 110.0, 'num_copies': 0}]

cdList = [{'cd_number': 1010, 'title': 'Mozart: Piano Concerto No. 21', 'category': 'Music', 'rental_price': 50.0,
           'num_copies': 40},
    {'cd_number': 1011, 'title': 'Rosetta Stone: Spanish', 'category': 'Foreign Languages', 'rental_price': 70.0,
           'num_copies': 30},
    {'cd_number': 1012, 'title': 'Calculus Made Easy', 'category': 'Math', 'rental_price': 80.0, 'num_copies': 40}]


# ALL Functions -----------------------------------------------------------------------------
# operation Menu for books
def operateBook():
    print('''

        1 - Add a new book
        2 - Remove a book
        3 - View available books
        4 - View unavailable books
        5 - View books by subject
        6 - Lend a book
        7 - Update books
        0 - Exit
        ''')


# operation Menu for Magazine
def operateMagazine():
    print('''

        1 - Add a new magazine
        2 - Remove a magazine
        3 - View available magazines
        4 - View unavailable magazines
        5 - View magazines by subject
        6 - Lend a magazine
        7 - Update magazine
        0 - Exit
        ''')


# operation Menu for Educational DVDs
def operateDVD():
    print('''

        1 - Add a new Educational DVD
        2 - Remove a DVD
        3 - View available Educational DVDs
        4 - View unavailable DVDs
        5 - View Educational DVDs by subject
        6 - Lend a DVD
        7 - Update DVD
        0 - Exit
        ''')


# operation Menu for CDs
def operateCD():
    print('''

        1 - Add a new Lecture CD
        2 - Remove a CD
        3 - View available Lecture CDs
        4 - View unavailable Lecture CD
        5 - View Lecture CDs by subject
        6 - Lend a CD
        7 - Update CD
        0 - Exit
        ''')


# Welcome screen and main menu
def MainMenu():
    print('''        
        ---------------
        Main Categories:
        ---------------

        1 Book
        2 Magazine
        3 Educational DVD
        4 Lecture CD
        5 View All Resources
        0 Exit

        ---------------
        '''
          )


# function for animated exiting programme
import time
def ex_programme():
    print("\nExiting program", end="")
    for i in range(10):
        time.sleep(0.2)
        print(".", end="", flush=True)
    print("!")
    print('''\nThank you for using My Library Management System. \nI hope you have a great day! ≧◠‿◠≦✌ ''')
    exit()


# function for view all resource by subject
def filter_sub():
    print("\nAll Books:")
    for book in booklist:
        print(book)
    print("\nAll Magazines:")
    for magazine in magazineList:
        print(magazine)
    print("\nAll Educational DVDs:")
    for dvd in dvdList:
        print(dvd)
    print("\nAll Lecture CDs:")
    for cd in cdList:
        print(cd)


# All functions ending area --------------------------------------------------------------------


# Input for welcome menu
print("\nWelcome to My Library Management System!")
MainMenu()
UserInput = int(input("Please choose an option: "))

# Book Part -------------------------------------------------------------------------------------------------------
while True:
    if (UserInput == 1):
        while True:
            operateBook()
            UserInput2 = int(input("Select your choice: "))
            if (UserInput2 == 1):
                if (UserInput2 == 1):
                    # adding a new book
                    isbn = int(input("Enter the ISBN number: "))
                    title = input("Enter the title: ")
                    print("Select the book format:")
                    print("1. Hardcover")
                    print("2. Paperback")
                    while True:
                        format_choice = int(input("Enter your choice: "))
                        if format_choice == 1:
                            format = "Hardcover"
                            break
                        elif format_choice == 2:
                            format = "Paperback"
                            break
                        else:
                            print("Invalid choice.")
                            format = ""
                    print("Select the book subject:")
                    print("1. Science")
                    print("2. History")
                    print("3. Literature")
                    while True:
                        subject_choice = int(input("Enter your choice: "))
                        if subject_choice == 1:
                            subject = "Science"
                            break
                        elif subject_choice == 2:
                            subject = "History"
                            break
                        elif subject_choice == 3:
                            subject = "Literature"
                            break
                        else:
                            print("Invalid choice.")
                            subject = ""
                            break
                    rental_price = float(input("Enter the rental price per day in Rs. "))
                    num_copies = int(input("Enter the number of copies: "))
                    book = {"ISBN": isbn, "title": title, "format": format, "subject": subject,
                            "rental_price": rental_price, "num_copies": num_copies}
                    print("\nBook added successfully.")
                    booklist.append(book)
                    print(book)


            elif (UserInput2 == 2):
                print("\nNow Available Books :\n")
                for book in booklist:
                    print(book)
                isbn = int(input("Enter the ISBN number of the book you want to remove: "))
                for book in booklist:
                    if book["ISBN"] == isbn:
                        booklist.remove(book)
                        print("Book removed successfully.")
                        break
                else:
                    print("Book not found in the list.")


            elif (UserInput2 == 3):
                # view available books
                print("Available Books:\n")
                for book in booklist:
                    if book["num_copies"] > 0:
                        print(book)


            elif (UserInput2 == 4):
                # view unavailable books
                print("Unavailable Books:\n")
                for book in booklist:
                    if book["num_copies"] == 0:
                        print(book)
                        break
                else:
                    print("Not unavailable book!")

            elif (UserInput2 == 5):
                # view all books or filter by subject
                print("Select a subject to filter by:\n")
                print("1. Science")
                print("2. History")
                print("3. Literature")
                print("4. Show all books")

                subject_choice = int(input("Enter your choice: "))
                if subject_choice == 1:
                    subject = "Science"
                elif subject_choice == 2:
                    subject = "History"
                elif subject_choice == 3:
                    subject = "Literature"
                elif subject_choice == 4:
                    subject = ""
                else:
                    print("Invalid choice.")
                    break

                print("Books filtered by subject:\n")
                for book in booklist:
                    if book["num_copies"] > 0:
                        if subject == "" or book["subject"] == subject:
                            print(book)


            elif (UserInput2 == 6):
                # lend a book
                isbn = int(input("Enter the ISBN number of the book you want to lend: "))
                for book in booklist:
                    if book["ISBN"] == isbn:
                        if book["num_copies"] > 0:
                            book["num_copies"] -= 1
                            print("Book lent successfully.")
                        else:
                            print("Book not available for lending.")
                        break
                else:
                    print("Book not found.")

            elif (UserInput2 == 7):
                # update book information
                isbn = int(input("Enter the ISBN number of the book you want to update: "))
                for book in booklist:
                    if book["ISBN"] == isbn:
                        print("1 - Update rental price")
                        print("2 - Update number of copies")
                        choice = int(input("Enter your choice: "))
                        if choice == 1:
                            new_rental_price = float(input("Enter the new rental price per day in Rs.: "))
                            book["rental_price"] = new_rental_price
                            print("Rental price updated successfully.")
                        elif choice == 2:
                            new_num_copies = int(input("Enter the new number of copies: "))
                            book["num_copies"] = new_num_copies
                            print("Number of copies updated successfully.")
                        else:
                            print("Invalid choice.")
                        break
                else:
                    print("Book not found.")

            elif (UserInput2 == 0):
                ex_programme()
                break

            else:
                print("\nInvalid choice. Please try again.")
                MainMenu()
                UserInput = int(input("Please choose an option: "))


    # Magazine Part ---------------------------------------------------------------------------------------------------
    elif (UserInput == 2):
        while True:
            operateMagazine()
            UserInput2 = int(input("Select your choice: "))
            if UserInput2 == 1:
                # adding a new magazine
                magazine_number = int(input("Enter the magazine number: "))
                title = input("Enter the title: ")
                print("Select the magazine print format:")
                print("1. Color")
                print("2. Black & White")
                while True:
                    format_mag = int(input("Enter your choice: "))
                    if format_mag == 1:
                        formatmag = "Color"
                        break
                    elif format_mag == 2:
                        formatmag = "Black & White"
                        break
                    else:
                        print("Invalid choice.")
                        formatmag = ""

                print("Select the magazine subject:")
                print("1. Science")
                print("2. Technology")
                print("3. Sports")
                while True:
                    subject_choice = int(input("Enter your choice: "))
                    if subject_choice == 1:
                        subject = "Science"
                        break
                    elif subject_choice == 2:
                        subject = "Technology"
                        break
                    elif subject_choice == 3:
                        subject = "Sports"
                        break
                    else:
                        print("Invalid choice.")
                        subject = ""

                rental_price = float(input("Enter the rental price per day in Rs. "))
                num_copies = int(input("Enter the number of copies: "))

                magazine = {
                    "magazine_number": magazine_number,
                    "title": title,
                    "print_format": formatmag,
                    "subject": subject,
                    "rental_price": rental_price,
                    "num_copies": num_copies
                }

                print("\nMagazine added successfully.")
                magazineList.append(magazine)
                print(magazine)


            elif UserInput2 == 2:
                # remove magazines
                print("\nNow Available Magazines :\n")
                for magazine in magazineList:
                    print(magazineList)
                    break
                magazine_number = int(input("Enter the magazine number of the magazine you want to remove: "))
                for magazine in magazineList:
                    if magazine["magazine_number"] == magazine_number:
                        magazineList.remove(magazine)
                        print("Magazine removed successfully.")
                        break
                else:
                    print("Magazine not found in the list.")

            elif UserInput2 == 3:
                # view available magazines
                print("Available Magazines:\n")
                for magazine in magazineList:
                    if magazine["num_copies"] > 0:
                        print(magazine)

            elif UserInput2 == 4:
                # view unavailable magazines
                print("Unavailable Magazines:\n")
                for magazine in magazineList:
                    if magazine["num_copies"] == 0:
                        print(magazine)
                        break
                else:
                    print("Not unavailable magazine!")

            elif UserInput2 == 5:
                    # view all magazines or filter by subject
                    print("Select a subject to filter by:\n")
                    print("1. Science")
                    print("2. Technology")
                    print("3. Sports")
                    print("4. Show all magazines")
                    subject_choice = int(input("Enter your choice: "))

                    if subject_choice == 1:
                        subject = "Science"
                    elif subject_choice == 2:
                        subject = "Technology"
                    elif subject_choice == 3:
                        subject = "Sports"
                    elif subject_choice == 4:
                        subject = ""
                    else:
                        print("Invalid choice.")
                        break

                    print("Magazines filtered by subject:")
                    for magazine in magazineList:
                        if magazine["num_copies"] > 0:
                            if subject == "" or magazine["subject"] == subject:
                                print(magazine)


            elif UserInput2 == 6:
                # lend a magazine
                magazine_number = int(input("Enter the magazine number you want to lend: "))
                for magazine in magazineList:
                    if magazine["magazine_number"] == magazine_number:
                        if magazine["num_copies"] > 0:
                            magazine["num_copies"] -= 1
                            print("Magazine lent successfully.")
                        else:
                            print("Magazine not available for lending.")
                        break
                else:
                    print("Magazine not found.")

            elif UserInput2 == 7:
                # update magazine information
                magazine_number = int(input("Enter the magazine number of the magazine you want to update: "))
                for magazine in magazineList:
                    if magazine["magazine_number"] == magazine_number:
                        print("1 - Update rental price")
                        print("2 - Update number of copies")
                        choice = int(input("Enter your choice: "))
                        if choice == 1:
                            new_rental_price = float(input("Enter the new rental price per day in Rs.: "))
                            magazine["rental_price"] = new_rental_price

                        elif choice == 2:
                            new_num_copies = int(input("Enter the new number of copies: "))
                            magazine["num_copies"] = new_num_copies
                            print("Number of copies updated successfully.")
                        else:
                            print("Invalid choice.")
                        break
                else:
                    print("Magazine not found.")


            elif (UserInput2 == 0):
                ex_programme()

            else:
                print("Invalid choice. Please try again.\n")
                MainMenu()
                UserInput = int(input("Please choose an option: "))


    # Educational DVD Part ------------------------------------------------------------------------------------------
    elif (UserInput == 3):
        while True:
            operateDVD()
            UserInput2 = int(input("Select your choice: "))
            if UserInput2 == 1:
                # adding a new Educational DVD
                dvd_number = int(input("Enter the DVD number: "))
                title = input("Enter the title: ")
                print("Select the DVD subject:")
                print("1. Astronomy")
                print("2. Math")
                print("3. Technology")
                while True:
                    subject_choice = int(input("Enter your choice: "))
                    if subject_choice == 1:
                        subject = "Astronomy"
                        break
                    elif subject_choice == 2:
                        subject = "Math"
                        break
                    elif subject_choice == 3:
                        subject = "Technology"
                        break
                    else:
                        print("Invalid choice.")
                        subject = ""
                rental_price = float(input("Enter the rental price per day in Rs. "))
                num_copies = int(input("Enter the number of copies: "))
                dvd = {"dvd_number": dvd_number, "title": title, "subject": subject, "rental_price": rental_price,
                       "num_copies": num_copies}
                print("\nEducational DVD added successfully.")
                dvdList.append(dvd)
                print(dvd)


            elif UserInput2 == 2:
                # remove dvd
                print("\nNow Available DVDs :\n")
                for dvd in dvdList:
                    print(dvdList)
                    break
                dvd_number = int(input("Enter the DVD number of the Educational DVD you want to remove: "))
                for dvd in dvdList:
                    if dvd["dvd_number"] == dvd_number:
                        dvdList.remove(dvd)
                        print("Educational DVD removed successfully.")
                        break
                else:
                    print("Educational DVD not found in the list.")

            elif UserInput2 == 3:
                # view available Educational DVDs
                print("Available Educational DVDs:")
                for dvd in dvdList:
                    if dvd["num_copies"] > 0:
                        print(dvd)

            elif UserInput2 == 4:
                # view unavailable Educational DVDs
                print("Unavailable Educational DVDs:\n")
                for dvd in dvdList:
                    if dvd["num_copies"] == 0:
                        print(dvd)
                        break
                else:
                    print("Not unavailable Educational DVD!")

            elif UserInput2 == 5:
                    # view all DVDs or filter by subject
                    print("Select a subject to filter by:")
                    print("1. Astronomy")
                    print("2. Technology")
                    print("3. Math")
                    print("4. Show all DVDs")
                    subject_choice = int(input("Enter your choice: "))

                    if subject_choice == 1:
                        subject = "Astronomy"
                    elif subject_choice == 2:
                        subject = "Technology"
                    elif subject_choice == 3:
                        subject = "Math"
                    elif subject_choice == 4:
                        subject = ""
                    else:
                        print("Invalid choice.")
                        break

                    print("DVDs filtered by subject:\n")
                    for dvd in dvdList:
                        if dvd["num_copies"] > 0:
                            if subject == "" or dvd["subject"] == subject:
                                print(dvd)


            elif UserInput2 == 6:
                # lend an Educational DVD
                dvd_number = int(input("Enter the DVD number you want to lend: "))
                for dvd in dvdList:
                    if dvd["dvd_number"] == dvd_number:
                        if dvd["num_copies"] > 0:
                            dvd["num_copies"] -= 1
                            print("Educational DVD lent successfully.")
                        else:
                            print("Educational DVD not available for lending.")
                        break
                else:
                    print("Educational DVD not found.")

            elif UserInput2 == 7:
                # update Educational DVD information
                dvd_number = int(input("Enter the DVD number of the Educational DVD you want to update: "))
                for dvd in dvdList:
                    if dvd["dvd_number"] == dvd_number:
                        print("1 - Update rental price")
                        print("2 - Update number of copies")
                        choice = int(input("Enter your choice: "))
                        if choice == 1:
                            new_rental_price = float(input("Enter the new rental price per day in Rs.: "))
                            dvd["rental_price"] = new_rental_price

                        elif choice == 2:
                            new_num_copies = int(input("Enter the new number of copies: "))
                            dvd["num_copies"] = new_num_copies
                            print("Number of copies updated successfully.")
                    else:
                        print("Invalid choice.")
                    break
                else:
                    print("Educational DVD not found.")


            elif (UserInput2 == 0):
                ex_programme()

            else:
                print("Invalid choice. Please try again.\n")
                MainMenu()
                UserInput = int(input("Please choose an option: "))


    # Lecture CD Part ------------------------------------------------------------------------------------------------
    elif (UserInput == 4):
        while True:
            operateCD()
            UserInput2 = int(input("Select your choice: "))
            if UserInput2 == 1:
                # add a new Lecture CD
                cd_number = int(input("Enter the CD number: "))
                title = input("Enter the title: ")
                print("Select the Lecture CD Subject:")
                print("1. Music")
                print("2. Maths")
                print("3. Foreign Languages")
                while True:
                    category_choice = int(input("Enter your choice: "))
                    if category_choice == 1:
                        category = "Music"
                        break
                    elif category_choice == 2:
                        category = "Maths"
                        break
                    elif category_choice == 3:
                        category = "Foreign Languages"
                        break
                    else:
                        print("Invalid choice.")
                        category = ""
                rental_price = float(input("Enter the rental price per day in Rs. "))
                num_copies = int(input("Enter the number of copies: "))
                cd = {"cd_number": cd_number, "title": title, "category": category,
                      "rental_price": rental_price, "num_copies": num_copies}
                print("\nLecture CD added successfully.")
                cdList.append(cd)
                print(cd)


            elif UserInput2 == 2:
                print("\nNow Available CDs :\n")
                for cd in cdList:
                    print(cdList)
                    break
                cd_number = int(input("Enter the CD number of the Lecture CD you want to remove: "))
                for cd in cdList:
                    if cd["cd_number"] == cd_number:
                        cdList.remove(cd)
                        print("Lecture CD removed successfully.")
                        break
                else:
                    print("Lecture CD not found in the list.")

            elif UserInput2 == 3:
                # Function to view available Lecture CDs
                print("Available Lecture CDs:")
                for cd in cdList:
                    if cd["num_copies"] > 0:
                        print(cd)

            elif UserInput2 == 4:
                # view unavailable Lecture CDs
                print("Unavailable Lecture CDs:\n")
                for cd in cdList:
                    if cd["num_copies"] == 0:
                        print(cd)
                        break
                else:
                    print("Not unavailable Lecture CD!")

            elif UserInput2 == 5:
                    # view all CDs or filter by category
                    print("Select a category to filter by:\n")
                    print("1. Music")
                    print("2. Foreign Languages")
                    print("3. Math")
                    print("4. Show all CDs")
                    category_choice = int(input("Enter your choice: "))

                    if category_choice == 1:
                        category = "Music"
                    elif category_choice == 2:
                        category = "Foreign Languages"
                    elif category_choice == 3:
                        category = "Math"
                    elif category_choice == 4:
                        category = ""
                    else:
                        print("Invalid choice.")
                        break

                    print("CDs filtered by category:\n")
                    for cd in cdList:
                        if cd["num_copies"] > 0:
                            if category == "" or cd["category"] == category:
                                print(cd)

            elif UserInput2 == 6:
                # lend a Lecture CD
                cd_number = int(input("Enter the CD number you want to lend: "))
                for cd in cdList:
                    if cd["cd_number"] == cd_number:
                        if cd["num_copies"] > 0:
                            cd["num_copies"] -= 1
                            print("Lecture CD lent successfully.")
                        else:
                            print("Lecture CD not available for lending.")
                        break
                else:
                    print("Lecture CD not found.")

            elif UserInput2 == 7:
                # update Lecture CD information
                cd_number = int(input("Enter the CD number of the Lecture CD you want to update: "))
                for cd in cdList:
                    if cd["cd_number"] == cd_number:
                        print("1 - Update rental price")
                        print("2 - Update number of copies")
                        choice = int(input("Enter your choice: "))
                        if choice == 1:
                            new_rental_price = float(input("Enter the new rental price per day in Rs.: "))
                            cd["rental_price"] = new_rental_price
                            print("Rental price updated successfully.")

                        elif choice == 2:
                            new_num_copies = int(input("Enter the new number of copies: "))
                            cd["num_copies"] = new_num_copies
                            print("Number of copies updated successfully.")
                        else:
                            print("Invalid choice.")
                        break
                    else:
                        print("Lecture CD not found.")

            elif (UserInput2 == 0):
                ex_programme()

            else:
                print("Invalid choice. Please try again.")
                MainMenu()
                UserInput = int(input("Please choose an option: "))



    # Filtering by Subject --------------------------------------------------------------------------------------------
    elif (UserInput == 5):
        filter_sub()
        MainMenu()
        UserInput = int(input("Please choose an option: "))


    # Exit Part ------------------------------------------------------------------------------------------------------
    elif (UserInput == 0):
        ex_programme()


    else:
        print("Invalid choice. Please try again.")
        MainMenu()
        UserInput = int(input("Please choose an option: "))
