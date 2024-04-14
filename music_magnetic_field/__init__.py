# pip install selenium

# selenium 4
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from music_magnetic_field.constants import SAVE_MUSIC_PATH


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

search_page_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

search_page_driver.get("https://www.hifini.com/search.htm")
assert "音乐" in search_page_driver.title
keyword = search_page_driver.find_element(By.NAME, "keyword")
keyword.clear()
keyword.send_keys("荷塘月色")

submit = search_page_driver.find_element(By.ID, "submit")
submit.click()

search_first_link = search_page_driver.find_element(By.CSS_SELECTOR,
                                                    '#body > div > div > div > div.card.search > div.card-body > ul > '
                                                    'li:nth-child(1) > div > div.subject.break-all > a')

page_url = search_first_link.get_attribute("href")
print("page_url", page_url)

search_page_driver.get(page_url)

# search_page_driver.execute_script("""
# function fnCopy(copyText) {
#
#       const input = document.createElement('input')
#       document.body.appendChild(input)
#       input.setAttribute('value', copyText)
#       input.select()
#       if (document.execCommand('copy')) {
#         document.execCommand('copy')
#       }
#       document.body.removeChild(input)
#       console.log('复制成功')
#
# }
#
# fnCopy(`${ap4.music.title}-${ap4.music.author}`)
# window.open(ap4.audio.src)
# """)

song_name = search_page_driver.execute_script("return `${ap4.music.title}-${ap4.music.author}`;")
print("song_name", song_name)
audio_src = search_page_driver.execute_script("return ap4.audio.src;")

file_path = f'{SAVE_MUSIC_PATH}/{song_name}'
save_audio(audio_src, file_path, {"song_name": song_name})

# # 当前窗口句柄
# current_window_handle = search_page_driver.current_window_handle
# print("current_window_handle", current_window_handle)
# # 获取所有窗口句柄
# windows = search_page_driver.window_handles
# print(windows)
# # 窗口切换到最新打开的窗口
# search_page_driver.switch_to.window(windows[-1])
#
# # 当前窗口句柄
# current_window_handle = search_page_driver.current_window_handle
# print("current_window_handle", current_window_handle)
#
# music_source = search_page_driver.find_element(By.CSS_SELECTOR, "body > video > source")
# music_url = music_source.get_attribute("src")

time.sleep(5)
search_page_driver.close()
