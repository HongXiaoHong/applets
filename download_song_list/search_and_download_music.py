import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from download_song_list import get_music_page_url, get_page_html_from_url, download_music
from constants import DOMAIN, MAX_TIMES, MAX_SEARCH_TIMES

# 创建浏览器实例
driver = webdriver.Chrome()  # 需要安装Chrome浏览器及对应的驱动

# 打开页面
driver.get(DOMAIN + "/search.htm")  # 替换为要访问的页面URL


def search_and_download_music(song):
    # 找到搜索框并输入关键字
    search_box = driver.find_element(By.NAME, "keyword")  # 替换为搜索框的定位方式和值
    search_box.clear()  # 清空输入框的内容
    search_box.send_keys(f'{song["artist_name"]} {song["song_name"]}')  # 替换为要搜索的关键字
    # 找到搜索按钮并点击
    search_button = driver.find_element(By.ID, "submit")  # 替换为搜索按钮的定位方式和值
    search_button.click()
    # 等待搜索结果加载完成（示例中等待10秒）
    wait = WebDriverWait(driver, 10)
    # search_results = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "threadlist")))  # 替换为搜索结果的定位方式和值
    # 获取新页面的内容
    new_page_content = driver.page_source
    # print(new_page_content)
    # 处理新页面的内容
    # 处理搜索结果
    # 得到第一个搜索结果的url
    if new_page_content:
        music_page_url = get_music_page_url(new_page_content, song)
        if music_page_url:
            music_page_html = get_page_html_from_url(DOMAIN + "/" + music_page_url)
            if music_page_html:
                download_music(music_page_html, song)
                return True
    else:
        print("{0}这首歌搜索不到".format(song["song_name"]))
    return False


download_times = 1
searched_times = -1
with open('song_list.json', 'r', encoding='utf-8') as json_file:
    song_list = json.load(json_file)
try:
    for song in song_list:
        if download_times > MAX_TIMES or searched_times > MAX_SEARCH_TIMES:
            break
        if not song["downloaded"] and not song["tried"]:
            searched_times += 1
            downloaded = search_and_download_music(song)
            if downloaded:
                song["downloaded"] = True
                download_times += 1
                # 等待 1 min 30 s
                time.sleep(90)
        song["tried"] = True
finally:
    with open('song_list.json', 'w', encoding='utf-8') as json_file:
        json.dump(song_list, json_file, indent=4, ensure_ascii=False)

# 关闭浏览器
driver.quit()
