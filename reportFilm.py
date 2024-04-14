from connect import * 

def search_by_year():
    try:
        _, dbCursor = db_access()
        year_released = input("Enter the year released: ")
        dbCursor.execute("SELECT * FROM tblFilms WHERE yearReleased = ?", (year_released,))
        rows = dbCursor.fetchall()
        if not rows:
            print("No records found.")
        else:
            for record in rows:
                print(record)
    except sql.ProgrammingError as e:
        print(f"Search error: {e}")



def search_by_rating():
    try:
        _, dbCursor = db_access()
        rating = input("Enter the film rating: ").lower()
        dbCursor.execute("SELECT * FROM tblFilms WHERE LOWER(rating) = ?", (rating,))
        rows = dbCursor.fetchall()
        if not rows:
            print("No records found.")
        else:
            for record in rows:
                print(record)
    except sql.ProgrammingError as e:
        print(f"Search error: {e}")



def search_by_genre():
    try:
        _, dbCursor = db_access()
        genre = input("Enter the genre: ").lower()
        dbCursor.execute("SELECT * FROM tblFilms WHERE LOWER(genre) = ?", (genre,))
        rows = dbCursor.fetchall()
        if not rows:
            print("No records found.")
        else:
            for record in rows:
                print(record)
    except sql.ProgrammingError as e:
        print(f"Search error: {e}")


#search_by_year()
# search_by_rating()
# search_by_genre()

if __name__ == "__main__":
    search_by_year()

if __name__ == "__main__":
    search_by_rating()

if __name__ == "__main__":
    search_by_genre()


