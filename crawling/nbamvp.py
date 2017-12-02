# -*- coding: utf-8 -*-
# @Time    : 2017/12/2 21:21
# @Author  : Matthew
# @Site    : 
# @File    : nbamvp.py
# @Software: PyCharm Community Edition
import re,urllib,urllib2,urlparse,re,xlwt
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def download(url,user_agent='matthew',proxy=None,num_tries=2):
    print 'Downloading:',url
    headers = {'User_agent': user_agent}
    request=urllib2.Request(url,headers=headers)
    opener=urllib2.build_opener()
    if proxy:
        proxy_params={urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html=urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Downloading error:',e.reason
        html=None
        if num_tries>0:
            if hasattr(e,'code') and 500<=e.code<=600:
                return download(url,user_agent,num_tries-1)
    return html
def getData(url):
    FindSeason='<td class="current season change_color col0 row.*">(.*)</td>'
    FindPlayer='<td class="normal player_name_out change_color col1 row.*"><a target=.*>(.*)</a></td>'
    FindNBAABA='<td class="normal league change_color col2 row.*">(.*)</td>'
    FindChuchang='<td class="normal g change_color col3 row.*">(.*)</td>'
    FindShoufa='<td class="normal gs change_color col4 row.*">(.*)</td>'
    FindMins='<td class="normal mp change_color col5 row.*">(.*)</td>'
    FindShootingRate='<td class="normal fgper change_color col6 row.*">(.*)</td>'
    FindShootingNum='<td class="normal fg change_color col7 row.*">(.*)</td>'
    FindShootingSum='<td class="normal fga change_color col8 row.*">(.*)</td>'
    Find3ShootingRate='<td class="normal threepper change_color col9 row.*">(.*)</td>'
    Find3ShootingNum='<td class="normal threep change_color col10 row.*">(.*)</td>'
    Find3ShootingSum='<td class="normal threepa change_color col11 row.*">(.*)</td>'
    FindFoulRate='<td class="normal ftper change_color col12 row.*">(.*)</td>'
    FindFoulNum='<td class="normal ft change_color col13 row.*">(.*)</td>'
    FindFoulSum='<td class="normal fta change_color col14 row.*">(.*)</td>'
    FindReboundSum='<td class="normal trb change_color col15 row.*">(.*)</td>'
    FindReboundFront='<td class="normal orb change_color col16 row.*">(.*)</td>'
    FindReboundBehind='<td class="normal drb change_color col17 row.*">(.*)</td>'
    FindAssists='<td class="normal ast change_color col18 row.*">(.*)</td>'
    FindSteals='<td class="normal stl change_color col19 row.*">(.*)</td>'
    FindBlocks='<td class="normal blk change_color col20 row.*">(.*)</td>'
    FindTurnovers='<td class="normal tov change_color col21 row.*">(.*)</td>'
    FindFouls='<td class="normal pf change_color col22 row.*">(.*)</td>'
    FindPoints='<td class="normal pts change_color col23 row.*">(.*)</td>'
    html=download(url)
    datalist=[]
    Season=re.findall(FindSeason,html)
    Player=re.findall(FindPlayer,html)
    NBAABA=re.findall(FindNBAABA,html)
    Chuchang=re.findall(FindChuchang,html)
    Shoufa=re.findall(FindShoufa,html)
    Mins=re.findall(FindMins,html)
    ShootingRate=re.findall(FindShootingRate,html)
    ShootingNum=re.findall(FindShootingNum,html)
    ShootingSum=re.findall(FindShootingSum,html)
    ShootingRate3=re.findall(Find3ShootingRate,html)
    ShootingNum3=re.findall(Find3ShootingNum,html)
    ShootingSum3=re.findall(Find3ShootingSum,html)
    ReboundSum=re.findall(FindReboundSum,html)
    ReboundBehind=re.findall(FindReboundBehind,html)
    ReboundFront=re.findall(FindReboundFront,html)
    Assists=re.findall(FindAssists,html)
    Steals=re.findall(FindSteals,html)
    Blocks=re.findall(FindBlocks,html)
    Turnovers=re.findall(FindTurnovers,html)
    Fouls=re.findall(FindFouls,html)
    Points=re.findall(FindPoints,html)
    datalist.append(Season)
    datalist.append(Player)
    datalist.append(NBAABA)
    datalist.append(Chuchang)
    datalist.append(Shoufa)
    datalist.append(Mins)
    datalist.append(ShootingNum)
    datalist.append(ShootingRate)
    datalist.append(ShootingSum)
    datalist.append(ShootingRate3)
    datalist.append(ShootingSum3)
    datalist.append(ShootingNum3)
    datalist.append(ReboundSum)
    datalist.append(ReboundBehind)
    datalist.append(ReboundFront)
    datalist.append(Assists)
    datalist.append(Steals)
    datalist.append(Blocks)
    datalist.append(Turnovers)
    datalist.append(Fouls)
    datalist.append(Points)
    return datalist
def savedata(datalist,name):
    col=['Season','Player','NBAABA','Chuchuang','Shoufa','Mins','ShootingNum',
         'ShootingRate','ShootingSum','ShootingRate3','ShootingSum3',
         'ShootingNum3','ReboundSum','ReboundBehind','ReboundFront','Assists',
         'Steals','Blocks','Turnovers','Fouls','Points']
    book=xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet=book.add_sheet('NBA-data',cell_overwrite_ok=True)
    for i in range(len(col)):
        sheet.write(0,i,col[i])
    for i in range(len(datalist)):
        for j in range(len(datalist[0])):
            sheet.write(j+1,i,datalist[i][j])
    book.save(name)
if __name__ == '__main__':
    url='http://www.stat-nba.com/award/item0.html'
    datalist=getData(url)
    name='matthew.xlsx'
    savedata(datalist,name)
    print len(datalist[0])
    print len(datalist)



