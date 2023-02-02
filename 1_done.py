# یک تابعی به نام reverseبنویسید که یک رشته حاوي عدد (مثبت یا منفی) را دریافت کند و معکوس آنرا برگرداند 
# 1234 -> 4321
# -2456 -> -6542




def cal_reverse( num : str ) :
    if num[0] == '-' :
        return print( num[0] + num[:0:-1] )
    else :
        return print( num[::-1] )


cal_reverse( '-2456' )