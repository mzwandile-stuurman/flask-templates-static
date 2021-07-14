from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template('homepage.html', name=name)

@app.route('/loops/<int:number>')

def times(number):
    return render_template('times.html',number=number)

if __name__ =='__main__':
    app.debug= True
    app.run()
