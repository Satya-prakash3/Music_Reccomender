from flask import Flask, jsonify, request,  render_template
from main import recommend_songs

app = Flask(__name__)

@app.route('/',methods=['GET'])
def root_file():
    return render_template("index.html")

@app.route('/api/v1/prediction', methods=['POST'])
def get_data():
    song_name = request.json.get('song_name')
    number_of_recomendation =request.json.get('n')
    if not song_name:
        return jsonify({"errors":"Kindly select a song, Thank you,"}), 400
    data = recommend_songs(song_name=song_name,n_recommendations=number_of_recomendation)
    if "errors" in data:
        return jsonify(data), 400
    else:
        return jsonify(data), 200
        


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)