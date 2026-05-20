from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        message = request.form.get('message', 'no message')
        return render_template_string('<h1>You submitted: {{message}}</h1>', message=message)
    return render_template_string('''
        <form method="post" action="/submit">
           <input type="text" name="message" placeholder="Enter a message">
           <input type="submit" value="Submit">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)