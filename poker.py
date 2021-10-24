from decimal import Decimal

def getPoker(bits):
    n=4;
    dict = {
        0:0,    
        1:0,    
        2:0,    
        3:0,    
        4:0,    
        5:0,    
        6:0,    
        7:0,    
        8:0,    
        9:0,    
        10:0,    
        11:0,    
        12:0,    
        13:0,    
        14:0,    
        15:0,    
    };
    for i in range(0, len(bits), n):
        value = int(bits[i:i+n],2)
        dict[value] = dict[value] + 1
    
    quaterOfLength = len(bits)/4
    
    x = 16/(quaterOfLength)
    suma = 0
    for key, value in dict.items():
        suma += (value*value)
        print("Liczba wystapien liczby ",key,": ", value)
        
    print("Wynik: ", x * suma - quaterOfLength)
        
        
