"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）

TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
如果传入“李秋水”，打印“呸，贱人”，
如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

"""

#定义一个类
class TongLao:
    def __init__(self,hp,power): #属性有血量，武力值（通过传入的参数得到）
        self.hp = hp
        self.power = power

    def see_people(self,name):
        if (name =='WYZ'):
            print("无崖子师弟！!")
        elif(name =="LQS"):
            print("呸，贱人李秋水")
        elif(name =="DCQ"):
            print("叛徒！我杀了你丁春秋")

#fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
#需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

    def fight_zms(self,enemy_hp,enemy_power):
        self.hp = self.hp/2
        self.power = self.power*10
        #进行一回合制对打
        final_tonglao_hp = self.hp - enemy_power
        final_enemy_hp = enemy_hp -self.power
        if(final_tonglao_hp > final_enemy_hp):
            print("天山童姥获胜")
        elif(final_tonglao_hp < final_enemy_hp):
            print("敌人获胜")
        else:
            print("双方平局")


tonglao = TongLao(100,500)
tonglao.see_people('WYZ')
tonglao.fight_zms(1000,20)