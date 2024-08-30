import re


def add(li):
    res = 0
    for n in li:
        # print(n)
        res += int(n)
    return res

def addition(st):

    # # res_1 = 0
    # split_st = st.split(',')
    # # print(type(split_st))
    # result_1 = add(split_st)
    # print(result_1)

    second_split = re.split('\n|,', st)
    print(second_split)
    result_2 = add(second_split)
    print(result_2)



    # return res



s = '1,2,3'
print(addition(s))