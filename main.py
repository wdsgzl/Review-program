import random
from matplotlib import pyplot as plt
percent = 0.05
add = 0.05

def rannum():
    a = random.random()
    a = (int)(a * 100)
    print("你的号码"+str(a))
    return a

def judge(index, per, constant, num):
    list = []


    print("本次休息概率"+str('%.2f'% per))
    index=int(index)
    temp = int(100*per)
    for i in range(temp):
        list.append(int(100 * random.random()))
    print("本轮休息号码" + str(list))
    if num in list:
        img = plt.imread('res/rest.jpg')
        print("恭喜你今天休息！")
        plt.imshow(img)
        plt.show()
        index=1
    else:
        img = plt.imread('res/study.jpg')
        print("给我学习！")
        plt.imshow(img)
        plt.show()
        index += 1

    return str(index)

try:

    file=open('continue/data.txt', "r+", encoding="utf-8")
    element = file.read()
    print("当前连续学习天数"+element)
    number = rannum()
    temp = int(element)
    if temp < 11:
            instant = 0.05
    else:
            instant = (temp - 9) * 0.05
    element = judge(element, instant, percent, number)
    file.seek(0)
    file.write(str(element))
    file.truncate()
except FileNotFoundError:
    print('文件未找到')
