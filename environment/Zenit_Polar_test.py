def cripto():

    zenit, polar = 'zenit', 'polar'
    final_message = ''
    message = input('message : ')
    n = 0
    for i in range(len(message)):
        x = message[n]
        if x in zenit:
            x = int(zenit.find(message[n]))
            final_message += polar[x]
        elif x in polar:
            x = int(polar.find(message[n]))
            final_message += zenit[x]
        else:
            final_message += message[n]
        n += 1
    
    print(final_message)