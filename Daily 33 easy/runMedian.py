import statistics as stats
def runMedian(a):
    print (1/2)
    s = []
    
    for i in a:
        s.append(int(i))
        s.sort()
        if len(s) == 1:
            print (s[0])
            
        elif len(s) % 2 == 0:
            print(0.5 * (s[len(s) // 2 - 1] + s[len(s) // 2]))
            #print(stats.median(s))
        else:
            print(s[len(s)//2])
            #print(stats.median(s))
        


l =  [2, 1, 5, 7, 2, 0, 5]

runMedian(l)