def percents(mstr):
    uppers = 0 # количесвто больших строк 

    sub_strs = mstr.split(" ")
    for stroka in sub_strs:  #элемент списка в строке 
    
        up = 0 # количество больших 
        low = 0 # количество малых 
        for simbol in stroka:
            if simbol.isupper():
                up +=1

            elif simbol.islower():
                low +=1

        if up > low :
            uppers +=1 

        
    proc = uppers*100// len(sub_strs)
    return proc
    # cnhjrf 1 len(arr) - uppers




print(percents("NDp Lka nuR vtE"), "%")
