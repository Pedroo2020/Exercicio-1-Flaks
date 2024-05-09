from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/numerospares', methods=['POST'])
def numerospares():
    resultado = ''
    x = 0
    while x < 101:
        if x % 2 == 0:
            resultado += str(x)+'<br>'
        x += 1

        if x > 100:
            resultado += 'Acabou'
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)