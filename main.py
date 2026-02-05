from flask import Flask, request, jsonify, abort
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api_key = "123456789"
@app.route('/api/data')
def get_data():
    key = request.headers.get('X-API-Key') or request.args.get('api_key')
    if key != api_key:
        abort(401, description="Unauthorized: Invalid API Key")
    data = {
        "message": "Hello, this is your data!",
    }
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
        