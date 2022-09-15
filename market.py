from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/market')
def market():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '938', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '788', 'price': 800},
        {'id': 3, 'name': 'PC', 'barcode': '234', 'price': 1200},
    ]

    return render_template('market.html', items=items)


# if __name__ == '__main__':
#     app.run(debug=True)
