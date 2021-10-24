def getSeries(bits):
    dict = {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
    }
    lastbit = None
    seriesLength = 0
    
    
    for b in bits:
        if lastbit is not None:
            if lastbit == b:
                seriesLength+=1
            elif seriesLength > 0:
                if seriesLength >= 6:
                    dict[6] = dict[6] + 1
                else:
                    dict[seriesLength] = dict[seriesLength] + 1
                
                seriesLength = 0
            
        lastbit = b
    
    for key, value in dict.items():
        print("Seria ",key,": ", value)
        