# برنامه ای بنویسید که محتوای یک فایل متنی را در فایل دیگری کپی کند.


f1 = open(r'D:\Extra\- User\Desktop\python\TahlilDadeh\Tamrin\session7\tamrin12first.txt', mode = 'r' )
f2 = open(r'D:\Extra\- User\Desktop\python\TahlilDadeh\Tamrin\session7\tamrin12second.txt', mode = 'a' )

for i in f1:
    f2.write( i )
f2.read()






f1.close()
f2.close()