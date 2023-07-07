import os
import random
import re

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
LRC_DIRECTORY = "E:/BaiduSyncdisk/music/lyrics"


def get_chinese_lrc_files(lrc_directory):
    lrc_files = []
    for root, dirs, files in os.walk(lrc_directory):
        for file in files:
            if file.endswith(".lrc") and re.search(r'[\u4e00-\u9fa5]+', file):
                lrc_files.append(os.path.join(root, file))
    return lrc_files


def print_random_lrc_files(directory, count, lyric_lines):
    result = []
    lrc_files = get_chinese_lrc_files(directory)
    if len(lrc_files) < count:
        print(f"Only found {len(lrc_files)} lrc files, cannot get {count} files.")
        return result
    selected_files = random.sample(lrc_files, count)
    for file in selected_files:
        # print(f"File: {file}")
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        song = re.search(r'\[ti:(.*?)\]', lines[1]).group(1)
        artist = re.search(r'\[ar:(.*?)\]', lines[2]).group(1)
        lyrics = [line for line in lines[3:] if not re.match(r'\[.*?\].*?:', line)]

        if len(lyrics) < lyric_lines:
            print(f"Not enough lyrics in file {file}. Only found {len(lyrics)} lines.")
            continue
        start_line = random.randint(0, len(lyrics) - lyric_lines)
        selected_lyrics = [re.sub(r'\[.*?\]', '', line) for line in lyrics[start_line: start_line + lyric_lines]]
        # print(f"Song: {song}\nArtist: {artist}\nLyrics:\n{''.join(selected_lyrics)}")
        # print("\n")
        result.append({
            "song": song,
            "author": artist,
            "lrcs": selected_lyrics
        })
    return result


@app.route("/random/lrcs")
def random_lrcs():
    data = print_random_lrc_files(LRC_DIRECTORY, 10, 3)
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='localhost', port=8888)
