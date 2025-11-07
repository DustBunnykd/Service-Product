import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from flask_mysqldb import MySQL

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', '#W15w2020#')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'serviceDB')

# Initialize MySQL
mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT Services FROM tbl_service')
    posts = cur.fetchall()  # This returns a list of tuples
    cur.close()

    # Check if any services exist
    if len(posts) > 0:
        return render_template('index.html', posts=posts)
    else:
        return render_template('noservices.html')

@app.route('/submit', methods=['POST'])
def submit():
    new_service = request.form.get('new_service')

    if not new_service or new_service.strip() == "":
        # Ignore empty services
        return redirect(url_for('index'))

    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO tbl_service (Services) VALUES (%s)', [new_service])
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True)
