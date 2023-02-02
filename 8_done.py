#  تابعی به نام  findMبنویسید که دوتا جمله را بصورت رشته متنی دریافت کند و کلمات مشترك آنها را برگرداند



def findM( sent1 : str, sent2 : str ) :

    my_l = []
    for item in sent1.split() :
        if item in sent2.split() :
            my_l.append( item )

    return print( my_l )

text1 = 'I am learning Python programming language'
text2 = 'I am going to learn machine learning'
findM(text1, text2)

