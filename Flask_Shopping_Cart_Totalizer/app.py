from flask import Flask, render_template, request

app = Flask(__name__)

class ShoppingCart:
    def total_price(self, *prices):
        return sum(prices)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/total', methods=['POST'])
def total():
    prices = request.form.getlist('price')
    prices = [float(p) for p in prices if p.strip() != '']
    cart = ShoppingCart()
    total = cart.total_price(*prices)
    return render_template('result.html', total=total, prices=prices)

if __name__ == '__main__':
    app.run(debug=True)
