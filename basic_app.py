from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        name = request.form['name']
        message = f"Hello, {name}! Welcome to the Python Web App!"
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Python Web App</title>
        </head>
        <body>
            <h1>Welcome to the Python Web App</h1>
            <form method="POST">
                <label for="name">Enter your name:</label>
                <input type="text" id="name" name="name" required>
                <input type="submit" value="Submit">
            </form>
            <p>{{ message }}</p>
        </body>
        </html>
    """, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
