#random_poker
import random
def playerOne(status):
    if status == "ok":
        print("OK")
        for i in range(0,3): #抽三張牌
            result = random.choice(card_symbol) #抽花色
            number = random.choice(card_number) #抽數字
            card = [result+number]
            player1_card.append(card)
            
        mc.setSign(x,y,z,63,0,"Player1's card:",player1_card[0],player1_card[1],player1_card[2])
            
    elif status == "not":
        print("get ready")
    else:
        print("ERROR try again")

def playerTwo(status2):
    if status == "ok":
        print("OK")
        for i in range(0,3): #抽三張牌
            result = random.choice(card_symbol) #抽花色
            number = random.choice(card_number) #抽數字
            card = [result+number]
            player2_card.append(card)
            
        mc.setSign(x+5,y,z,63,0,"Player2's card:",player2_card[0],player2_card[1],player2_card[2])
            
    elif status == "not":
        print("get ready")
    else:
        print("ERROR try again")
    
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

card_symbol = ["梅花","愛心","方塊","黑桃"]
card_number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

player1_card = []
player2_card = []

status = input("請確認玩家一的狀況(ok or not):")
status2 = input("請確認玩家二的狀況(ok or not):")
playerOne(status)
playerTwo(status2)




