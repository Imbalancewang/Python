def leap_year(year):
    if year%4==0 and year%100!=0:
        return 1
    elif year%100==0 and year%400==0:
        return 1
    else:
        return 0

def judge(day,month,year):
    monthday=(0,31,59,90,120,151,181,212,243,273,304,334)
    ss=monthday[month-1]+day+leap_year(year)
    print ss

year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))
judge(day,month,year)
