import os

from flask import Flask, jsonify, send_file, request
from flask_cors import CORS

from constants import SAVE_MUSIC_PATHS, MIME_TYPE

app = Flask(__name__)
CORS(app)


def search_sons(song_path):
    """
    搜索某个目录下的歌曲
    @param song_path: 目录
    @return: 歌单 {歌名: 后缀,...}
    """
    song_filenames = {}
    song_files = os.listdir(song_path)
    for file in song_files:
        song_filenames[file[:file.index(".")]] = file[file.index(".") + 1:]
    return song_filenames


@app.route("/playlist", methods=['GET'])
def random_lrcs():
    data = {
        "favorite": search_sons(SAVE_MUSIC_PATHS["favorite"]),
        "like": search_sons(SAVE_MUSIC_PATHS["like"]),
        "exercise": search_sons(SAVE_MUSIC_PATHS["exercise"])
    }
    return jsonify(data)


@app.route('/audio/<filename>', methods=['GET'])
def get_audio(filename):
    suffix = get_suffix()
    currentPlaylistChoose = request.args.get("currentPlaylistChoose")
    favorite_path = SAVE_MUSIC_PATHS[currentPlaylistChoose]
    return send_file(favorite_path + '/' + filename + "." + suffix,
                     mimetype=MIME_TYPE[suffix])


def get_suffix():
    suffix = request.args.get("suffix")
    if suffix not in MIME_TYPE:
        raise Exception('音乐文件只能是 {} 这两种类型, 您现在输入的是值为: {}'.format(LIMIT_SUFFIX, suffix))
    return suffix


@app.route('/lyrics/<filename>', methods=['GET'])
def get_lyrics(filename):
    with open("E:/BaiduSyncdisk/music/lyrics/{}.lrc".format(filename), "r", encoding='utf-8') as lrc:
        lrc_content = lrc.read()
    return jsonify({
        "lrc": lrc_content
    })


if __name__ == "__main__":
    app.run(host='localhost', port=8891)
