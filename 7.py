'''
 تابعی به نام  fillNoneبنویسید که اعضاي خالی در جدول را با عدد قبلی آن جایگزین کند، اولین عضو اگر خالی بود با
صفر جایگزین شود:

input: [1,None,2,None,4,None,4,5,None] output: [1,1,2,2,4,4,4,5,5]
'''

m = [1,None,2,None,4,None,4,5,None]


for i in m: 
    if type(i) == None :
        
      d =  m.insert(i, m[i] )

print(d)

