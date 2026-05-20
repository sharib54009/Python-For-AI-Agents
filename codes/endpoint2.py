from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/greet/<name>')
def greet_func(name) :
    return render_template_string('<h1>hello, {{name}}! </h1>', name = name)

        
#This route takes number from the user and returns the square of that number
@app.route('/square/<int:number>')
def square(number):
    result = number ** 2
    return render_template_string('<h1>the square of {{number}} is {{result}}! </h1>', number = number, result = result  )



if __name__ == '__main__': 
    app.run(debug=True)