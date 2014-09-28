import sqlite3, requests
from flask import Flask, request, g, render_template

app = Flask(__name__)
DATABASE = 'books.db'


def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

@app.route('/search')
def search():
	name = request.args.get("name")
	r = requests.get ("https://www.googleapis.com/books/v1/volumes?q=" + name)
	rjson = r.json()
	return render_template("books.html", rjson=rjson)

@app.route('/')
def mypage():
	return app.send_static_file('mypage.html')

@app.route('/template')
def template():
	return render_template("album.html")

@app.route('/album', methods=["POST"])
def album():
    title = request.form['title']
    author = request.form['author']
    date = request.form['date']
    db_add_mybooks(title, author,date)
    books = db_read_books()
    return render_template("album.html", books= books)
	
def db_read_books():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM books")
    return cur.fetchall()

def db_add_mybooks(title, author, date):
	cur = get_db().cursor()
	book_info = (title, author, date)
	cur.execute("INSERT INTO books VALUES (?, ?, ?)", book_info)
	get_db().commit()

if __name__ == '__main__':
	app.run(debug=True)