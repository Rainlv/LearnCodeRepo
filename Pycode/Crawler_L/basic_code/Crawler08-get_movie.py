import requests
from lxml import etree
import Crawler00_get_proxy
from requests import exceptions
import re
# import time

# times = 36

def get_htmlElm(url):
    try:
        html = requests.get(url,headers=headers,proxies=proxy,timeout=15)
        html = html.content.decode('gbk')
        htmlElm = etree.HTML(html)
        return htmlElm
    except exceptions.Timeout:
        return None
    except Exception as e:
        print(e)
        return None

def get_moviePage(url):

    # 获取当前页下的详情页
    proxy = Crawler00_get_proxy.generate_proxy()

    url_domain = 'https://www.ygdy8.net'
    try:
        html = requests.get(url,headers=headers,proxies=proxy,timeout=10)
        html = html.text
        html = etree.HTML(html)

    except:
        print('获取详情页超时，重新获取中')
        get_moviePage(url)

    if html is not None:

        tableElm = html.xpath('//table[@class = "tbspan"]')

        mLink_list = []
        for table in tableElm:

            link = table.xpath('./tr[2]//a/@href')[0]
            # print(link)
            movie_link = url_domain + link

            mLink_list.append(movie_link)

        return mLink_list
    
    else:
        return None

# print(get_moviePage(url))

def get_download_url(url,times):
    # global times

    result_list = {}

    try_times = 0

    if get_moviePage(url) is not None:

        # times += 1

        for movie_page in get_moviePage(url):
            
            pageElm = get_htmlElm(movie_page)
            if  pageElm is not None:
                # try:
                # 获取电影标题
                try:
                    title = pageElm.xpath('//h1//text()')[0]
                except Exception as e:
                    print(e)
                    continue
                # print(title)
                # 获取下载链接
                
                # print(download_magnetUrl)
                try:
                    download_magnetUrl = pageElm.xpath('//p/a/@href')[0]
                except IndexError:
                    try:
                        td = pageElm.xpath('//td[@style="WORD-WRAP: break-word"]')[1]
                        try:
                            download_magnetUrl = td.xpath('.//a/@href')[0]
                        except TypeError:
                            download_magnetUrl = td.xpath('.//a/@href')
                        except Exception as e:
                            print('0')
                            print(e)
                        if not download_magnetUrl.startswith('magnet','ftp'):
                            raise IndexError
                    except IndexError:
                        try:
                            td = pageElm.xpath('//td[@style="WORD-WRAP: break-word"]')[0]
                            download_magnetUrl = td.xpath('.//a/@href')[0]
                        except:
                            print('1')
                            print('出现错误，跳过')
                            continue
                    except Exception as e:
                        print('2')
                        print(e)
                        print('出现错误，跳过')
                        continue
                except Exception as e:
                    print('3')
                    print(e)
                    print('出现错误，跳过')
                    continue

                result_list[title] = download_magnetUrl + '\n' 

                # print(result_list)

                print(title+'   爬取完成')
                # except Exception as e :
                #     print(e)
                #     continue
            else:
                print('连接超时，跳过')
                continue
        
        else:
            print('*'*50)
            print('第{}页爬取完成'.format(times))
            print('*'*50)
        
    else:
        try_times += 1
        if try_times > 5:
            result_list = {}
        else:
            print('获取详情页失败')
            print('尝试重新获取详情页')
            print('第{}次尝试......'.format(try_times))
            proxy = Crawler00_get_proxy.generate_proxy()
            get_download_url(url,times)

    return result_list
       
    

def save_magent(url,times):
    with open('movie_download.txt','a',encoding='utf-8') as w:
        for key,value in get_download_url(url,times).items():
            w.writelines(key + ':\t' + value + '\n')
        else:
            w.writelines('*'*20 + '以上为第{}页内容'.format(times) + '*'*20 + '\n')



def get_page_num():
    with open('movie_download.txt','r',encoding='utf-8') as r:
        lines = r.readlines()
        last_line = lines[-1]
        # last_line.replace('\n','')
        # print(last_line)
        page_num = re.match(r'\*{20}以上为第(\d{2,3})页内容\*{20}',last_line)
        page_num = page_num.group(1)
        return int(page_num)


if __name__ == "__main__":

    proxy = Crawler00_get_proxy.generate_proxy()

    headers = {
            'Referer': 'https://www.ygdy8.net/html/gndy/dyzz/list_23_2.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

    start_num = get_page_num() + 1 

    for page_num in range(start_num,211):

        times = page_num

        url = 'https://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'.format(page_num)
        try:
            save_magent(url,page_num)
        except:
            save_magent(url,page_num)
    else:
        print('所有信息爬取完成')
