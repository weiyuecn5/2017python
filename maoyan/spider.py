import requests
import re
import json
from multiprocessing import Pool
def get_html(url):
    data = requests.get(url)
    if data.status_code == 200:
        return data.text
    return None
def get_content(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time' :item[4].strip()[5:],
            'score':item[5]+item[6]
        }
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_html(url)
    for item in get_content(html):
        print(item)
        write_to_file(item)
if __name__ == '__main__':
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])
    pool.close()
    pool.join()