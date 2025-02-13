from flask import Flask, jsonify, request
from main import recommend_songs

app = Flask(__name__)

@app.route('/api/v1/prediction', methods=['POST'])
def get_data():
    song_name = request.json.get('song_name')
    if not song_name:
        return jsonify({"errors":"Kindly select a song, Thank you,"})
    data = recommend_songs(song_name=song_name,n_recommendations=5)
    return jsonify(data['name'])


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)
