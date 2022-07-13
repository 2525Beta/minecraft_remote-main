from curses import tparm
from mcje.minecraft import Minecraft
import param_MCJE as param
import axis_flat
import time
mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("接続完了")

def set_house(x=-10, y=63, z=-10, material=param.GOLD_BLOCK):
    mc.setBlocks( 0, 3, 0, -5, 8, 5, param.STONE)
    mc.setBlocks(-1, 4, 1, -4, 7, 4, param.AIR)
    mc.setBlocks( 0, 4, 4,  0, 5, 4, param.AIR)

    mc.setBlocks( 0, 5, 2,  0, 6, 1, param.GLASS)

set_house()