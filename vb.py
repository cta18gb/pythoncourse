shape = (input('shape'))
if shape == 'triangle':
    x = int(input('high'))
    y = int(input('high'))
    while (x < 0) or (y < 0):
        x = int(input('hi1gh'))
        y = int(input('hig1h'))
    d = (x * y) / 2
    print('The area is', d)


elif shape == 'recatngular':
    while (z>0)and(k>0)and(l>0)and (m>0):
        z = input(int('enter a horizontal side'))
        k = input(int('enter the other horizontal side'))
        l = input(int('enter a vertical side'))
        m = input(int('enter the other vertical side'))
        a=z+k+l+m
        e=z*m
    print('The perimeter is',a)
    print('The area is,',e)
else:
    w = 5
    while w < 10:
        print(w)
        w += 1


