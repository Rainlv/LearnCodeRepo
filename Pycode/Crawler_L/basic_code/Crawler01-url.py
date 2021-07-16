import urllib.request
import urllib.parse
import json
import easygui as g

url = 'http://fanyi.youdao.com/translate'

content = g.enterbox(msg='请输入要翻译为英文的语句',title='中译英')

data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15809778682506'
data['sign'] = 'ec983824f7047deb88dc8adcf2541ff9'
data['ts'] = '1580977868250'
data['bv'] = '901200199a98c590144a961dac532964'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTlME'
data = urllib.parse.urlencode(data).encode('utf-8')

# header = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
# }

res = urllib.request.urlopen(url,data)
html = res.read().decode('utf-8')

trans = json.loads(html)
result = trans['translateResult'][0][0]['tgt']

g.msgbox(msg='{}的英文翻译为{}'.format(content,result))