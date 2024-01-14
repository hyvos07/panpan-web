from flask import Flask, render_template
from threading import Thread

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

def run():
  app.run(host='0.0.0.0',port=8080)

def run_http():  
    t = Thread(target=run)
    t.start()
    
if __name__ == "__main__":
    run_http()