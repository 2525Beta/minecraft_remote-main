from mcje.minecraft import Minecraft
import param_MCJE1122 as param
import axis_flat
import time

Materials = param.IRON_BLOCK
X,Y,Z = 0,3,0
mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("接続完了")


mc.setBlocks( X, Y, Z, X-5, Y+5, Z+5, Materials)
mc.setBlocks(X-1, Y+1, Z+1, X-4, Y+4, Z+4, param.AIR)
mc.setBlocks( X, Y+1, Z+4,  X, Y+2, Z+4, param.AIR)

mc.setBlocks( X, Y+2, Z+2,  X, Y+3, Z+1, param.GLASS)
mc.setBlocks(X-4, Y+1, Z+5, param.CRAFTING_BLOCK)