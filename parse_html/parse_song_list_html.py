import json
from bs4 import BeautifulSoup

from utils.string_utils import extract_chinese


def html_to_markdown(song_list):
    # 生成Markdown表格
    table = "| **歌曲** | **歌手** |\n|---------|----------|\n"
    for song in song_list:
        table += f"| {song[0]} | {song[1]} |\n"

    return table


def get_songs(html_file_path):
    """
    通过 html 字符串
    :param html_file_path:
    :return:
    """
    # 从HTML文件中读取内容
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
    # 创建BeautifulSoup对象并解析HTML内容
    soup = BeautifulSoup(html_content, 'html.parser')
    # 查找歌曲列表项
    song_items = soup.find_all('div', class_='songlist__item')
    # 创建存储歌曲和歌手的列表
    songs = []
    # 提取歌曲和歌手信息
    for item in song_items:
        song_name = item.find('span', class_='songlist__songname_txt').find('a').text.strip()
        artist_name = item.find('a', class_='playlist__author').text.strip()
        songs.append((song_name, artist_name))
    return songs


def save_songs_as_json(songs, json_file_path):
    song_list = []
    for song in songs:
        song_dict = {
            'song_name': song[0],
            'artist_name': song[1],
            'downloaded': False  # 默认设置为未下载
        }
        song_list.append(song_dict)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(song_list, json_file, indent=4, ensure_ascii=False)

    print(f"歌曲列表已保存为JSON文件：{json_file_path}")


def save_todo_as_markdown(song_list, markdown_file_path):
    # 生成Markdown待办列表
    todo_list = ""
    for song in song_list:
        todo_list += f"- [ ] {extract_chinese(song[0])}-{song[1]}\n"

    with open(markdown_file_path, 'w', encoding='utf-8') as markdown_file:
        markdown_file.write(todo_list)

    print(f"待办事项列表已保存为Markdown文件：{markdown_file_path}")


html_path = "life_songs.html"
songs = get_songs(html_path)
# 将HTML转换为Markdown表格
markdown_table = html_to_markdown(songs)

# 将Markdown表格保存到Markdown文件
output_file = 'song_list.md'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(markdown_table)

print(f"Markdown表格已保存到 {output_file}")

# 调用函数将歌曲列表保存为JSON文件
output_json_file = 'song_list.json'
# 保存为JSON文件
save_songs_as_json(songs, output_json_file)

# 将待办事项保存为Markdown文件
todo_output_file = 'todo_list.md'
save_todo_as_markdown(songs, todo_output_file)
