# تابعی بنویسید که سه نقطه در فضای دو بعدی بگیرد و تعیین کند که آیا این سه نقطه همراستا هستند یا نه؟
# در مسئله قبل اگر نقاط همراستا نیستند نوع مثلث تشکیل شده را تعیین کنن
# (متساوی الاضلاع یا متساوی الثاقین یا قائم الزاویه یا معمولی)

import math 

def trian(a, b, c):
    
    mAB = b[1] - a[1] / b[0] - a[0]
    mAC = c[1] - a[1] / c[0] - a[0]

    if mAB == mAC :
        print('Three points are in same direction')

    else:
        dAB = math.dist( (a[0], a[1]), (b[0], b[1]) )
        dBC = math.dist( (b[0], b[1]), (c[0], c[1]) )
        dCA = math.dist( (c[0], c[1]), (a[0], a[1]) )
         
        if dAB == dBC == dCA :
            print('Type of triangle is :  Mosaviolazla')    

        elif dAB == dBC or dAB == dCA or dBC == dCA :
            print('Type of triangle is : Motesaviolsaghein : ')
        
        elif pow(dAB, 2) == pow(dBC, 2) + pow(dCA, 2) or pow(dBC, 2) == pow(dAB, 2) + pow(dCA, 2) or pow(dCA, 2) == pow(dAB, 2) + pow(dBC, 2) :
            print('Type of triangle is : Ghaemolzavieh ')

        else:
            print(' Just a poor triangle!!!')



t1 = trian((6, 12), (10, 7), (3, 5))
t2 = trian((4, 4), (6, 3), (1, 3))
t3 = trian((-2, 0), (2, 0), (1, 4))