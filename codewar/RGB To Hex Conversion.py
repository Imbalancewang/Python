def rgb(r, g, b):
    #your code here :)
    str,strr,strg,strb='','','',''
    if r>=0 and r<256:
        strr=hex(r)[-2:].upper()
    elif r<0:
        strr='00'
    else:
        strr='FF'
    if g>=0 and g<256:
        strg=hex(g)[-2:].upper()
    elif g<0:
        strg='00'
    else:
        strg='FF'
    if b>=0 and b<256:
        strb=hex(b)[-2:].upper()
    elif b<0:
        strb='00'
    else:
        strb='FF'
    str=(strr+strg+strb).replace('X','0')
    return str
print rgb(-20,275,125)