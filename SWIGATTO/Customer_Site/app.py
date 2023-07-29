import mysql.connector as connection
from flask import Flask, render_template, redirect, request
from datetime import datetime


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
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('signin.html')

# Registration form value stored in mysql database
@app.route('/sighnup', methods=['POST'])
def signup():
    email = request.form.get('email')
    name = request.form.get('name')
    Passward = request.form.get('pass')
    Phone_No = request.form.get('phone')
    cur.execute("use food_ordering_data")
    query = " INSERT INTO registration values(%s, %s, %s, %s)"
    val4 = [(email, name, Passward, Phone_No)]
    cur.executemany(query, val4)
    conn.commit()
    message2="Your Registration is completed Please Login from here"
    return render_template('signin.html', message3=message2)

# Login form authentication or validation
@app.route('/sign_in', methods=['POST'])
def signin():
    email = request.form['sign_email']
    passward = request.form['sign_pass']

    # Check if the email and password are valid
    cursor = conn.cursor()
    cur.execute("use food_ordering_data")
    cursor.execute('SELECT * FROM registration WHERE email = %s AND Passward = %s', (email, passward))
    data = cursor.fetchone()
    cursor.close()
    message4="It seems that you are not register, Please first register here then try for login"

    if data:
        return render_template('zogo.html')
    else:
        return render_template('register.html', message3=message4)


@app.route('/forgot_pass')
def forgot():
    message6='Reset your password'
    return render_template('register.html', message7=message6)


@app.route('/register')
def registration():
    message8='Register Here'
    return render_template('register.html', message7=message8)

@app.route('/member')
def member():
    return render_template("signin.html")

# logo link
@app.route('/home_1')
def homme_1():
     return render_template('index.html')

@app.route('/order')
def order():
    return render_template("zogo.html")

@app.route('/demo')
def demo():
        return render_template("register.html")

@app.route('/cart')
def cart():
    return render_template('cart.html')

cart=[]
price=[]
# total=sum(price)
@app.route('/Barbeque')
def barbeque():
    cart.append('barbeque')
    price.append(200)
    return render_template("cart.html", cart1=cart, price1=price, total1=sum(price))

@app.route('/Burgers')
def burger():
        cart.append('burgers')
        price.append(300)
        return render_template("cart.html", cart1=cart, price1=price, total1=sum(price))


@app.route('/Sandwiches')
def sandwiches():
        cart.append('sandwiches')
        price.append(150)
        return render_template("cart.html", cart1=cart, price1=price, total1=sum(price))


@app.route('/Breweries')
def breweries():
       cart.append('breweries')
       price.append(150)
       return render_template("cart.html", cart1=cart, price1=price, total1=sum(price))

@app.route('/Seafood')
def Seafood():
       cart.append('Seafood')
       price.append(150)
       return render_template("cart.html", cart1=cart, price1=price, total1=sum(price))

@app.route('/popup')
def popup():
       cart.append('popup')
       price.append(150)
       return render_template("cart.html", cart1=cart, price1=price, total1=sum(price))

@app.route('/Tex-Mex')
def TexMex():
       cart.append('TexMex')
       price.append(150)
       return render_template("cart.html", cart1=cart, price1=price, total1=sum(price))

@app.route('/Brunch')
def Brunch():
       cart.append('Brunch')
       price.append(150)
       return render_template("cart.html", cart1=cart, price1=price, total1=sum(price))

@app.route('/coffee')
def coffee():
       cart.append('coffee')
       price.append(150)
       return render_template("cart.html", cart1=cart, price1=price, total1=sum(price))

@app.route('/Italian')
def Italian():
       cart.append('Italian')
       price.append(150)
       return render_template("cart.html", cart1=cart, price1=price, total1=sum(price))

@app.route('/American')
def American():
       cart.append('American')
       price.append(150)
       return render_template("cart.html", cart1=cart, price1=price, total1=sum(price))

@app.route('/pizza')
def pizza():
       cart.append('pizza')
       price.append(150)
       return render_template("cart.html", cart1=cart, price1=price, total1=sum(price))

@app.route('/Bakeries')
def bakeries():
       cart.append('bakeries')
       price.append(150)
       return render_template("cart.html", cart1=cart, price1=price, total1=sum(price))


@app.route('/order_now')
def order_now():
    
    # Get the current time
    now = datetime.now()
    time = str(now.strftime("%H:%M:%S"))

    for j in range(0,len(cart)):
            cur.execute("use food_ordering_data")
            query3 = " INSERT INTO food_price values(%s, %s)"
            price_1=str(price[j])
            val2 = [(price_1, time)]
            cur.executemany(query3, val2) 
    conn.commit()

    for i in range(0,len(cart)):
            cur.execute("use food_ordering_data")
            query2 = " INSERT INTO food_order values(%s, %s)"
            food=cart[i]
            val = [(food, time)]
            cur.executemany(query2, val)
    conn.commit()

    message1="Enter your address for ordering"
    return render_template("cart.html", message=message1)



@app.route('/address',methods=['POST'])
def address():
    name = request.form.get('name')
    mobile = str(request.form.get('mobile'))
    Flat = request.form.get('Flat')
    City = request.form.get('city')
    state = request.form.get('state')
    zipcode = request.form.get('zip')
    cur.execute("use food_ordering_data")
    query = " INSERT INTO address values(%s, %s, %s, %s,%s, %s)"
    val4 = [(name, mobile, Flat, City, state, zipcode)]
    cur.executemany(query, val4)
    conn.commit()
    return "Your Order will be delevered in few minutes"

if __name__ == '__main__':
    app.run(debug=True)
