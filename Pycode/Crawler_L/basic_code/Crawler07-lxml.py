from lxml import etree


# response.xpath('//div[contains(@class,"abc")]') 找到包含abc类的div标签

# 直接解析字符串
def parse_text():
    text = '''
        <div id="wrapper">
        <div id="header">
        <h1>国内高匿代理IP</h1>
        <img alt="免费http代理" id="logo" src="//fs.xicidaili.com/images/logo.png" />
        <div id="myurl">
            XiciDaili.com
        </div>
        <ul id="nav">
            <li><a class="false" href="/">首页</a></li>
            <li><a href="/api">API提取</a></li>
            <li><a class="active" href="/nn/">国内高匿代理</a></li>
            <li><a class="false" href="/nt/">国内普通代理</a></li>
            <li><a class="false" href="/wn/">国内HTTPS代理</a></li>
            <li><a class="false" href="/wt/">国内HTTP代理</a></li>
            <li><a class="false" href="/articles/">代理小百科</a></li>
        </ul>
        </div>
        <div id="body" class="clearfix proxies">
    '''

    htmlElem = etree.HTML(text)  # 返回的是对象，会对html代码自动纠错补全
    html = etree.tostring(htmlElem, encoding='utf-8').decode()
    print(html)


# 文件读取 解析
def parse_file():
    parser = etree.HTMLParser(encoding='utf-8')  # 创建一个html解析器
    htmlEle = etree.parse(r'Crawler_L\proxy.html', parser=parser)
    html = etree.tostring(htmlEle, encoding='utf-8').decode()
    print(html)


# html标签获取
def get_tr():
    parser = etree.HTMLParser(encoding='utf-8')
    htmlEle = etree.parse(r'Crawler_L\proxy.html', parser=parser)

    # tr标签获取
    def get_AllTr():
        trs = htmlEle.xpath("//tr")  # 返回的是对象列表
        for tr in trs:
            print(tr)
            print(etree.tostring(tr, encoding='utf-8').decode())  # 读取对象内容，返回为字符串

    # 获取第二个tr标签
    def get_SecondTr():
        trs = htmlEle.xpath('//tr[2]')[0]  # 返回的是列表，用序列号提取内容
        print(etree.tostring(trs, encoding='utf-8').decode())

    # 获取第二个后的tr标签
    def get_UpSecondTr():
        trs = htmlEle.xpath('//tr[position()>2]')[0]  # position 参数
        print(etree.tostring(trs, encoding='utf-8').decode())

    # 获取带有类属性的tr标签
    def get_trClass():
        trs = htmlEle.xpath("//tr[@class='odd']")
        for tr in trs:
            print(etree.tostring(tr, encoding='utf-8').decode())


# 获取a标签的href属性
def get_aHref():
    parser = etree.HTMLParser(encoding='utf-8')
    htmlEle = etree.parse(r'Crawler_L\proxy.html', parser=parser)

    a_hrefs = htmlEle.xpath('//a/@href')  # 获取属性值的写法,返回的是字符串，不用再tostring
    for a_href in a_hrefs:
        print(a_href)


# 获取标签内内容，实操
def get_ip():  # a.text也可
    parser = etree.HTMLParser(encoding='utf-8')
    htmlEle = etree.parse(r'Crawler_L\proxy.html', parser=parser)

    tableElm = htmlEle.xpath('//table[@id="ip_list"]')[0]
    # table = etree.tostring(tableElm,encoding='utf-8')
    trs = tableElm.xpath(".//tr[@class='odd' or @class='']")  # xpath语法.//tr表示在上级目录下的tr
    list_ip_port = []
    for tr in trs:
        ip = tr.xpath(".//td[2]/text()")[0]  # .//td[not(@class)}]表示目录下没有class属性的td标签
        port = tr.xpath(".//td[3]/text()")[0]  # .//td[3]/text() 返回td[3]标签下的文本内容 返回类型是列表
        address = tr.xpath('.//td[4]/a/text()')[0]
        # print(address)
        time = tr.xpath('.//td[last()-1]/text()')[0]  # xpath表示序列号没有[-1]的表示法，表示最后一个用[last()]，倒数第二个[last()-1]
        print(time)
        list_ip_port.append(ip + ':' + port)
        break
    # print(list_ip_port)
