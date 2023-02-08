from flask import Flask, request

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    files = request.files.getlist("files")
    for file in files:
        file.save("path/to/save/file")
    return "Files uploaded successfully"

if __name__ == "__main__":
    app.run()
