

def addition(st):

    res = 0
    split_st = st.split(',')
    print(type(split_st))
    for n in split_st:
        # print(n)
        res += int(n)

    return res



s = '1,2,3'
print(addition(s))