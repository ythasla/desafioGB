from flask import Flask, Response, request, render_template, url_for
from flask_mysqldb import MySQL
from werkzeug.utils import redirect
import mysql.connector
import json

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
mysql = MySQL(app)


@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM computer")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', computers=data)


@app.route('/salvar', methods=["POST"])
def salvar():
    nome = request.form['nome']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO computer (data) VALUES (%s)", (nome,))
    mysql.connection.commit()
    return redirect(url_for('index'))


@app.route('/update', methods=["POST"])
def update():
    id_data = request.form['id']
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE computer SET data=%s WHERE id=%s", (nome, id_data, cpf, email,))
    mysql.connection.commit()
    return redirect(url_for('index'))


@app.route('/delete/<string:id_data>', methods=["GET"])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM computer WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))
