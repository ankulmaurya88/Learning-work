from flask import Flask, render_template, request

app = Flask(__name__)

class Greeter:
    def greet(self, name, time="Hello", emoji="😊"):
        return f"{time}, {name}! {emoji}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet_user():
    name = request.form['name']
    time = request.form['time']
    emoji = request.form['emoji']

    greeter = Greeter()

    # Simulate method overloading by checking inputs
    if time == "" and emoji == "":
        greeting = greeter.greet(name)
    elif emoji == "":
        greeting = greeter.greet(name, time)
    else:
        greeting = greeter.greet(name, time, emoji)

    return render_template('result.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)

