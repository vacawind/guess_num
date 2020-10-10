import random

r = random.randint(1,100)

while True:
	num = input("猜一個數字，範圍1~100：")
	num = int(num)
	if num == r:
		print("終於猜對了!!")
		break
	elif num > r:
		print("猜錯了，密碼比",num,"還要小")
	else:
		print("猜錯了，密碼比",num,"還要大")
