import os

import requests

cookies = {
    'kpf': 'PC_WEB',
    'clientid': '3',
    'did': 'web_e45d805382b61f95d23f2dacc976e9c8',
    'ktrace-context': '1|MS43NjQ1ODM2OTgyODY2OTgyLjYxNzI3ODUxLjE3MDA0NDk0ODk1MDguMzkwNjQ4|MS43NjQ1ODM2OTgyODY2OTgyLjEyODE3MjM2LjE3MDA0NDk0ODk1MDguMzkwNjQ5|0|graphql-server|webservice|false|NA',
    'kpn': 'KUAISHOU_VISION',
}

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'kpf=PC_WEB; clientid=3; did=web_e45d805382b61f95d23f2dacc976e9c8; ktrace-context=1|MS43NjQ1ODM2OTgyODY2OTgyLjYxNzI3ODUxLjE3MDA0NDk0ODk1MDguMzkwNjQ4|MS43NjQ1ODM2OTgyODY2OTgyLjEyODE3MjM2LjE3MDA0NDk0ODk1MDguMzkwNjQ5|0|graphql-server|webservice|false|NA; kpn=KUAISHOU_VISION',
    'Origin': 'https://www.kuaishou.com',
    'Referer': 'https://www.kuaishou.com/profile/3xvwhhjmxzwfzqq',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'accept': '*/*',
    'content-type': 'application/json',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'operationName': 'visionProfilePhotoList',
    'variables': {
        'userId': '3xvwhhjmxzwfzqq',
        'pcursor': '',
        'page': 'profile',
    },
    'query': 'fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n',
}
url = 'https://www.kuaishou.com/graphql'
response = requests.post(url, cookies=cookies, headers=headers, json=json_data)
print(response.json())
backup_urls = []
for feed in response.json()['data']['visionProfilePhotoList']['feeds']:
    manifest = feed['photo'].get('manifest')
    if manifest:
        for adaptation_set in manifest.get('adaptationSet', []):
            for representation in adaptation_set.get('representation', []):
                backup_urls.extend(representation.get('backupUrl', []))

# 打印所有的 backupUrl
for url in backup_urls:
    print(url)
# 下载所有视频
# for i, url in enumerate(backup_urls):
#     response = requests.get(url)
#     if response.status_code == 200:
#         video_filename = os.path.join('C:/DownLoads', f'video_{i}.mp4')
#         with open(video_filename, 'wb') as video_file:
#             video_file.write(response.content)
#         print(f'Video {i} downloaded and saved as {video_filename}')
#     else:
#         print(f'Failed to download video {i}')