from flask import Flask, request, jsonify

app = Flask(__name__)

posts = [
    {"id": 1, "title": "11111", "body": "1111111"},
    {"id": 2, "title": "22222", "body": "2222222"},
    {"id": 3, "title": "33333", "body": "3333333"}
]

@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(posts), 200

if __name__ == "__main__":
    app.run(debug=True)
