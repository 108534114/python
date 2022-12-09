輸入=int(input("請輸入一個數："))
可以整除的個數=0
for x in range(1,輸入+1):
    if 輸入 % x==0:
       可以整除的個數=可以整除的個數+1
if 可以整除的個數==2:
   print("是質數")
else:
   print("不是質數")    
    