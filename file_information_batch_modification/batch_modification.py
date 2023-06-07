import os
import csv
from mutagen.easyid3 import EasyID3
from mutagen.wave import WAVE
from mutagen.flac import FLAC
from mutagen.mp4 import MP4

# 导出元数据信息到 CSV 文件中进行查看

def extract_audio_metadata(folder_path, output_csv):
    # 打开CSV文件并写入表头
    with open(output_csv, 'w', newline='', encoding='gbk') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['文件名后缀', '文件名', '艺术家', '专辑', '标题'])

        # 遍历文件夹中的文件
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                # 检查文件扩展名，仅处理音频文件
                if filename.lower().endswith(('.mp3', '.ogg', '.flac', '.wav')):
                    filename_without_suffix = filename[:filename.rfind('.')]
                    file_path = os.path.join(root, filename)
                    song_name, author = filename_without_suffix.split("-")

                    try:
                        audio = getAudio(file_path, filename)

                        artist = audio.get('artist', [''])[0]
                        if has_error_character(artist) \
                                or artist == "" \
                                or "sd00.cn" in artist \
                                or "本子音乐网" in artist:
                            artist = author

                        album = audio.get('album', [''])[0]
                        try:
                            album = audio.get('album', [''])[0].encode('latin1').decode('gbk')
                        except:
                            pass
                        if album == "" \
                                or "sd00.cn" in album \
                                or "本子音乐网" in album:
                            album = song_name

                        title = audio.get('title', [''])[0]
                        if has_error_character(title) \
                                or title == "" \
                                or "sd00.cn" in title \
                                or "本子音乐网" in title:
                            title = song_name

                        # 将文件信息写入CSV文件
                        writer.writerow([filename, filename_without_suffix, artist, album, title])
                    except Exception as e:
                        print(f"无法处理文件 '{file_path}': {str(e)}")
                        writer.writerow([filename, filename_without_suffix, "", "", "", "", ""])


def has_error_character(title):
    if '\u04bb' in title \
            or '\x83' in title \
            or '\xc0' in title \
            or '\xc4' in title \
            or '\xcd' in title \
            or '\xd1' in title \
            or '\xc2' in title \
            or '\xd5' in title \
            or '\xc1' in title \
            or '\xba' in title \
            or '\xb4' in title \
            or '\xbd' in title:
        print(f"error title is {title}")
        return True
    return False


def getAudio(file_path, filename):
    if filename.lower().endswith('.mp3'):
        audio = EasyID3(file_path)  # 使用mutagen读取音频元数据
    elif filename.lower().endswith('.wav'):
        audio = WAVE(file_path)
    elif filename.lower().endswith('.flac'):
        audio = FLAC(file_path)
    elif filename.lower().endswith('.m4a'):
        audio = MP4(file_path)
    return audio


# 用法示例
folder_path = 'E:/BaiduSyncdisk/music/favorite/good'  # 替换为要遍历的文件夹路径
output_csv = 'E:/BaiduSyncdisk/music/favorite/to/output.csv'  # 替换为输出CSV文件的路径

extract_audio_metadata(folder_path, output_csv)
