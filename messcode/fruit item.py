width=input('please input the width:')
price_width=10
item_width=width-price_width
header_format='%-*s%*s'
format=       '%-*s%*.2f'
print '='*width
print header_format%(item_width,'item',price_width,'price')
print '='*width
print format %(item_width,'Apples',price_width,0.4)
print format %(item_width,'pears',price_width,0.5)
print format %(item_width,'can',price_width,1.92)
print format %(item_width,'peach',price_width,8)
print format %(item_width,'prunes',price_width,12)
print '='*width
