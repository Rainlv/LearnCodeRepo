import re

# with open('movie_download.txt','r',encoding='utf-8') as r:
#     lines = r.readlines()
#     last_line = lines[-1]
#     # last_line.replace('\n','')
#     # print(last_line)
#     page_num = re.match(r'\*{20}以上为第(\d{2,3})页内容\*{20}',last_line)
#     page_num = page_num.group(1)
#     print(int(page_num))


with open(r'img\195XX109_2020010925849241.jpg','rb') as r:
    s = r.read()
    print(s)