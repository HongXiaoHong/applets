import re
from bs4 import BeautifulSoup
import requests

from constants import DOMAIN, SAVE_MUSIC_PATH


def save_audio(url, file_path, song_info):
    """
    通过请求url保存音乐文件到本地
    :param song_info: 需要保存的歌曲信息
    :param url: 音乐请求url
    :param file_path: 音乐保存路径
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        # 添加其他请求头字段，根据需要自行添加
    }
    response = requests.get(url, headers=headers, stream=True)

    if response.status_code == 200:
        content_type = response.headers.get('Content-Type')
        file_extension = '.mp3'
        if content_type == 'audio/x-m4a' or content_type == "audio/mp4":
            file_extension = '.m4a'

        file_path_with_extension = file_path + file_extension

        with open(file_path_with_extension, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print('File saved successfully:', file_path_with_extension)
    else:
        print('Failed to download file:', response.status_code, song_info)


def extract_music_url(json_string):
    """
    通过正则表达式获取json字符串中的音乐请求url
    :param json_string: 脚本script 中的json字符串
    :return: 音乐请求url
    """
    music_url = ""
    # 解析 JSON 字符串
    # 使用正则表达式匹配 URL
    match = re.search(r"url:\s*'([^']+)'", json_string)

    # 获取第一个匹配的 URL
    if match:
        music_url = match.group(1)
        # print(music_url)

    return music_url


def download_music(html_content, song_info):
    """
    从html中找到对应的音乐请求 url , 再通过url进行下载
    :param html_content: 音乐保存页面
    """
    if html_content is None or html_content == "":
        # 打开HTML文件并读取内容
        with open('test.html', 'r', encoding="utf-8") as file:
            html_content = file.read()

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找所有的<script>标签
    script_tags = soup.find_all('script')

    # 遍历所有的<script>标签，找到目标代码段
    target_code = None
    for script in script_tags:
        # 假设目标代码段包含特定的变量名或标识符
        if script.string and 'ap4' in script.string:
            target_code = script.string
            break

    # 打印目标代码段
    if target_code:
        # print(target_code)
        # 假设 script_string 是包含了 var ap4 = new APlayer({...}) 的字符串

        # 使用正则表达式提取 APlayer 参数的部分
        pattern = r"var\s+ap4\s*=\s*new\s+APlayer\s*\((.*?)\);"
        match = re.search(pattern, target_code, re.DOTALL)
        if match:
            ap4_params = match.group(1)
            # print(ap4_params)
            # 处理 APlayer 参数
            # 在这里，ap4_params 是一个包含参数内容的字符串
            # 您可以根据需要进一步解析和处理参数
            music_url = extract_music_url(ap4_params)
            # print(music_url)
            domain = "https://www.hifini.com/"
            request_url = DOMAIN + "/" + music_url
            # print(request_url)
            # 调用 save_mp3 函数保存音频文件
            file_path = f'{SAVE_MUSIC_PATH}/{song_info["song_name"]}-{song_info["artist_name"]}'
            save_audio(request_url, file_path, song_info)
        else:
            # 未找到 APlayer 参数
            pass


def get_music_page_url(html_content, song_info):
    """
    从html中获取搜索结果中的音乐页面url
    :param song_info: 歌曲信息
    :param html_content: html 页面
    :return: 搜索结果音乐url
    """
    url = ""
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='media')  # 获取所有符合条件的 li 元素

    for li_element in li_elements:
        li_song_name = li_element.find("div", class_="subject").find('a').text.strip()
        print(f"li_song_name is {li_song_name}.")
        if song_info["song_name"] in li_song_name and song_info["artist_name"] in li_song_name:
            url = li_element['data-href']
            print(li_song_name)
            break  # 找到匹配的元素后跳出循环

    if not url:
        print(f"No matching li element found for {song_info}.")

    return url


def get_page_html_from_url(page_url):
    """
    根据 URL 获取页面的html字符串
    :param page_url: url
    :return: 页面html
    """
    html_result = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        # 添加其他请求头字段，根据需要自行添加
    }
    response = requests.get(page_url, headers=headers)

    if response.status_code == 200:
        html_result = response.text
        # print('music_page_html is:', html_result)
    else:
        print('Failed to load music_page_html:', response.status_code)

    return html_result
