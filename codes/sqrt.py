from flask import Flask, render_template_string, request
import math

app = Flask(__name__)

@app.route('/sqrt', methods=['GET'])
def sqrt():
    try:
        num1 = request.args.get('num1', type=float)
        num2 = request.args.get('num2', type=float)

        if num1 is None or num2 is None:
            return render_template_string('<h1>Please provide both num1 and num2 as query parameters.</h1>')
        if num1 < 0 or num2 < 0:
            return render_template_string('<h1>Please provide non-negative numbers.</h1>')
        
        if num2 == 0:
            return render_template_string('<h1>Cannot divide by zero.</h1>')
        
        result = num1 / num2

        if result < 0:
            return render_template_string('<h1>Result is negative. Cannot compute square root.</h1>')
        
        sqrt_result = math.sqrt(result)
        return render_template_string('<h1>The square root of {{num1}} divided by {{num2}} is {{sqrt_result}}.</h1>', num1=num1, num2=num2, sqrt_result=sqrt_result)
    except ValueError:
        return render_template_string('<h1>Invalid input. Please provide valid numbers.</h1>')
    

if __name__ == '__main__':
    app.run(debug=True)