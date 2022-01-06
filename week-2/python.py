def calculate(min, max):
    n=min
    sum=0
    while n<=max:
        sum=sum+n
        n+=1
    print(sum)
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


def avg(data):
    i=0
    count=data['count']
    total=0
    while i<count:
        total=total+data["employees"][i]["salary"]
        i+=1
    print(total/data['count'])

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) 

def maxProduct(nums):
    max=0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            sum=nums [i]*nums [j]
            if i==0 and j==1:
                max=sum
            if(sum>max):
                max=sum
    return max
print(maxProduct([5, 20, 2, 6]) )# 得到 120
print(maxProduct([10, -20, 0, 3])) # 得到 30
print(maxProduct([-1, 2]))# 得到 -2
print(maxProduct([-1, 0, 2]))# 得到 0
print(maxProduct([-1,-2,0]))





#def twoSum(nums, target):
#    i=0
#   j=i+1
#    length=len(nums)
#    while i<length:
#        while j<length:
#            num=nums[i]+nums[j]
#            if num==target:
#                return[i,j]
#            j+=1
#        i+=1
    
#result=twoSum([2, 11, 7, 15], 9)
#print(result) # show [0, 2] because nums[0]+nums[2] is 9


def twoSum(nums, target):
    sum=0
    for i in range(0,len(nums)):
        for j in range(1,len(nums)):
            sum=nums[i]+nums[j]
            if sum==target:
                return[i,j]
    print(sum)

    
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


