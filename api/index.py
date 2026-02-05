from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    # Headers to ensure security context for Camera/Mic
    response = render_template('index.html')
    return response

if __name__ == '__main__':
    app.run(debug=True)
