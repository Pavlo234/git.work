def unique_in_order(kl):
    if len(kl) == 0 :
        return []
    # p = kl
    # kl = []
    # for i in p:
    #     kl.append(i)
    plx = []
    for w in kl:
        if len(plx) == 0:
            plx.append(w) 
        if w != plx[-1]:
            plx.append(w)
    return plx

def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res
            


p = 'AAAsdddddaaA'



print(p)
print(unique_in_order(p))