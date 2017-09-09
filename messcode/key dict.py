phonebook={'alice':{'phone':'3213','add':'fsd'},
           'beth':{'phone':'321','add':'dasdas'}}
name=raw_input('input the name:')
label={'phone':'phone number','add':'address'}
req=raw_input('phone number(p) or address (a):')
if req==p :key='phone'
if req==a :key='add'
print "%s's %s is %s."%(name.label[key],phonebook[name][key])
