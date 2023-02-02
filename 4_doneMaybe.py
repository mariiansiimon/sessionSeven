#  تابعی به نام  firstUCharبنویسید که یک رشته متنی را بعنوان ورودي بگیرد و اولین کاراکتر غیرتکراري آنرا یافته و
# اندیس آن در رشته متنی را برگرداند، درصورتیکه چنین کاراکتري را پیدا نکرد عدد منفی یک را برگرداند


sentences = 'all cops are bastard, all cats are beautiful'

# ef firstUchar( sentence : str ):


my_d = {}
for i in sentences :
    res = sentences.count(i)
    my_d[ i ] = res
# print( my_d )

for i in my_d :
    if my_d[i] == 1:
        print(i)
        sentences.index( i )
