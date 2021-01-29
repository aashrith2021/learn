from flask import *

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('calci.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'add':
            result = float(num1) + float(num2)
            return render_template('calci.html', result=result)

        elif operation == 'subtract':
            result = float(num1) - float(num2)
            return render_template('calci.html', result=result)

        elif operation == 'multiply':
            result = float(num1) * float(num2)
            return render_template('calci.html', result=result)

        elif operation == 'divide':
            result = float(num1) / float(num2)
            return render_template('calci.html', result=result)
        else:
            return render_template('calci.html')


if __name__ == '__main__':
    app.run(debug=True)