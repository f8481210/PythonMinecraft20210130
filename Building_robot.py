#Building_robot
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

name = input("請問你叫什麼名字：")
long = int(input(name+"請問你要蓋多長的房子："))
weight = int(input(name+"請問你要蓋多寬的房子："))
hight = int(input(name+"請問你要蓋多高的房子："))

block = int(input(name+"請問要用什麼樣子的材料："))

x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+long,y+hight,z+weight,block)
mc.setBlocks(x+1,y+1,z+1,x+long-1,y+hight-1,z+weight-1,0)
 #空心

mc.postToChat(name+"你指定的建材"+str(block))
mc.postToChat("你的房子長："+str(long)+"寬："+str(weight)+"高："+str(hight)+"的建築物已將建好了")