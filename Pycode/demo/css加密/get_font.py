# reference：https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484921&idx=1&sn=72a707c5bc67eede144947829cab4dc6&chksm=fc8bbd68cbfc347eca6727ff90f85ef58a4fdd7c2f75a962aee3ccd5e9c4266dbe5f4e6e2262&scene=27#wechat_redirect
import pytesseract
import requests
import re
from fontTools.ttLib import TTFont
import os
import matplotlib.pyplot as plt
from PIL import Image

URL = 'https://maoyan.com/board/1'
RAW_HEADERS = '''
Referer: https://maoyan.com/board/1
User-Agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50
'''
FONT_DOMAIN = 'http://vfile.meituan.net/colorstone/'

def dict_header(header):
    new_header = {}
    header_list = header.split('\n')
    for item in header_list:
        if item:
            key = item[:item.find(":")]
            value = item[item.find(":") + 2:]
            new_header[key] = value
    return new_header


def download_html(url):
    res = requests.get(url, headers=dict_header(RAW_HEADERS))
    if res.status_code == 200:
        return res


def get_font(url):
    save_dir_font = 'font/'
    save_dir_num = 'num/'

    # 解析页面源代码
    html = download_html(url).text

    # 获取font文件url
    font_file_name = re.findall(r'//vfile.meituan.net/colorstone/(\w+\.woff)', html)[0]
    font_url = FONT_DOMAIN + font_file_name
    font_file = download_html(font_url)

    # 下载font文件
    if not os.path.exists(os.path.join(os.path.abspath('.'), save_dir_font)):
        os.mkdir(save_dir_font)
    with open(save_dir_font + font_file_name, 'wb') as w:
        w.write(font_file.content)

    # 解析字体文件
    font = TTFont('font/' + font_file_name)
    font.saveXML('font/ ' + font_file_name + '.xml')

    font_code_list = font.getGlyphNames()[1:]

    x = [i[0] for i in font['glyf'][font_code_list[0]].coordinates]
    y = [i[1] for i in font['glyf'][font_code_list[0]].coordinates]

    plt.plot(x, y)

    frame = plt.gca()
    # y 轴不可见
    frame.axes.get_yaxis().set_visible(False)
    # x 轴不可见
    frame.axes.get_xaxis().set_visible(False)

    if not os.path.exists(os.path.join(os.path.abspath('.'), save_dir_num)):
        os.mkdir(save_dir_num)

    img_path = save_dir_num + font_file_name.replace('.woff', '.png')

    plt.savefig(img_path)
    plt.show()

    num = Image.open(img_path)
    result = pytesseract.image_to_string(num, config='--psm 10' 'digits')
    print(result)


if __name__ == '__main__':
    get_font(URL)
