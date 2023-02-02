# یک تابعی به نام  avglenghبنویسید که یک رشته حاوي یک جمله انگلیسی را دریافت کند و میانگین طول کلمات آنرا
# برگرداند، بدیهی است که علائم نگارشی نظیر . : ؟ ! ، کلمه محسوب نمی شون  


txt = 'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.'



# def avglengh(txt : str ) :
my_d = {}
my_l = []
for item in txt.split() :
    my_d[item] = txt.count(item) 

for i in my_d : 
    my_l.append( i )


