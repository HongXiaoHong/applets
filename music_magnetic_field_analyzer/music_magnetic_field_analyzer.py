from flask import Flask, jsonify, request
from flask_cors import CORS
from download_song_list import get_page_html_from_url, download_music

app = Flask(__name__)
CORS(app)


def download(music_page_url, request_params):
    music_page_html_content = get_page_html_from_url(music_page_url)
    # song = get_song_info(music_page_url)
    if music_page_html_content:
        return download_music(music_page_html_content, request_params)


@app.route("/music/magnetic/field/download", methods=['POST'])
def random_lrcs():
    data = request.get_json()
    url = data.get('url')
    try:
        song_info = download(url, data)
        data = song_info
        data["result"] = "success"
        print("save success: ", song_info)
    except Exception as e:
        print("An error occurred: ", e)
        data = {"result": "fail", "track": str(e)}

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='localhost', port=8888)
