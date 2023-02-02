'''
تابعی به نام  movSefrبنویسید که یک لیست را بعنوان ورودي بگیرد و صفرهاي موجود در لیست را به انتهاي لیست
منتقل کند، بدون اینکه ترتیب سایر اعضاي آرایه بهم بخورد:

input: [1,0,3,4,0,0,7,5,0,6] output: [1,3,4,7,5,6,0,0,0,0]

'''

def movSefr(the_list : list ) :

    new_list = the_list.copy()

    for i in new_list :
        if i == 0 :
            d = new_list.remove(0)
            new_list.append(0)

    return print( new_list )


movSefr( [1,0,3,4,0,0,7,5,0,6] )