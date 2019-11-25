# 產生一個隨機整數1-100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random

r = random.randint(1, 100)
count = 0
print(r)
while True:
	ans = input('請輸入一個整數: ')
	ans = int(ans)
	count += 1 # count = count + 1
	if ans < r:
		print('比答案還要小')
	elif ans > r:
		print('比答案還要大')
	else:
		print('終於猜對了!')
		break
	print('你猜了第', count, '次')