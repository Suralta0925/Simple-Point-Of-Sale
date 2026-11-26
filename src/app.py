from flask import Flask, render_template, url_for

from database import Database
from repository import UserRepo

db = Database()
with db.transaction() as conn:
    repo = UserRepo(conn, db)
    print(repo.readAll())



# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)