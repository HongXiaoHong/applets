# applets

各种小程序

## 这里有个分支

### early_bed_healthy_player | 早睡身体好播放器

做一个 播放器
功能:

- 收集本地目录的文件, 做成一个歌单
- 返回 对应的mp3文件


前端发来下载链接

```http
GET http://localhost:8891/playlist
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
