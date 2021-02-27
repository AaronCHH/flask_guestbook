from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return '<h1>Hello There!</h1>'


@app.route('/home', methods=['GET', 'POST'])
def home():
  return '<h1>You are on the home page!</h1>'


if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.jinja_env.auto_reload = True
  app.run(debug=True)
