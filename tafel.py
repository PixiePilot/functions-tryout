def tafels():
    try:
        Tafel = (int)(input('van welk getal wilt u de tafel zien?: '))
    except ValueError:
        print('Please enter a number.')

        tafels()
    for a in range(1,11):
        print (Tafel * a)
tafels()