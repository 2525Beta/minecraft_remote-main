from mcje.minecraft import Minecraft
import param_MCJE1122 as param


mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("接続完了")


def make_house(x=0, y=3, z=0, material = param.DIAMOND_BLOCK):
    #スーパーフラット用なので普通の世界で作成するときはY座標をいじってください
    mc.setBlocks(x,     y,     z,     x - 5, y + 5, z + 5, material)
    mc.setBlocks(x - 1, y + 1, z + 1, x - 4, y + 4, z + 4, param.AIR)
    mc.setBlocks(x,     y + 1, z + 4, x,     y + 2, z + 4, param.AIR)

    mc.setBlocks(x,     y + 2, z + 2,  x, y + 3, z + 1, param.GLASS)
    mc.setBlocks(x - 4, y + 1, z + 5, param.CRAFTING_BLOCK)
    
make_house(x=7)
