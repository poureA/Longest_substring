def Find(seq)->str :
    '''This function get a string of digits and return the longest substring with alternating odd/even or even/odd digits.\nIf two or more substrings have the same length, it return the substring that occurs first.'''
    numbers = [str(i) for i in range(0,10)]
    Next = 1
    back = -1
    temp = ''
    series_list = list()
    for i in seq :
        if i not in numbers :
            return 'just integer values can be use'
    for i in seq[:len(seq)-1] :
        if i == '0' :
            return '0 found'
        else :
            if int(i)%2==0 :
                if int(seq[Next])%2!=0 :
                    temp += i
                    Next += 1
                    back += 1
                else :
                    if int(seq[back])%2!=0 :
                        temp += i
                        series_list.append(temp)
                        temp = ''
                        Next += 1
                        back += 1
                    else :
                        temp = ''
                        Next += 1
                        back += 1
            else :
                if int(seq[Next])%2==0 :
                    temp += i
                    Next += 1
                    back += 1
                else :
                    if int(seq[back])%2==0 :
                        temp += i
                        series_list.append(temp)
                        temp = ''
                        Next += 1
                        back += 1
                    else :
                        temp = ''
                        Next += 1
                        back += 1
    if seq[-1] in numbers and seq[-1] != '0' :
        if int(seq[-1])%2==0 :
            if int(seq[-2])%2!=0 :
                temp+= seq[-1]
        else :
            if int(seq[-2])%2==0 :
                temp+= seq[-1]
        lengths = list()
        for i in series_list :
            lengths.append((len(i)))
        for i in lengths :
            if i == max(lengths) :
                idx = lengths.index(i)
                return series_list[idx]
    else :
        return 'somthing wrong'
print(Find.__doc__,'\n')
print(Find(input('enter the series of numbers here :')))
exit = input('enter any key to exit :')
