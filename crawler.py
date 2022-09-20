# 爬虫
from typing import Union, Any

import requests
import pymysql

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
}

# 域名
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=0%2C0&fp=detail&logid=9498582126123275256&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=0&lpn=0&st=-1&word=%E9%B8%9F&z=0&ic=0&hd=0&latest=0&copyright=0&s=undefined&se=&tab=0&width=&height=&face=undefined&istype=2&qc=&nc=&fr=&simics=&srctype=&bdtype=0&rpstart=0&rpnum=0&cs=2937201382%2C2515441350&catename=&nojc=undefined&album_id=&album_tab=&cardserver=&tabname=&pn=0&rn=30&gsm=1&1663057266052='
response = requests.get(url, headers=headers)
p_url = response.json()['data']

for i in range(30):
    m = p_url[i]['hoverURL']
    res = requests.get(url=m, headers=headers)
    loc: Union[str, Any] = 'pictures\\' + m[29:36] + '.jpeg'
    with open(loc, mode='wb') as f:
        f.write(res.content)

    # 连接数据库
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306, user='root',
        passwd='yxc',
        db='srtp',
        charset='utf8',
        use_unicode=True,
    )

    # 创建游标
    cursor = conn.cursor()

    sql = "INSERT INTO pictures (images_location, category) VALUES (%s, 'birds')"
    cursor.execute(sql, loc)    # 写入地址和类别

    # 提交
    conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()