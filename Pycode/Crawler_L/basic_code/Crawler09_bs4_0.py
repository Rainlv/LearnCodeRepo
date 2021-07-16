from bs4 import BeautifulSoup

text = '''
    <table id="ip_list">
    <tr>
      <th class="country">国家</th>
      <th>IP地址</th>
      <th>端口</th>
      <th>服务器地址</th>
      <th class="country">是否匿名</th>
      <th>类型</th>
      <th class="country">速度</th>
      <th class="country">连接时间</th>
      <th width="8%">存活时间</th>
      
      <th width="20%">验证时间</th>
    </tr>
  
    <tr class="odd">
      <td class="country"><img src="//fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>
      <td>114.226.89.147</td>
      <td>9999</td>
      <td>
        <a href="/2020-02-08/jiangsu">江苏常州</a>
      </td>
      <td class="country">高匿</td>
      <td>HTTPS</td>
      <td class="country">
        <div title="0.525秒" class="bar">
          <div class="bar_inner fast" style="width:93%">
            
          </div>
        </div>
      </td>
      <td class="country">
        <div title="0.105秒" class="bar">
          <div class="bar_inner fast" style="width:95%">
            
          </div>
        </div>
      </td>
      
      <td>1分钟</td>
      <td>20-02-08 15:00</td>
    </tr>
  
    <tr class="">
      <td class="country"><img src="//fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>
      <td>223.241.119.222</td>
      <td>9999</td>
      <td>
        <a href="/2020-02-08/anhui">安徽</a>
      </td>
      <td class="country">高匿</td>
      <td>HTTPS</td>
      <td class="country">
        <div title="0.484秒" class="bar">
          <div class="bar_inner fast" style="width:94%">
            
          </div>
        </div>
      </td>
      <td class="country">
        <div title="0.096秒" class="bar">
          <div class="bar_inner fast" style="width:97%">
            
          </div>
        </div>
      </td>
      
      <td>1分钟</td>
      <td>20-02-08 15:00</td>
    </tr>
  <p class = 'odd'>
    <a>
      测试段落
    </a>
  </p>
'''

""" 
# print(text)
bs = BeautifulSoup(text,'lxml')     # text指定文档，'lxml'指定解析器
# 解析器 'lxml' 'html5lib' 等等
# print(type(bs))  # 打印出来的是文本内容,bs是一个类文本的bs对象
print(bs.prettify()) # 美化代码 """



bs = BeautifulSoup(text,'lxml')

def get_tr():   # 获取所有tr标签
    
    def find():
        trs = bs.find_all('tr')
        # print(type(trs))      #   类似列表的对象
        # print(trs)

        for tr in trs:
            print(tr)   #   类似字符串的对象，包含tr标签内所有内容
    def css():
        trs = bs.select('tr')

        for tr in trs:
            print(tr)

# 获取第二个tr标签
def get_secTr():

    def find():
        tr = bs.find_all('tr',limit=2)[1]  # limit 参数设置最多获取数量，获取第二个tr没用专门的bs4方法，通过列表操作获得
        print(tr)
    def css():
        tr = bs.select('tr')[1]  
        print(tr)


# 获取class是odd的tr标签
def get_tr_odd():

    def find():
        # trs = bs.find_all('tr',class_ = 'odd')  # way1
        trs = bs.find_all('tr',attrs= {'class':'odd'})  #way2  两种方法都可以成功获取
        # print(trs)
        for tr in trs:
            print(tr)

    def css():
        trs = bs.select('.odd')  # 选择所有类为odd的元素
        trs = bs.select('tr.odd')   # 选择所有类为odd的tr元素
        # trs = bs.select("tr[class = 'odd']")    # 与上一行等价
        for tr in trs:
            print(tr)
    
    # css()

# get_tr_odd()

# 获取title和class都有值的div标签

def get_div():  # 多条件过滤
    # div_list = bs.find_all('div',title="0.105秒",class_="bar" )
    div_list = bs.find_all('div',attrs={'title': '0.105秒','class':'bar'} )
    # print(div_list) 
    for div in div_list:
        print(div)

        # css选择器无法实现，只能过滤一个值

# 获取a标签下的href属性
def get_href():
    alist = bs.find_all('a')
    for a in alist:
        #   way1
        href = a['href']
        print(href)
        #   way2 attrs属性
        href = a.attrs['href']
        print(href)



def get_words():

    # .content 返回某个标签下的直接子元素，包括字符串，返回的是列表
    # .children 返回某个标签下的直接子元素，包括字符串，返回的是列表迭代器
    # 标签中直接字符子元素获取可用.string 返回的是文本，没有文本返回None
    # 获取标签下所有标签包含的文本.strings 返回的是生成器，可转列表
    # 获取标签下所有标签包含的文本.text() 返回的是文本
    # 获取标签下所有标签包含的非空白文本（自动删空白，如\n）.stripped_strings 返回的是生成器，可转列表
   
    def test_contents():  # .contents
      p = bs.select('p')[0]
      content = p.contents
      print(content)
      
    test_contents()

    # 获取ip地址及端口号
    def get_ip_port():  # .string，

        trs = bs.find_all('tr')[1:] # 过滤掉第一个标题tr

        for tr in trs:
            tds = tr.find_all('td')
            ip = tds[1].string  # .string方法获取标签内的文本，只能获取单行字符，相当于xpath的text()
            port = tds[2].string
            print(ip + ':' + port)
 

    # 获取tr标签下所有非标签文本
    def get_infos():   # .strings

        trs = bs.find_all('tr')[1:]
        for tr in trs:
            infos = tr.strings # 返回值是一个生成器对象
            infos = list(infos)
            print(infos) # 存在较多换行


    # 获取tr标签下所有非标签飞空文本
    def get_uns_infos():  # .stripped_strings
        trs = bs.find_all('tr')[1:]
        for tr in trs:
            infos = tr.stripped_strings  # 返回非空元素，返回值是生成器
            infos = list(infos)
            print(infos)


    def get_str_infos():   # .get_text()
        trs = bs.find_all('tr')[1:]
        for tr in trs:
            infos = tr.get_text()  # 返回所有元素（含空字符），返回值是文本
            print(infos)

get_words()