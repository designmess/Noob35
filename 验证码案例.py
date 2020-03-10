# filename="abcdefghijk"
# #[] [:] 包前不包后
# print(filename[3:6])
# print(filename[:6]) #前可以省略 从头开始打
# print(filename[3:]) #后可以省略
# print(filename[7:-1]) #支持负数 但是负数包前不包后 

# #双[::-]
# print(filename[::-1]) #-1表示方向
# print(filename[-1:-6:-1])
# #但又 print(filename[0:5:-1])是错的
# print(filename[5:0:-1])
# i="hello world"
# # h e l l o [] w o r l d
# # 0 1 2 3 4 5  6 7 8 9 10
# #-11-10-9-8-7-6-5-4-3-2-1
# print(i[-1:5:-1])
# print(i[0:5])
# print(i[::-1])
# print(i[-8:1:-1])
# print(i[2:8])

#字符串内建函数 关于大小写相关
# message="yuqi is cute."
# #.
# msg=message.capitalize()
# print(msg)
# msg=message.title()
# print(msg)
#.upper 全部大写 .lower 全部小写
#验证码案例
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
code=""
import random
while True:
	for i in range(4):
		ran=random.randint(1,len(s))
		#len(s)求字符串长度
		code+=s[ran-1]
		#TypeError: 'str' object is not callable
	print("验证码:"+code)
	user_input=input("请输入验证码:")

	if user_input.lower()==code.lower():  #不区分大小写
		print("Welcome to XX")
		break
	else:
		code=""
		print("验证码错误请重新输入")