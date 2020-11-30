"""
一个回合制游戏，每个角色都有hp和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""

def fight():
    ##定义四个变量分别代表各自血量和攻击力
    my_hp = 1000
    my_power = 200
    enemy_hp = 700
    enemy_power = 200
    while True:
        #双方血量一直执行减法直至一方血量为0
        my_hp = my_hp - enemy_power #我的血量等于我的上一次血量减去敌人的攻击力
        enemy_hp = enemy_hp - my_power #敌人血量等于敌人上一次血量减去我的攻击力
        if(my_hp == enemy_hp == 0): #双方血量相等平局
            print("平局")
            print("我的血量是",my_hp)
            print("敌人的血量是",enemy_hp)
            break
        elif(my_hp <= 0): #对打后我的血量先小于等于0， 我输了
            print("我输了")
            print("我的血量是",my_hp)
            print("敌人的血量是",enemy_hp)
            break
        elif(enemy_hp <= 0): #一次或几次对打后，敌人的血量先小于等于0， 敌人输了
            print("敌人输了")
            print("我的血量是",my_hp)
            print("敌人的血量是",enemy_hp)
            break
        else:
            True #如果双方血量都没有小于等于0， 继续循环继续对打

fight() #执行方法fight