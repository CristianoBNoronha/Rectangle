
l = int(input("digite a largura: "))
h = int(input("digite a altura: "))
rl = 1
rh = 1
while rh <= h:
    if rh == 1:
        while rl <= l:            
            print("#", end = "")
            rl = rl + 1
        rl = 1
        rh = rh + 1
        print()
        
    if rh == h:
        while rl <= l:
            print("#", end="")
            rl = rl + 1
        rl = 1
        rh = rh + 1
        print()
        
    if 1 < rh < h:
        if rl == 1:
            rl = rl + 1
            print("#", end = "")
        if rl >= 2 <= l:
            while rl <= l:
                if rl < l:
                    rl = rl + 1
                    print(" ", end = "")
                if rl == l:
                    rl = rl + 1                    
                    print("#", end = "")
        rh = rh + 1
        rl = 1
        print()
            

        
        #if 1 < rl < l:
            #while rl + 1 <= l - 1:
                #if 1 < rl < l:
                    #print(" ", end = " ")           
        
            
    
    
            



    
    
        
