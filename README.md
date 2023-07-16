# applets

各种小程序

## 这里有个分支

### early_bed_healthy_player | 早睡身体好播放器

做一个 播放器
功能:

- 收集本地目录的文件, 做成一个歌单, 还没完全自动 todo
- 返回 对应的mp3文件
- 获取歌词


前端发来下载链接

### 歌单列表
```http
GET http://localhost:8891/playlist
```

成功响应

```json5
{
  "exercise": {
    "BOOM-Tiësto": "mp3",
    "Because Of You-Ne-Yo": "m4a",
    "Empty Love-Lulleaux": "mp3",
    "Everytime We Touch-xxxCr3": "m4a",
    "I'll Do It-Heidi Montag": "m4a",
    "RISE-The Glitch Mob": "mp3",
    "Unstoppable-Sia": "mp3"
  },
  "favorite": {
    "Angel(Live)-张杰": "mp3",
    "Infinity-JaymesYoung": "mp3",
    "Relax(TakeItEasy)-MIKA": "wav",
    "golden hour-JVKE": "m4a",
    "一样的月光-徐佳莹": "mp3",
    "三国恋-Tank": "mp3",
    "下雨天-南拳妈妈": "mp3",
    "不浪漫罪名-王杰": "mp3",
    "不要忘记我爱你-张碧晨": "mp3",
    "为你写诗-吴克群": "mp3",
    "九儿-谭晶": "mp3",
    "人世间-雷佳": "m4a",
    "人间惊鸿客-叶里": "mp3",
    "你一定要幸福-简弘亦": "mp3",
    "你要的全拿走-胡彦斌": "mp3",
    "修炼爱情-林俊杰": "m4a",
    "偏偏喜欢你-陈百强": "mp3",
    "凤凰于飞 (Live)-林俊杰": "m4a",
    "凤凰传奇-海底": "flac",
    "初恋-曾比特": "mp3",
    "勋章-鹿晗": "mp3",
    "千里之外-周杰伦费玉清": "mp3",
    "只是太爱你-张敬轩": "mp3",
    "后来的我们-五月天": "mp3",
    "告白の夜-Ayasa绚沙": "mp3",
    "嘉宾-张远": "mp3",
    "多远都要在一起-G": "E.M. 邓紫棋.m4a",
    "夜曲-周杰伦": "m4a",
    "够钟-周柏豪": "wav",
    "大眠-王心凌": "mp3",
    "天后-陈势安": "mp3",
    "天堂-腾格尔": "mp3",
    "天梯-C AllStar": "m4a",
    "天行九歌-霍尊": "m4a",
    "太多-陈冠蒲": "mp3",
    "如愿-王菲": "mp3",
    "如果你也听说-张惠妹": "mp3",
    "学不会-林俊杰": "mp3",
    "完-陈奕迅": "mp3",
    "寂寞先生-曹格": "mp3",
    "小小-容祖儿": "mp3",
    "小河淌水-龚琳娜": "mp3",
    "就让这大雨全都落下-容祖儿": "mp3",
    "弥敦道-洪卓立": "mp3",
    "心墙-郭静": "mp3",
    "心淡-容祖儿": "wav",
    "忘记时间-胡歌": "mp3",
    "念念不忘-麦浚龙": "mp3",
    "悟空-戴荃": "mp3",
    "想你的夜-关喆": "mp3",
    "想见你想见你想见你-八三夭": "mp3",
    "我怀念的-林俊杰": "m4a",
    "我是如此相信-周杰伦": "m4a",
    "我爱你不问归期 - 白小白": "mp3",
    "我的回忆不是我的-海鸣威": "mp3",
    "我的太阳-帕瓦罗蒂": "wav",
    "我的楼兰-云朵": "mp3",
    "房间-刘瑞琦": "mp3",
    "手心的蔷薇-林俊杰": "m4a",
    "指纹-胡歌": "m4a",
    "挥着翅膀的女孩-容祖儿": "wav",
    "无名之辈-陈雪燃": "mp3",
    "春秋-张敬轩": "mp3",
    "暗香-沙宝亮": "wav",
    "最后一页-江语晨": "mp3",
    "最爱-周慧敏": "mp3",
    "月光-胡彦斌": "mp3",
    "月半小夜曲-李克勤": "mp3",
    "有心人-张国荣": "mp3",
    "李健-贝加尔湖畔": "mp3",
    "极乐净土-Maria": "mp3",
    "梁山伯与茱丽叶-曹格": "mp3",
    "森林-MR": "mp3",
    "毛不易 - 红颜旧 (Live)": "flac",
    "没离开过-林志炫": "mp3",
    "浪漫血液-林俊杰": "mp3",
    "爱在记忆中找你-林峰": "mp3",
    "爱得太迟-古巨基": "mp3",
    "爱是你我-刀郎": "mp3",
    "爱的故事上集-孙耀威": "mp3",
    "男人KTV-侧田": "mp3",
    "男儿当自强-林子祥": "mp3",
    "眼鼻嘴-太阳": "mp3",
    "突然好想你-五月天": "mp3",
    "窗-虎二": "mp3",
    "答应不爱你-郑中基": "mp3",
    "红蔷薇白玫瑰-G": "E.M. 邓紫棋.m4a",
    "练习-刘德华": "mp3",
    "罗生门-麦浚龙": "mp3",
    "耿耿于怀-麦浚龙": "mp3",
    "背对背拥抱-林俊杰": "m4a",
    "致姗姗来迟的你-阿肆,林宥嘉": "mp3",
    "花海-周杰伦": "m4a",
    "这份爱-Davichi": "mp3",
    "雅俗共赏-许嵩": "mp3",
    "靠近-袁娅维": "mp3",
    "风的季节-Soler": "mp3"
  },
  "like": {
    "Far Away from Home-Groove Coverage": "m4a",
    "Letting Go (Live版)-吉克隽逸＋汪苏泷": "m4a",
    "Scarborough Fair (斯卡布罗集市)-Sarah Brightman": "m4a",
    "Звезда-Vitas": "m4a",
    "Криком журавлиным(鹤唳)-Vitas": "m4a",
    "Посвящение(奉献)-Vitas": "flac",
    "云宫迅音-许镜清": "mp3",
    "你是我的眼-林宥嘉": "m4a",
    "假如爱有天意-李健": "m4a",
    "傻子-林宥嘉": "m4a",
    "光年之外-G": "E.M. 邓紫棋.m4a",
    "光的方向-张碧晨": "m4a",
    "关键词-林俊杰": "m4a",
    "刘惜君-执迷不悔(Live)": "mp3",
    "卷珠帘 (Live)-费玉清": "m4a",
    "卷珠帘-霍尊": "m4a",
    "后知后觉-冯允谦": "m4a",
    "嘉宾(粤)-张远": "m4a",
    "嘉宾-张远": "m4a",
    "国王与乞丐-华晨宇": "mp3",
    "堆积情感-邓岳章": "m4a",
    "天龙八部之宿敌-许嵩": "mp3",
    "好想爱这个世界啊-华晨宇": "mp3",
    "如果爱忘了-蓝心羽": "m4a",
    "开始懂了-孙燕姿": "m4a",
    "张靓颖、汪苏泷-金风玉露 (Live)": "mp3",
    "心墙-林俊杰": "m4a",
    "情意结-邓岳章": "m4a",
    "情歌-侧田": "m4a",
    "想自由-林宥嘉": "m4a",
    "慢慢-张学友": "mp3",
    "时光背面的我-刘至佳": "mp3",
    "月球上的人-陈奕迅": "mp3",
    "月球下的人-李幸倪": "m4a",
    "桃花诺-G": "E.M. 邓紫棋.m4a",
    "残酷月光-林宥嘉": "m4a",
    "永不失联的爱-周兴哲": "mp3",
    "浪费-林宥嘉": "m4a",
    "海底（Live）-凤凰传奇": "mp3",
    "潇洒走一回-叶倩文": "m4a",
    "無心愛-古巨基": "m4a",
    "爱不得忘不舍-白小白": "m4a",
    "爱错-王力宏": "m4a",
    "玫瑰少年-五月天": "m4a",
    "真的爱着你 (明慧版)-明慧": "m4a",
    "神秘嘉宾-林宥嘉": "m4a",
    "童话镇 - 陈一发儿": "m4a",
    "缘分一道桥-王力宏": "m4a",
    "花香-周传雄": "m4a",
    "落花流水-陈奕迅": "m4a",
    "薛之谦 - 天外来物": "mp3",
    "赤伶（逆水寒戏曲玩法推广曲）-谭晶": "m4a",
    "起风了（旧版） - 买辣椒也用券": "m4a",
    "那些年-胡夏": "m4a",
    "那女孩对我说-小阿七": "m4a",
    "高山低谷-林奕匡": "m4a",
    "高山低谷-郑秀文": "mp3",
    "黑夜问白天-林俊杰": "m4a",
    "산다는 건 (活着 )-洪真英": "m4a"
  }
}
```

### 歌曲获取

```http request
GET /audio/Angel(Live)-%E5%BC%A0%E6%9D%B0?suffix=mp3&currentPlaylistChoose=favorite HTTP/1.1
Accept: */*
Accept-Encoding: identity;q=1, *;q=0
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Host: localhost:8891
Range: bytes=0-
Referer: http://127.0.0.1:5500/
Sec-Fetch-Dest: audio
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: cross-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79
dnt: 1
sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"

```


### 歌词

```http request
GET /lyrics/Angel(Live)-%E5%BC%A0%E6%9D%B0 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Host: localhost:8891
Origin: http://127.0.0.1:5500
Referer: http://127.0.0.1:5500/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79
dnt: 1
sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"

```

响应

```json5
{
  "lrc": "﻿[id:1306436173]\n[ti:云中的Angel (Live)]\n[ar:张杰]\n[al:Just For Star洛杉矶音乐分享会]\n[00:00.00]作词 : 谢小娜\n[00:00.33]作曲 : 谢小娜\n[00:00.66]张杰-云中的Angel（Live）\n[00:01.72]出品：Planet Culture 张杰行星文化音乐厂牌\n[00:27.74]小时候总爱抬头看白云朵朵\n[00:35.68]哼着我最爱的angel\n[00:43.57]天上白云一朵朵都住着angel\n[00:51.96]为每个相信童话的孩子守候\n[01:02.49]我最爱的那首歌最爱的angel\n[01:10.89]我到什么时候才能遇见我的angel\n[01:17.92]我最爱的那首歌最爱的angel\n[01:26.73]我不是王子也会拥有我的angel\n[01:54.52]每次受伤的时候天上的angel\n[02:02.30]会默默地为我流泪\n[02:10.44]每下一场小雨都像一个angel\n[02:18.80]陪伤心的人等着阳光出现时候\n[02:29.89]我最爱的那首歌最爱的angel\n[02:38.84]我到什么时候才能遇见我的angel\n[02:45.83]我最爱的那首歌最爱的angel\n[02:54.38]我不是王子也会拥有我的angel\n[03:10.43]当你学会勇敢就会遇见你的angel\n[03:38.21]Angel\n"
}
```

### 前端

![early_bed_healthy_player](https://raw.githubusercontent.com/HongXiaoHong/images/main/picture/msedge_EZgSA5djnQ.gif)