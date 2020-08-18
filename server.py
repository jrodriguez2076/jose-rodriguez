from flask import Flask, send_from_directory, send_file, render_template

app = Flask(__name__)

@app.route('/')
def serve():
    return send_from_directory('dist','index.html')

if __name__ == "__main__":
    app.run()

