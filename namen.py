def functie():
    a = input('U can enter names here, To stop u can type stop: ')
    
    b = input('U can enter ages here, To stop u can type stop: ')
    if a == 'stop':
        quit()
    elif b == 'stop':
        quit()
    else:
        functie()
functie()