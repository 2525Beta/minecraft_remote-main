from mcje.minecraft import Minecraft
import param_MCJE as param
import axis_flat
import time

mc = Minecraft.create(port=param.PORT_MC)
pos = mc.player.getTilePos()

axis_flat.reset_minecraft_world(mc, width=100)
