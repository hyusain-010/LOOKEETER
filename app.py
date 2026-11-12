import sqlite3
import database

from flask import Flask, render_template, request, redirect, session

from email_validator import validate_email, EmailNotValidError

from services.gravatar import gravatar
from services.dnslookup import get_mx

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

app = Flask(__name__)
app.secret_key = "lookeeter_secret"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/admin')
def admin():

    if session.get('user') != 'admin':
        return redirect('/')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users ORDER BY id DESC"
    )
    users = cursor.fetchall()

    cursor.execute(
        "SELECT * FROM searches ORDER BY id DESC"
    )
    searches = cursor.fetchall()

    conn.close()

    return render_template(
        'admin.html',
        users=users,
        searches=searches
    )


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )

            conn.commit()
            conn.close()

            return redirect('/login')

        except sqlite3.IntegrityError:
            return "Username already exists"

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = cursor.fetchone()

        conn.close()

        if user and check_password_hash(user[2], password):
            session['user'] = username
            return redirect('/')

        return "Invalid username or password"

    return render_template('login.html')


@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect('/login')


@app.route('/history')
def history():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM searches
        ORDER BY id DESC
    """)

    searches = cursor.fetchall()

    conn.close()

    return render_template(
        'history.html',
        searches=searches
    )


@app.route('/stats')
def stats():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM searches")
    total_searches = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "stats.html",
        total_users=total_users,
        total_searches=total_searches,
        total=total_searches
    )


@app.route('/search', methods=['POST'])
def search():

    email = request.form['email'].strip()

    try:
        validate_email(email)
        valid = True
    except EmailNotValidError:
        valid = False

    avatar = gravatar(email)

    username_part = email.split("@")[0] if "@" in email else email

    domain = email.split("@")[1] if "@" in email else ""

    try:
        mx_records = get_mx(domain) if domain else []
    except Exception:
        mx_records = []

    gravatar_found = True

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO searches(email) VALUES(?)",
        (email,)
    )

    conn.commit()
    conn.close()

    google_link = (
        f"https://www.google.com/search?q={email}"
    )

    github_link = (
        f"https://github.com/search?q={username_part}"
    )

    linkedin_link = (
        f"https://www.linkedin.com/search/results/all/?keywords={username_part}"
    )

    google_linkedin = (
        f"https://www.google.com/search?q=site:linkedin.com/in+{username_part}"
    )

    return render_template(
        'results.html',
        email=email,
        avatar=avatar,
        valid=valid,
        gravatar_found=gravatar_found,
        mx_records=mx_records,
        google_link=google_link,
        github_link=github_link,
        linkedin_link=linkedin_link,
        google_linkedin=google_linkedin,
        username_part=username_part
    )


if __name__ == '__main__':
    database.init_db()
    app.run(debug=True)