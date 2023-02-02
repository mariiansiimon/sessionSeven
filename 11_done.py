# تابعی بنویسید که یک عدد بگیرد و تعیین کند که آیا این عدد توان کامل است یا نه؟


def tavan( num ):
    s = 1 
    for i in range(1, num + 1 ):
        if num % i == 0:
            s += 1

    if num == s :
       return print(True) 
    else:
       return print(False)            


tavan(12)
tavan(4)