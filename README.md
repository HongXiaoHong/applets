# applets
各种小程序

## file_information_batch_modification | 文件信息批量修改
将文件夹中的音乐文件规范成 歌名-歌手.后缀
并且移动到 good 目录中
最后导出一份 CSV
可在 Excel 中查看

## rename | 重命名文件 
批量修改文件名
从1开始

## my_server | web 测试服务
开启一个 web 服务提供测试

## job_data | 爬虫寻找职位公司信息
51job.py 寻找前程无忧的公司

1. 设置搜索条件

![](https://raw.githubusercontent.com/HongXiaoHong/images/main/picture/msedge_INQcqykxUN.png)

2. 寻找可用接口调用

点击第二页看到一个搜索的接口
![](https://raw.githubusercontent.com/HongXiaoHong/images/main/picture/msedge_4OqAlq8aNl.png)

```http request
GET /api/job/search-pc?api_key=51job&timestamp=1689436776&keyword=&searchType=2&function=&industry=&jobArea=030200&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=01%2C02%2C06&companySize=&jobType=&issueDate=&sortType=0&pageNum=3&requestId=cebc409685705e61627b666f91c753f4&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb HTTP/1.1
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Cookie: guid=d7ca1777098353a02805c23ffc75de87; slife=lastvisit%3D030200%26%7C%26; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22d7ca1777098353a02805c23ffc75de87%22%2C%22first_id%22%3A%22189499b6fd9c16-0531a7a58a2611-7e56547f-1327104-189499b6fda868%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com.hk%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5NDk5YjZmZDljMTYtMDUzMWE3YTU4YTI2MTEtN2U1NjU0N2YtMTMyNzEwNC0xODk0OTliNmZkYTg2OCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6ImQ3Y2ExNzc3MDk4MzUzYTAyODA1YzIzZmZjNzVkZTg3In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22d7ca1777098353a02805c23ffc75de87%22%7D%2C%22%24device_id%22%3A%22189499b6fd9c16-0531a7a58a2611-7e56547f-1327104-189499b6fda868%22%7D; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60030200%7C%21recentSearch0%7E%60030200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA01%2C02%2C06%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60030200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA01%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60030200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA06%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60030200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; partner=www_google_com_hk; seo_refer_info_2023=%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com.hk%5C%2F%22%2C%22referHost%22%3A%22www.google.com.hk%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D; privacy=1689430162; JSESSIONID=5CBE842E75BF7122D00B44EFC3073216; ssxmod_itna=QqUx0DgD2DnAGQDC+DXCWP0IY+=Rz3rQN73Yq7DlEDWqPGzDAxn40iDtrrueOiZ00wFK+iiP2WU/A34YFPuA+DqEKWZLeGLDmKDyKW44PDxhq0rD74irDDxD3DbRdDSDWKD9D0bMgy2VKDbxi36xiaDGeDec9ODY5DhxDCR0PDwx0C6p2DKnI+CgA1FbyD3fG46xG1740H6nfvbS3jK0v+I+SGfCKDXcdDvhv1ZgppDB4C/pyGD2G3N0DPOardjQGY1705bLrx6D2qqhxBhhDvqWh4Dh2nDDp4KjUS4D; ssxmod_itna2=QqUx0DgD2DnAGQDC+DXCWP0IY+=Rz3rQN73YqD6pSD05TnD03q3+nzKOO6KR8RRDAIzVlE7i25N/riohsll6rKq+3/2GhQhK8hahxIc/3Mx4OtO+=b2TRiW9vT0LsWKkbjOFki62QQd+M74GF4uQXIE0DaAj4wB55=QR90fineEYY=kTkSnvq2RE4=erbXQTX3aKKqfpqkaYO8dFHkdn6+u9OLZRDyZROghc4yRK7=CK+=CFmdC267D9PvojmkpoIkcSE6=Njht60OfFphwl266CfgIF7y+c8LKZ4vaCbwvE1HmobHedMRi/d1HuFdqFH4QtRFkhY5l5oE7ui+H8Kxu1/bFVBhvMth8KA3kwdW9oh6b8vWC2EmmCwHqmX3HXkIB4pnCmjCwtoI87Tju5/0bOCTFwvUMARMvBCpN3mN4QzoARjarcTW=FYxfn7E/jpYdW7hYZnrhPLZgfq0IO=qEDDwomo0qeoeLWp5eABKhg3FMb+D=mXBw5QDnQDN77/Q6Nr7qw7BBPeEDAGDhDpxWqt0yAD5hGKiYBMKEquGxwDei5ji+rLpEQDDjKDeuD4D==; acw_tc=ac11000116894367772894763e00e02f304957f1a06e16e54c5225021a09f6; acw_sc__v2=64b2c269862dd5cb4e86ba3d3235c0eb306db584
From-Domain: 51job_web
Host: we.51job.com
Referer: https://we.51job.com/pc/search?jobArea=030200&keyword=&searchType=2&companyType=01,02,06&sortType=0&metro=
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79
account-id:
dnt: 1
partner: www_google_com_hk
property: %7B%22partner%22%3A%22www_google_com_hk%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D030200%26keyword%3D%26searchType%3D2%26companyType%3D01%2C02%2C06%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%22%2C%22userType%22%3A%22%22%2C%22isLogin%22%3A%22%E5%90%A6%22%2C%22accountid%22%3A%22%22%7D
sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sign: ae74c815793331f5a6306798b0593e9eeff7fa3977785e73dc6032ba645a08b5
user-token:
uuid: d7ca1777098353a02805c23ffc75de87
```

不过这个接口请求次数是有限制的, 这里是 9 次
所以一段时间之后就要重新获取请求头
3. 最后获取的结果 保存到一个 Excel 里面

![](https://raw.githubusercontent.com/HongXiaoHong/images/main/picture/EXCEL_gFpfs2bWHu.png)

## 位于分支的applets
### random-quote-machine
原本是打算做一个返回随机名言的接口
随机名言还要使用爬虫进down一些名言警句下来
还有一个想法是
从 BrainyQuote 这个网站爬虫抓取每天的名言警句
[BrainyQuote-quote_of_the_day](https://www.brainyquote.com/quote_of_the_day)

但是突然间想做一个随机歌词的接口也不错
毕竟有一部分lrc文件了

从文件夹 E:/BaiduSyncdisk/music/lyrics 中
读取lrc 文件后
提取文件中的连续几句作为返回

访问 [获取歌词](http://localhost:8888/random/lrcs)
就可以得到
```json5
[
    {
        "author": "林宥嘉",
        "lrcs": [
            "",
            "",
            ""
        ],
        "song": "浪费"
    },
    {
        "author": "郭静",
        "lrcs": [
            "我的爱会攀上窗台盛放",
            "打开窗你会看到悲伤融化",
            "你会闻到幸福晴朗的芬芳"
        ],
        "song": "心墙"
    },
    {
        "author": "胡彦斌",
        "lrcs": [
            "曾爱的贪得无厌",
            "也要为过去留一些尊严",
            "散了我们就干脆一点"
        ],
        "song": "你要的全拿走"
    },
    {
        "author": "周慧敏",
        "lrcs": [
            "伴我星夜里幻想",
            "方知不用太紧张",
            "没法隐藏这份爱"
        ],
        "song": "最爱"
    },
    {
        "author": "林宥嘉",
        "lrcs": [
            "我跟谁变得亲密 谁逐渐离我远去",
            "华丽演出共襄盛举 唯有你的背影",
            "友情客串却留下刻骨铭心的回忆"
        ],
        "song": "神秘嘉宾"
    },
    {
        "author": "洪卓立",
        "lrcs": [
            "我未有想过绝望看她走",
            "「分手」两字情绝不留",
            "为爱伤心的声线 变了怀旧"
        ],
        "song": "弥敦道"
    },
    {
        "author": "林志炫",
        "lrcs": [
            "Right now 闭上眼用心去感受",
            "有一个声音 它说爱情 没离开过",
            ""
        ],
        "song": "没离开过"
    },
    {
        "author": "Tank",
        "lrcs": [
            "等待良人归来那一刻 眼泪为你唱歌",
            "在我离你远去那一天 蓝色的雨下在我眼前",
            "骄傲的泪 不敢弃守我眼睛"
        ],
        "song": "三国恋"
    },
    {
        "author": "林峰",
        "lrcs": [
            "前事最怕有人提起 就算怎么伸尽手臂",
            "我们亦有一些距离",
            "我情愿我狠心憎你 我还在记忆中找你"
        ],
        "song": "爱在记忆中找你"
    }
]
```

### early_bed_healthy_player | 早睡身体好播放器

做一个 播放器
功能:

- 收集本地目录的文件, 做成一个歌单, 还没完全自动 todo
- 返回 对应的mp3文件
- 获取歌词