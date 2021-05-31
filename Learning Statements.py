#Created on 2021-Jun-2021
#Created by Jayaprakash J
############################################
#Learning about statements.
############################################
while True:
    reply =input('Enter Text:')
    if reply =="stop": 
        break
    try:
        result = int(reply)
    except:
        print('Excption Occured!')
    else:
        print(reply)
        i = int(reply)
        if i < 20:
            print('low')
        else:
            print('High')
print('bye!')

