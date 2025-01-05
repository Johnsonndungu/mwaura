from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Root'
app.config['MYSQL_DB'] = 'items_data'

mysql = MySQL(app)
def index():
    # You can display a list of items here 
    items = items.query.all()
    return render_template('index.html', items=items) 

global cur 
global items
#login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cur.fetchone()
        cur.close()

        if user and user[2] == password: 
            # Successful login
            return render_template('index.html')
        else:
            return "Invalid username or password."

    return render_template('login.html')


#add items
@app.route('/templates/add_item',methods = ['GET','POST'])
def add_items():
    if request.method == 'POST':
        name = request.form['itemName']
        quantity = request.form['itemQuantity']
        price = request.form['itemPrice']
        date = request.form['Date']

        new_item = items(name=name, quantity=quantity, price=price, Date = date)
        cur.session.add(new_item)
        cur.session.commit()

        return redirect(url_for('index')) 

    return render_template('add_items.html') 



if __name__ == '__main__':
    app.run(debug=True)