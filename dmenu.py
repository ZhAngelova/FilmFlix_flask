# Import all CRUD modules
import readFilms, addFilm, updateFilm, deleteFilm, reportFilm

#read the main menu from txt file
def read_file(file_path):
    try:
        with open(file_path) as open_file:
            # read() reads the file content and save it in the variable called rf
            rf = open_file.read()
 
            return rf
    except FileNotFoundError as nf:
        print(f"File not found: {nf}")
   
    except FileExistsError as ne:
        print(f"File not exists: {ne}")

#print(read_file("PythonWorkingFiles/FilmFlix Project/dbMenu.txt")) just check!


# add try - except?!
def report_menu():
    try:    
        report_options = """
        1. Print details of all films.
        2. Print all films of a particular year of release.
        3. Print all films of a particular rating.
        4. Print all films of a particular genre.
        5. Exit the Report menu.
        """

        report_option = 0
        report_options_list = ["1", "2", "3", "4", "5"]
            
        while report_option not in report_options_list:
            print(report_options)
            report_option = input("Enter an option from Report menu above: ")
            
            if report_option not in report_options_list:
                print(f"{report_option} is not a valid choice")
            else:
                return report_option
    except ValueError:
        print("Please enter a valid integer choice.")

def films_menu():
    try:
        filmOption = 0 #initialise the option variable wih the integer value 0
        optionsList = ["1","2","3","4","5"] #create a list data structure with string values 
        menu_choices = read_file("dbMenu.txt")
        
        while filmOption not in optionsList:
            print(menu_choices) 

            filmOption = input("Select an option from Main menu: ") 

            if filmOption not in optionsList:
                print(f"{filmOption} is not a valid choice")

        return filmOption
    
    except FileNotFoundError as e:
        print(f"Add error: {e}")  

main_program = True              

while main_program:
    main_menu = films_menu()
    
    if main_menu == "1":
        addFilm.insert_record()
    elif main_menu == "2":
        deleteFilm.delete_film()
    elif main_menu == "3":
        updateFilm.update_film_record()
    elif main_menu == "4":
        report_option = report_menu()
        if report_option == "1":
            readFilms.read_films()
        elif report_option == "2":
            reportFilm.search_by_year()
        elif report_option == "3":
            reportFilm.search_by_rating()
        elif report_option == "4":
            reportFilm.search_by_genre()
        elif report_option == "5":
            continue  # Go back to the main menu
    else:
        main_program = False

input("Press Enter to exit....")


