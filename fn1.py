# def fn():
#     print("fn called")

# def exp(x):
#     return x**2

# print(exp(2))

# def get_fruits():
#     return ['오렌지', '사과', '바나나']

# print(get_fruits()[1])

# def get_name():
#     return 'kent', 'beck'

# def full_name(firstname, lastname):
#     return firstname + lastname

# print(full_name('aaa', 'bbb'))

# def var_param(a, *vp):
#     print(type(vp))
#     print(a, len(vp), vp[len(vp)-1])

# var_param('AA', 'bbb', 'ccc')

# def default_param(a, b = 'BBB'):
#     print(a, b)

# default_param('AAA')

# def cal(list):
#     if(list[1] == '+'):
#         return int(list[0]) + int(list[2])
#     elif(list[1] == '-'):
#         return int(list[0]) - int(list[2])
#     elif(list[1] == '*'):
#         return int(list[0]) * int(list[2])
#     else:
#         return int(list[0]) / int(list[2])
# exp = input("연산할 식을 입력 하세요 >> ")
# exps = exp.split(' ')
# result = cal(exps)
# print(result)

def cal(a, b, c):
    if(b == '+'):
        return int(a) + int(c)
    
    elif(b == '-'):
        return int(a) - int(c)
    
    elif(b == '*'):
        return int(a) * int(c)
    
    else:
        return float(a) /float(c)

a, b, c = input("계산할 식을 입력하세요 >> ").split(' ')
print(cal(a,b,c))
