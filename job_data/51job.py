import requests
import json
import pandas as pd


def get_list(i):
    url = "https://we.51job.com/api/job/search-pc?api_key=51job&timestamp=1689436776&keyword=&searchType=2&function=&industry=&jobArea=030200&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=01%2C02%2C06&companySize=&jobType=&issueDate=&sortType=0&pageNum=" + str(
        i) + "&requestId=cebc409685705e61627b666f91c753f4&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb"

    headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", "Connection": "keep-alive",
               "Cookie": "guid=d7ca1777098353a02805c23ffc75de87; slife=lastvisit%3D030200%26%7C%26; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22d7ca1777098353a02805c23ffc75de87%22%2C%22first_id%22%3A%22189499b6fd9c16-0531a7a58a2611-7e56547f-1327104-189499b6fda868%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com.hk%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5NDk5YjZmZDljMTYtMDUzMWE3YTU4YTI2MTEtN2U1NjU0N2YtMTMyNzEwNC0xODk0OTliNmZkYTg2OCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6ImQ3Y2ExNzc3MDk4MzUzYTAyODA1YzIzZmZjNzVkZTg3In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22d7ca1777098353a02805c23ffc75de87%22%7D%2C%22%24device_id%22%3A%22189499b6fd9c16-0531a7a58a2611-7e56547f-1327104-189499b6fda868%22%7D; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60030200%7C%21recentSearch0%7E%60030200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA01%2C02%2C06%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60030200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA01%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60030200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA06%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60030200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; acw_tc=ac11000116894367772894763e00e02f304957f1a06e16e54c5225021a09f6; acw_sc__v2=64b2c269862dd5cb4e86ba3d3235c0eb306db584; acw_sc__v3=64b2c423175e33ec1cafb2a03c7f212f7341ba9d; JSESSIONID=B0E09CAE4B1D8100165DEAFFB6D7C275; ssxmod_itna=eqGxyWD=it0QW4Ba8e5DkDBjb=qiIIjKXAIeqdD/KDfo4iNDnD8x7YDv+ATRY+/iBTd4OQA+7qd68CraIdo72nEhetoASyvYDU4i8DCLxyxCxeetD5xGoDPxDeDADYE0DAqiOD7qDd06TXZmqDEDYPBDA3Di4D+GT=DmqG0DDtO/4G2D7tBUBxB8lLYuduM8A2xKDtDjkTD/fpHoDU3haF4/LrWaciaWqGyDKGu9dNDqdTDCOUDguiGmSqo93wY8hpKK7weYAoo00wFQMwhF8DRFBTrjY+sfGDDGfG33TD==; ssxmod_itna2=eqGxyWD=it0QW4Ba8e5DkDBjb=qiIIjKXAIeqG9b5QUDfxGXIydGa8Wj5As+ojp0IQD6lxyUx2Q8M7+p5kmCE0wHF3Z7xjMj1p7akOA+CdBIzodCh826=D1A=9ep80KCIXCHydzUy=GbZ1Hrbp2CDRyry=KiqBKib6Pi4pqOdl5rMhY141Tzr25m5g7HIfPfU=giuG9Dseu=i/Wqp+Tq2GAi4KwiVSLC0Kl=RYnzZznzN2BWy3TuqqgRU9OQTX3zUxOwUIokD65Cb/5i52KEVxOBIRnai9vn9n5uuNkj0wAQgXTjDrWx02NI5+K9VnyDNTX/vWzRVGmOGvaF4lGYxbYERcV3ccIv1S7lWRqTuV9qSI5wDovDghDEi855y7migQO4Cm7+f7gI5yz5NkcYVGQKgaKg462wK5=XerxomD5byrrEOYKAm/GEQH4bxDKkDoYqOBoxWeHaeMDj+Z8ifjBYeSdqD7=DYKxeD===",
               "From-Domain": "51job_web", "Host": "we.51job.com",
               "Referer": "https://we.51job.com/pc/search?jobArea=030200&keyword=&searchType=2&companyType=01,02,06&sortType=0&metro=",
               "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79",
               "account-id": "", "dnt": "1", "partner": "",
               "property": "%7B%22partner%22%3A%22%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D030200%26keyword%3D%26searchType%3D2%26companyType%3D01%2C02%2C06%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%22%2C%22userType%22%3A%22%22%2C%22isLogin%22%3A%22%E5%90%A6%22%2C%22accountid%22%3A%22%22%7D",
               "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"",
               "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"",
               "sign": "a166a793b9fb8ad7e3630608f36327dd93c0991694a6d294c66369ef48a49c9b", "user-token": "",
               "uuid": "d7ca1777098353a02805c23ffc75de87"}
    response = requests.get(url, headers=headers)
    # print the response text
    print(response.text)
    # 将字符串解析为Python字典
    data_dict = json.loads(response.text)
    # 获取items列表
    items = data_dict['resultbody']['job']['items']
    # 创建一个空的列表，用于存储职位行业和公司
    job_list = []
    # 遍历items
    for item in items:
        # 职位
        jobName = item['jobName']
        # 获取职位行业
        industry1 = item['industryType1Str']
        industry2 = item['industryType2Str']
        # 获取公司名称
        company = item['fullCompanyName']
        # 将职位行业和公司添加到列表
        job_list.append({'职位': jobName, '行业1': industry1, '行业2': industry2, '公司全名': company})
    return job_list


def gather_and_combine_lists():
    # 创建一个空列表来存放所有的列表
    combined_list = []

    for i in range(9):
        # 获取列表并添加到总列表中
        combined_list.extend(get_list(i))

    return combined_list


array = gather_and_combine_lists()
# 创建一个DataFrame
df = pd.DataFrame(array)

# 保存到Excel文件
df.to_excel('job_data.xlsx', index=False)
