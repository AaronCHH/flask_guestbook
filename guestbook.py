from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return '<h1>Hello There!</h1>'


if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.jinja_env.auto_reload = True
  app.run(debug=True)
