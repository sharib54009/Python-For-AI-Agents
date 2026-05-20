from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/sqrt', methods=['GET', 'POST'])
def compute_sqrt():

    if request.method == 'POST':

        try:
            num1 = request.form.get('num1', type=float)
            num2 = request.form.get('num2', type=float)

            if num1 is None or num2 is None:
                error = 'Both Number 1 and Number 2 are required.'
                return render_template('form.html', error=error)

            if num2 == 0:
                error = 'Division by zero is not allowed.'
                return render_template('form.html', error=error)

            division_result = num1 / num2

            if division_result < 0:
                error = 'Cannot compute square root of a negative number.'
                return render_template('form.html', error=error)

            sqrt_result = math.sqrt(division_result)

            return render_template(
                'result.html',
                division_result=division_result,
                sqrt_result=sqrt_result
            )

        except (ValueError, TypeError):
            error = 'Invalid input. Please provide numeric values for Number 1 and Number 2.'
            return render_template('form.html', error=error)

    else:
        return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=False)
