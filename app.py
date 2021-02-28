from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guestbook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def index():
  result = model.Comments.query.all()
  return render_template('index.html', result=result)


@app.route('/sign')
def sign():
  return render_template('sign.html')


@app.route('/process', methods=['POST'])
def process():
  name = request.form['name']
  comment = request.form['comment']
  signature = model.Comments(name=name, comment=comment)
  db.session.add(signature)
  db.session.commit()

  return redirect(url_for('index'))


@app.route('/home', methods=['GET', 'POST'])
def home():
  links = [
      'https://www.youtube.com', 'https://www.bing.com',
      'https://www.python.org', 'https://www.enkato.com'
  ]
  return render_template('example.html', links=links)


if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.jinja_env.auto_reload = True
  app.run(debug=True)
