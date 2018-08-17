import requests
from bs4 import BeautifulSoup
import time
import random
import xlwt

def get_page():
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')  # 当前表的名字
    ws.write(0, 0, '小区')
    ws.write(0, 1, '构造')
    ws.write(0, 2, '面积')
    ws.write(0, 3, '价格')
    ws.write(0, 4, '方位')
    ws.write(0, 5, '修饰')
    ws.write(0,6,'面积数字')
    # city=['jn','cs','sh','bj','cd','sz','cq','lf','nj','sy','xa','zz','zh','dl','fs','hf','xm','hk']#济南 长沙 上海 北京 成都  深圳 重庆 廊坊 南京 沈阳 西安 郑州  珠海 大连 佛山  合肥 厦门 海口
    # for i in range(3,18):
    #     print('这是%s'%city[i])
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    j=1
    for c in range(1,2):
        # url_page='https://m.lianjia.com/'+str(city[c])+'/zufang/pg'
        try:
            for k in range(0,100):
                url='https://m.lianjia.com/cs/zufang/pg'+str(k)+'/?_t=1'#一页23户 13468 585
                print(url)
                res=requests.get(url,headers=headers,timeout=5).text
                # print(res)
                html=BeautifulSoup(res,'lxml')
                try:
                    wheres=html.find_all('div','item_other text_cut')
                    whichs=html.find_all('div','item_minor')
                    hows=html.find_all('div','item_main')
                    # print(hows)
                    # print(whichs)
                    # print(wheres)
                    for i in range(len(wheres)):
                        xiushi = hows[i].text#修饰
                        jiage=(whichs[i].text).split('元')[0]#价格 筛去了\月
                        list=(wheres[i].text).split('/')
                        print(xiushi)
                        print(jiage)
                        for i in range(4):
                            print(list[i])#构造 面积 方位 名字
                        shuzi=(list[1]).split('m')[0]
                        print(shuzi)#单纯的为了好计算将平方米的数字提取出来了。
                        print()
                        ws.write(j, 0, list[3])
                        ws.write(j, 1, list[0])
                        ws.write(j, 2, list[1])
                        ws.write(j, 3, jiage)
                        ws.write(j, 4, list[2])
                        ws.write(j, 5, xiushi)
                        ws.write(j, 6, shuzi)
                        j=j+1
                    wb.save('链家网租房-长沙.xls')
                    rtime=float(random.randint(1,100)/20)
                    print("请让我休息%d秒钟"%rtime)
                    print("接下来将要爬取长沙第%d页"%(k+1))
                    time.sleep(rtime)
                except:
                    pass
        except:
            pass



    # print(j)

if __name__=='__main__':
    get_page()