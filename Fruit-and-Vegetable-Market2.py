import random
import time
face1 = ["微笑","咧嘴","开心","哭泣"]
face2 = ["微笑","咧嘴","开心"]
players = ["a","b","c","d"]
class Player:
    def __init__(self,name):
        self.name = name
        self.faces = []#构造函数创建对象
    def generate_faces(self,confident):
        if confident:
            self.faces = random.choices(face2,k=5)
        else:
            temp = random.choices(face1,k=4)
            if "哭泣" not in temp:
                fifth = "哭泣"
            else:
                fifth = random.choice(face1)
            self.faces = temp + [fifth] #改进将四个人都从四个表情里面随机改成随机选一人从去除表情的表中选择
                                        #并引入类，使得重复环节去除只剩一个，代码整洁
print("游戏开始！")
Players = [Player("a"),Player("b"),Player("c"),Player("d")]
confidentplayer = random.choice(players)
for p in Players:
    p.generate_faces(confident=(p.name == confidentplayer))#使用布尔类型判断进入方法中的if或else
    time.sleep(2)#同一个类中的对象可以调用类中的方法
for round in range(5):
    print(f"\n【第{round+1}轮】")
    display = (f"A:{Players[0].faces[round]} "
               f"B:{Players[1].faces[round]} "
               f"C:{Players[2].faces[round]} "
               f"D:{Players[3].faces[round]}")
    print(display)
    time.sleep(2)
x = input("\n请输入最自信的那一个(a/b/c/d):").lower()
if x == confidentplayer:
    print("正确！")
else:
    print(f"错误！最自信的玩家是:{confidentplayer}")