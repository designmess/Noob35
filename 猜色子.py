import random
print("$"*30)
print("$"," "*26,"$")
print("$"," "*26,"$")
print("$"," "*2,"welcome to this game"," "*2,"$")
print("$"," "*26,"$")
print("$"," "*26,"$")
print("$"*30)
username=input("小伙子你叫什么名字:\n")
money=0
answer=input("要玩两把吗？(y/n)")
if answer=="y":

	while money<2:
		n=int(input("金币不足,请充值（充值金额必须是100的倍数):"))
		if n%100==0 and n>0:
			money=(n//100)*30
	print("当前游戏币{}枚，玩一局扣除2个币".format(money))
	print("Load...")
	while True:
		t1=random.randint(1,6)
		t2=random.randint(1,6)
		money-=2
		print("洗牌完成请猜大小:\n")
		guess=input("请输入'大'或者'小'：")
	#判断：
		if ((t1+t2)>6 and guess=="大") or ((t1+t2)<=6 and guess=="小"):
			print("骰子一个{}点,一个{}点,共{}点".format(t1,t2,t1+t2))
			print("{}恭喜中奖,获得游戏币4个".format(username))
			money+=4
			print("目前您有{}枚游戏币".format(money))
		else:
			print("骰子一个{}点,一个{}点,共{}点".format(t1,t2,t1+t2))
			print("本局未猜中,")
			print("目前您有{}枚游戏币".format(money))
		answer=input("是否继续玩？y/n")
		if answer!="y" or money<2:
			print("Game Over")
			break
	print("欢迎下次光临")
