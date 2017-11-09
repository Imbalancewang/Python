def format_duration(seconds):
    if seconds == 0: return "now"
    origin = seconds
    dic = {
        'year': 60 * 60 * 24 * 365,
        'day': 60 * 60 * 24,
        'hour': 60 * 60,
        'minute': 60,
        'second': 1
    }
    spent = {}
    ans = ""
    for x in ['year','day','hour','minute','second']:
        spent[x] = seconds // dic[x]
        ans += "{}{} {}{}".format('' if seconds == origin else ' and ' if seconds % dic[x] == 0 else ', ',spent[x],x,'s' if spent[x] > 1 else '') if spent[x] > 0 else ''
        seconds %= dic[x]
    return  ans
print format_duration(38945)