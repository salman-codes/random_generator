import time

def shuffle (arr, n):
    for i in range(n-1,0,-1):
        j= int(0 + int(round(time.time()*1000)) % (i - 0))
        arr[i],arr[j] = arr[j],arr[i]
    num=""
    k=0
    l=10
    while l > 1:
        num=str(arr[k])+num
        k+=1
        l-=1
    return num

arr=[0,1,2,3,4,5,6,7,8,9]

def random_number(min, max):
    num = int(shuffle(arr, 10))
    return int(min + num % (max - min))

min = int(input("First Number: "))
max = int(input("Second Number: "))
count = int(input("How many random numbers you want? "))
random_num_list = []
while count > 0:
    rand = random_number(min, max)
    random_num_list.append(rand)
    count -= 1

print(random_num_list)
