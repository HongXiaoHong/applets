# applets

各种小程序

## 这里有个分支

### music_magnetic_field_analyzer

做一个 音乐磁场 网页的解析
功能:

- 下载音乐到本地
- 返回下载的音乐信息给页面
- 选择不同目录进行下载, 见music_magnetic_field_analyzer/constants.py

复制windows路径的时候记得更换反斜杠 \ 为 斜杠 /

```python
SAVE_MUSIC_PATHS = {
    "temp": "E:/BaiduSyncdisk/music/download/temp",
    "like": "E:/BaiduSyncdisk/music/like",
    "favorite": "E:/BaiduSyncdisk/music/favorite",
    "life": "E:/BaiduSyncdisk/music/download/life",
    "exercise": "E:/BaiduSyncdisk/music/exercise",

}
```

前端发来下载链接

```http
POST http://localhost:8888/music/magnetic/field/download
Content-Type: application/json

{
    "url": "https://www.hifini.com/thread-4284.htm",
    "directory": "favorite"
}
```

成功响应

```json5
{
    "artist_name": "周柏豪",
    "music_url": "get_music.php?key=sHFKPlODpcWKT+8xzWMHKJ2nR8NkDo1z/xmSSf/+vgcnBATGy2vBJ9DX7E71soNa2+Dg7OwNQA",
    "result": "success",
    "song_name": "我的宣言"
}
```

### 前端

![music_magnetic_field_analyzer](https://raw.githubusercontent.com/HongXiaoHong/images/main/picture/music_magnetic_field_analyzer.gif)

![music_magnetic_field_analyzer_v1](https://raw.githubusercontent.com/HongXiaoHong/images/main/picture/music_magnetic_field_analyzer_v1.gif)
