import urllib.request
import easygui as g
import re


def url_open(url):
    # http://pic.ali213.net/
    req = urllib.request.Request(url)
    req.add_header =  [
    ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
    ,('Accept-Encoding','gzip, deflate, br')
    ,('Accept-Language','zh-CN,zh;q=0.9')
    ,('Cache-Control','max-age=0')
    ,('Connection','keep-alive')
    ,('Cookie','Hm_lvt_18a964a3eb14176db6e70f1dd0a3e557=1580211059; _xsrf=2|5a4ecde5|a5121c2a4185f087fb510a7c45c736fd|1581050890; BAIDU_SSP_lcr=https,//www.baidu.com/s?wd=%E5%97%85%E4%BA%8B%E7%99%BE%E7%A7%91&rsv_spt=1&rsv_iqid=0xe35144a200040412&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=&tn=baiduhome_pg&ch=&rsv_enter=1&rsv_dl=ib&inputT=2535; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1580211059,1581050892; _ga=GA1.2.1137258785.1581050892; _gid=GA1.2.1997717800.1581050892; __cur_art_index=7400; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1581050969')
    ,('Host','www.qiushibaike.com')
    ,('If-None-Match','"b8e8fe33484614412d83d8a07bd4e0e3cbef6378"')
    ,('Referer','https,//www.qiushibaike.com/?x')
    ,('Sec-Fetch-Mode','navigate')
    ,('Sec-Fetch-Site','same-origin')
    ,('Sec-Fetch-User','?1')
    ,('Upgrade-Insecure-Requests','1')
    ,('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
    ]
    html = urllib.request.urlopen(req)
    return html
    # print(html)


def get_pic_path(url):
    html = url_open(url).read().decode('utf-8')
    img_path_list = re.findall(r"<img src='.+?'",html)
    # print(img_path_list)
    img_url = []
    for img_path in img_path_list:
        img_path = re.search(r"<img src='(.+?)'",img_path)
        img_path = 'http:'+img_path.group(1)
        img_url.append(img_path)
    return img_url

def download_pic(path):
    for each_img in path:
        html = url_open(each_img)
        html = html.read()
        filename = each_img.split('/')[-1]
        with open(r'E:\Code\Pycode\img\{}'.format(filename),'wb') as w:
            w.write(html)
        # write()函数必须写入str类型
        # read()读出来的是bytes类型
        # bytes-->decode-->str
        # str -->encode -->bytes


# url = g.enterbox(msg='输入要爬图片的网站地址：',title='网页图片爬取工具：')
url = 'http://pic.ali213.net/'


download_pic(get_pic_path(url))