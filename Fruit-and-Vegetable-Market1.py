import random
import time
face = ["微笑","咧嘴","开心","哭泣"]
a = random.choices(face, k=5)
b = random.choices(face, k=5)
c = random.choices(face, k=5)
d = random.choices(face, k=5)
time.sleep(5)
for round in range(5):
    print(f"\n[第{round+1}轮]")
    print(f"A:{a[round]} B:{b[round]} C:{c[round]} D:{d[round]}")
    time.sleep(5)
ans = []
if "哭泣" not in a:
    ans.append("a")
if "哭泣" not in b:
    ans.append("b")
if "哭泣" not in c:
    ans.append("c")
if "哭泣" not in d:
    ans.append("d")
if len(ans) == 0:
    print("\n本局都哭过，重新开局！")
    exit()
Answer = input("\n请输入abcd里最自信的那一个（没有哭过是最自信的）如果有多个请连着写答案：").lower()
if sorted(list(Answer)) == sorted(ans):
    print("正确！")
else: print(f"错误！答案是：{''.join(ans)}")