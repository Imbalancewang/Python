# -*- coding: utf-8 -*-
# @Time    : 2017/12/3 22:12
# @Author  : Matthew
# @Site    : 
# @File    : allplayers.py
# @Software: PyCharm Community Edition
#4613
import urllib2,urllib,urlparse,re,xlwt
import sys,time,socket
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
#socket.setdefaulttimeout(60)
def download(url,user_agent='matthew',proxy=None,num_tries=2):
    print 'Downloading:',url
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    headers={'User_agent':user_agent}
    request=urllib2.Request(url,headers=headers)
    opener=urllib2.build_opener()
    if proxy:
        proxy_params={urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html=urllib2.urlopen(request,timeout=60).read()
    except urllib2.URLError as e:
        if isinstance(e.reason,socket.timeout):
            print 'Downloading error:',e.reason,url
            return None
        print 'Downloading error:', e.reason
        html=None
        if num_tries>0:
            if hasattr(e,'code') and 500<=e.code<=600:
                return download(url,user_agent,num_tries-1)
    time.sleep(0.5)
    return html
def getData(url):
    html=download(url)
    if html==None:return ['']*30
    FindName='<div class="row"><div class="column">全　　名:</div>(.*)</div>'
    FindPosition='<div class="row"><div class="column">位　　置:</div>(.*)</div>'
    FindHeight='<div class="row"><div class="column">身　　高:</div>(.*)米.*</div>'
    FindWeight='<div class="row"><div class="column">体　　重:</div>(.*)公斤.*</div>'
    FindNormalseason='<td class="normal season" colspan="2">(.*)年</td>'
    FindNormaltm='<td class="normal tm">(.*)支</td>'
    FindNormalg='<td class="normal g">(.*)</td>'
    FindNormalgs='<td class="normal gs">(.*)</td>'
    FindNormalmp='<td class="normal mp">(.*)</td>'
    FindNormalfgper='<td class="normal fgper">(.*)</td>'
    FindNormalfg='<td class="normal fg">(.*)</td>'
    FindNormalfga='<td class="normal fga">(.*)</td>'
    FindNormalthreepper='<td class="normal threepper">(.*)</td>'
    FindNormalthreep='<td class="normal threep">(.*)</td>'
    FindNormalthreepa='<td class="normal threepa">(.*)</td>'
    FindNormalftper='<td class="normal ftper">(.*)</td>'
    FindNormalft='<td class="normal ft">(.*)</td>'
    FindNormalfta='<td class="normal fta">(.*)</td>'
    FindNormaltrb='<td class="normal trb">(.*)</td>'
    FindNormalorb='<td class="normal orb">(.*)</td>'
    FindNormaldrb='<td class="normal drb">(.*)</td>'
    FindNormalast='<td class="normal ast">(.*)</td>'
    FindNormalstl='<td class="normal stl">(.*)</td>'
    FindNormalblk='<td class="normal blk">(.*)</td>'
    FindNormaltov='<td class="normal tov">(.*)</td>'
    FindNormalpf='<td class="normal pf">(.*)</td>'
    FindNormalpts='<td class="normal pts">(.*)</td>'
    FindNormalw='<td class="normal w">(.*)</td>'
    FindNormall='<td class="normal l">(.*)</td>'
    datalist=[]
    Name=re.findall(FindName,html)
    Position=re.findall(FindPosition,html)
    Height=re.findall(FindHeight,html)
    Weight=re.findall(FindWeight,html)
    datalist.append(Name[0] if len(Name)>0 else '')
    datalist.append(Position[0] if len(Position)>0 else '')
    datalist.append(Height[0] if len(Height)>0 else '')
    datalist.append(Weight[0] if len(Weight)>0 else '')
    Normalseason=re.findall(FindNormalseason,html)
    Normaltm=re.findall(FindNormaltm,html)
    Normalg=re.findall(FindNormalg,html)
    Normalgs=re.findall(FindNormalgs,html)
    Normalmp=re.findall(FindNormalmp,html)
    Normalfgper=re.findall(FindNormalfgper,html)
    Normalfg=re.findall(FindNormalfg,html)
    Normalfga=re.findall(FindNormalfga,html)
    Normalthreepper=re.findall(FindNormalthreepper,html)
    Normalthreep=re.findall(FindNormalthreep,html)
    Normalthreepa=re.findall(FindNormalthreepa,html)
    Normalftper=re.findall(FindNormalftper,html)
    Normalft=re.findall(FindNormalft,html)
    Normalfta=re.findall(FindNormalfta,html)
    Normaltrb=re.findall(FindNormaltrb,html)
    Normalorb=re.findall(FindNormalorb,html)
    Normaldrb=re.findall(FindNormaldrb,html)
    Normalast=re.findall(FindNormalast,html)
    Normalstl=re.findall(FindNormalstl,html)
    Normalblk=re.findall(FindNormalblk,html)
    Normaltov=re.findall(FindNormaltov,html)
    Normalpf=re.findall(FindNormalpf,html)
    Normalpts=re.findall(FindNormalpts,html)
    Normalw=re.findall(FindNormalw,html)
    Normall=re.findall(FindNormall,html)
    datalist.append(Normalseason[0] if len(Normalseason)>0 else '')
    datalist.append(Normaltm[0] if len(Normaltm)>0 else '')
    datalist.append(Normalg[0] if len(Normalg)>0 else '')
    datalist.append(Normalgs[0] if len(Normalgs)>0 else '')
    datalist.append(Normalmp[0] if len(Normalmp)>0 else '')
    datalist.append(Normalfgper[0] if len(Normalfgper)>0 else '')
    datalist.append(Normalfg[0] if len(Normalfg)>0 else '')
    datalist.append(Normalfga[0] if len(Normalfga)>0 else '')
    datalist.append(Normalthreepper[0] if len(Normalthreepper)>0 else '')
    datalist.append(Normalthreep[0] if len(Normalthreep)>0 else '')
    datalist.append(Normalthreepa[0] if len(Normalthreepa)>0 else '')
    datalist.append(Normalftper[0] if len(Normalftper)>0 else '')
    datalist.append(Normalft[0] if len(Normalft)>0 else '')
    datalist.append(Normalfta[0] if len(Normalfta)>0 else '')
    datalist.append(Normaltrb[0] if len(Normaltrb)>0 else '')
    datalist.append(Normalorb[0] if len(Normalorb)>0 else '')
    datalist.append(Normaldrb[0] if len(Normaldrb)>0 else '')
    datalist.append(Normalast[0] if len(Normalast)>0 else '')
    datalist.append(Normalstl[0] if len(Normalstl)>0 else '')
    datalist.append(Normalblk[0] if len(Normalblk)>0 else '')
    datalist.append(Normaltov[0] if len(Normaltov)>0 else '')
    datalist.append(Normalpf[0] if len(Normalpf)>0 else '')
    datalist.append(Normalpts[0] if len(Normalpts)>0 else '')
    datalist.append(Normalw[0] if len(Normalw)>0 else '')
    datalist.append(Normall[0] if len(Normall)>0 else '')
    return datalist
def ExcelWrite(datalist,name):
    col=['Name','Position','Height','Weight','Career','Team','Game',
         'First Publish','TimeAve','ShootingRateAve','HitAve',
         'NumberofhandsAve','ThreeRateAve','ThreeHitAve','ThreeNumAve',
         'FoulRateAve','FoulHitAve','FoulNumAve','ReboundsAve','OffRebAve',
         'DefRebAve','AssistsAve','StealAve','BlockAve','TurnoverAve',
         'PersonalFoulAve','PointsAve','WinSum','LoseSum']
    book=xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet=book.add_sheet('NBA-data',cell_overwrite_ok=True)
    for i in range(len(col)):
        sheet.write(0,i,col[i])
    for i in range(len(datalist)):
        for j in range(len(datalist[0])):
            sheet.write(i+1,j,datalist[i][j])
    book.save(name)
if __name__ == '__main__':
    name='lucky.xlsx'
    start=time.time()
    data=[]
    for i in range(4300,4613):
        #if i%10==0:print i
        url = 'http://www.stat-nba.com/player/%d.html'%i
        temp=getData(url)
        data.append(temp)
    ExcelWrite(data,name)
    end=time.time()
    print end-start
