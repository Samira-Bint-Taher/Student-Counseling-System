from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(_name_)
app.secret_key = "flash message"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'studentcrud'

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', student=data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        universityemail = request.form['universityemail']
        phone = request.form['phone']
        counsellingtopic = request.form['counsellingtopic']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student (name,university email,phone,counselling topic) VALUES (%s, %s, %s)",
                    (name, universityemail, phone, counsellingtopic))
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/base')
def student():
    return render_template('base.html')


if _name_ == "_main_":
    app.run(debug=True)

