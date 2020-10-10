import random

r = random.randint(1,100)
count = 0
while True:
	print("\n")
	num = input("猜一個數字，範圍1~100：")
	num = int(num)
	count = count + 1
	if num == r:
		print("終於猜對了!!總共猜了",count,"次")
		break
	elif num > r:
		print("猜錯了，密碼比",num,"還要小")
	else:
		print("猜錯了，密碼比",num,"還要大")

	print("這是你目前猜的第",count,"次")
