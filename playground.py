from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def start_playground():
    print("start assignment playground")
    print("go to URL add /play")
    return render_template('playground.html', amount = int(1))

@app.route('/play')
def lvl_1():
    print("connected to playground.py")
    return render_template('playground.html', amount=int(3))

@app.route('/play/<int:x>')
def lvl_2(x):
    print("connected to the x of boxes")
    return render_template('playground.html', amount=x)

@app.route('/play/<int:x>/<color>')
def lvl_3(x, color):
    print('changing colors of boxes')
    return render_template('playground.html', amount=x, color = color)

if __name__=="__main__":
    app.run(debug=True)