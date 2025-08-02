import math



inputList = input("Enter a list your clan members' levels, separated by commas. ")
clanList = inputList.strip().split(",")
a = 0
def health(level):
    if level < 7:
        p = 0.1*level
    else:
        p = (0.2*((level-1) % 3))+0.3
    immohealth = 17500*p*(3**(math.ceil(x/3)))

    return immohealth

damagePerClick = 0

for person in clanList:
    damagePerClick += 10*(3**(int(person)-1))
n=1
a=0
b=0
c=0
d=0
e=0
f=0
x=1
while health(x) <= 900*damagePerClick:
    for n in range(901):
        if health(x) <= n*damagePerClick and health(x) > (n-1)*damagePerClick:
            c=b
            b=a
            a=x
            f=e
            e=d
            d=n
        n+=1
    x+=1
print('')

def pve(x):
    if x < 0:
        x=0
    return x

print('Maximum Immortal levels:')
print(f'{c} @ {round(f/15,1)} CPS.  (raw clicking: {round(pve(-30+f/15),1)} CPS)')
print(f'{b} @ {round(e/15,1)} CPS.  (raw clicking: {round(pve(-30+e/15),1)} CPS)')
print(f'{a} @ {round(d/15,1)} CPS.  (raw clicking: {round(pve(-30+d/15),1)} CPS)')