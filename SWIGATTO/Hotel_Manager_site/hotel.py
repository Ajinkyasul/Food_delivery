import mysql.connector as connection
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

conn = connection.connect(
    host='localhost',
    user='root',
    password='Ajinkya@605',
    database='food_ordering_data',
    use_pure=True
)
cur = conn.cursor()

@app.route('/')
def home():
    
    cursor = conn.cursor()
    cur.execute("use food_ordering_data")
    cursor.execute('SELECT * FROM food_order order by placed DESC LIMIT 3')
    data = cursor.fetchall()

    
    return render_template('manager.html', order=data)
    # return items

    
if __name__ == '__main__':
    app.run(debug=True)