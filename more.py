lst = ['오렌지', "사과", "배"]
# dic = {"오렌지" : 400, "사과" : 200, "바나나" : 300}

# for key in dic:
#     print("key = ", key, dic[key])

# for i,v in enumerate(lst):
#     print("tt = ", i, v)
#     print(lst[i])

# for key, element in dic.items():
#     print(dic[key])

# for i in range(0,20,2):
#     print(i)

# arr = [i ** 2 for i in range(0, 20, 2)]
# print(arr)
# print("최소값:", min(arr))
# print("최대값:", max(arr))

# outs = [f for f in lst if f != '사과']
# print(outs)
error_msg = "정확히 입력해 주세요"
person = input("이름, 나이, 성별을 입력하세요.")
if person == '':
    print(error_msg)
    exit()
if ',' not in person:
    print(error_msg)
    exit()
persons = person.split(',')
if len(persons) != 3:
    print(error_msg)
    exit()
print("당신의 이름은 {}, 당신의 나이는 {}, 당신의 성별은 {} 입니다.".format(persons[0],persons[1],persons[2]))