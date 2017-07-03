#__author__:keal
#-*-coding:utf-8 -*-

import requests
import json
import xlsxwriter
import string

proxies={'http':'http://122.6.116.84:808'}

url='https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
headers={
'Host': 'www.lagou.com',
'Connection': 'keep-alive',
'Content-Length': '26',
'Origin': 'https://www.lagou.com',
'X-Anit-Forge-Code': '0',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'X-Requested-With': 'XMLHttpRequest',
'X-Anit-Forge-Token': 'None',
'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
'Cookie': 'user_trace_token=20170601035057-76af2a67-463a-11e7-9586-5254005c3644; LGUID=20170601035057-76af2d90-463a-11e7-9586-5254005c3644; X_HTTP_TOKEN=2c90d08c59ee5298a27757e6c27b3244; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=ABAAABAAAGFABEF3EA3296E1B04B41C1AC8761D92807D17; SEARCH_ID=1f1de7d9bddf416582daa397394e9a2a; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%2598%25AF%25E6%2598%25AF%25E8%2590%25A8%25E8%25BE%25BE%25E5%2593%2587%25E5%25AE%2589%25E6%258A%259A%25E9%2598%25BF%25E8%2590%25A8%25E5%25BE%25B7%25E9%2598%25BF%25E8%2590%25A8%25E5%25BE%25B7%25E9%2598%25BF%25E8%2590%25A8%25E8%2590%25A8%25E8%25BE%25BE%25E5%25B8%25A6%25E5%25A8%2583%25E6%2592%2592%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3Fcity%3D%25E5%25B9%25BF%25E5%25B7%259E%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; TG-TRACK-CODE=search_code; _putrc=FCA4D126584AAA0A; login=true; unick=%E8%B0%A2%E7%A7%91; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=23; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1498204523,1498206097,1498840190,1498916978; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1498999806; _gid=GA1.2.2014512842.1498840190; _ga=GA1.2.765344592.1496260244; LGSID=20170702204527-53360da1-5f24-11e7-bb9c-525400f775ce; LGRID=20170702205013-fd72c410-5f24-11e7-a15d-5254005c3644'
}


def get_lagou(res_url,page):
    post_data={'first': 'true', 'pn': page, 'kd': 'python'}
    json=requests.post(res_url,post_data,headers=headers,proxies=proxies).json()
    list=json['content']['positionResult']['result']
    info_list=[]
    for i in list:
        info=[]
        info.append(i['companyFullName'])
        info.append(i['companyLabelList'])
        info.append(i['companySize'])
        info.append(i['firstType'])
        info.append(i['positionAdvantage'])
        info.append(i['positionLables'])
        info.append(i['positionName'])
        info.append(i['salary'])
        info.append(i['secondType'])
        info_list.append(info)
    return info_list

def write_into_excel():
    #利用xlsxwriter创建excel表
    workbook=xlsxwriter.Workbook('lagou_python.xlsx')
    worksheet=workbook.add_worksheet()
    #存储所有页码爬取到的资料
    info_result=[]
    for i in range(1,7):
        info_current_page=get_lagou(url,i)
        info_result=info_result+info_current_page
    print(info_result)
    num_=1
    for item in info_result:
        col_A = 'A%s' % (num_)
        col_B = 'B%s' % (num_)
        col_C = 'C%s' % (num_)
        col_D = 'D%s' % (num_)
        col_E = 'E%s' % (num_)
        col_F = 'F%s' % (num_)
        col_G = 'G%s' % (num_)
        col_H = 'H%s' % (num_)
        col_I = 'I%s' % (num_)
        worksheet.write(col_A, item[0])
        worksheet.write(col_B, ','.join(item[1]))
        worksheet.write(col_C, item[2])
        worksheet.write(col_D, item[3])
        worksheet.write(col_E, item[4])
        worksheet.write(col_F, ','.join(item[5]))
        worksheet.write(col_G, item[6])
        worksheet.write(col_H, item[7])
        worksheet.write(col_I, item[8])
        num_+=1
    workbook.close()
if __name__ == '__main__':
    write_into_excel()
















