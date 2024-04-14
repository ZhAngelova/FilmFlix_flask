from flask import Flask, render_template, url_for, request, redirect, abort
import sqlite3 as sql
 
# this file previous called dbMenu renamed to app.py
# Importing necessary modules
# from reportFilm import *
 
 
app = Flask(__name__)
 
def db_access():
    try: 
        with sql.connect('filmflix.db') as dbCon: 
                    
            dbCon.row_factory = sql.Row
            return dbCon
        
    except sql.OperationalError as e: 
        print(f"Connect failed: {e}")

    

# retrieve film information from a database.
def get_film(film_id):
    conn = db_access()
    film = conn.execute('SELECT * FROM tblFilms WHERE filmID = ?',(film_id,)).fetchone()
    conn.close()
    if film is None:
        abort(404)
    return film 


@app.route('/')
def index():
    conn = db_access() #internal connection to the db page
    films = conn.execute('SELECT * FROM tblFilms').fetchall()
    conn.close()
    return render_template('index.html', title='Home', films=films)
   
    
@app.route('/add_film', methods = ('GET','POST'))
def add():
    if request.method == 'POST':
        film = { 
            "filmID":request.form.get('filmID'),
            "title":request.form['title'],
            "year":request.form['year'],
            "rating":request.form['rating'],
            "duration":request.form['duration'],
            "genre":request.form['genre']
        }
        conn = db_access()
        # conn.execute('INSERT INTO tblFilms VALUES(NULL, ?, ?, ?, ?, ?)', film)
        conn.execute('INSERT INTO tblFilms (filmID, title, yearReleased, rating, duration, genre) VALUES (:filmID, :title, :year, :rating, :duration, :genre)', film)
                
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('add_film.html')


@app.route('/update/<int:film_id>', methods = ('GET', 'POST'))
def update(film_id):
    film = get_film(film_id)
    if request.method == 'POST':
        updated_film = {
            "filmID": film_id,
            "title":request.form.get('title'),
            "year":request.form['year'],
            "rating":request.form['rating'],
            "duration":request.form['duration'],
            "genre":request.form['genre']                     
        }
        conn = db_access()
        conn.execute('UPDATE tblFilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ? WHERE filmID = ?',
            (updated_film['title'], updated_film['year'], updated_film['rating'], updated_film['duration'], updated_film['genre'], updated_film['filmID']))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('update.html', film = film) 


@app.route('/delete/<int:film_id>', methods=('GET', 'POST'))
def delete(film_id):
    if request.method == 'POST':
        conn = db_access()
        conn.execute('DELETE FROM tblFilms WHERE filmID = ?', (film_id,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        # Render a confirmation page for GET request
        return render_template('confirm_delete.html', film_id=film_id)




if __name__ == "__main__":
    app.run(debug=True)




























