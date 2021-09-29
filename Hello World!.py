def helloworld(amount: int):
    global a
    for a in range(amount):
        print('hello world')
    return
def attempt():
    global a
    try:
        a = (int)(input('Amount of times repeated: '))
        helloworld(a)
        
    except ValueError:
        print('please enter a number.')
        attempt()
        
attempt()