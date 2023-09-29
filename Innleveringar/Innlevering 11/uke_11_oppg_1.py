
def mean(listen):
    length = len(listen)
    summednumbers = 0
    for i in listen:
        summednumbers += i
    average = summednumbers / length
    return average

def median(listen):
    length = len(listen)
    sortedlist = sorted(listen)
    if length % 2 == 0:
        mednumber1 = sortedlist[int(length/2)]
        mednumber2 = sortedlist[int((length/2)-1)]
        med = (mednumber1 + mednumber2) / 2
    else:
        med = sortedlist[int(length/2)]
    return med
def mode(listen):
    ny = {}
    for i in listen:
        if i in ny:
            ny[i] += 1
        else:
            ny[i] = 1
    return max(ny, key=ny.get) #Stack overflow https://stackoverflow.com/questions/31288030/is-there-a-significantly-better-way-to-find-the-most-common-word-in-a-list-pyth 08.11.21
        
