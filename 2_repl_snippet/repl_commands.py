from gfx_pack import GfxPack
gp = GfxPack()
gp.set_backlight(255, 0, 0, 0)

from gfx_pack import SWITCH_A
import time

while True:
    if gp.switch_pressed(SWITCH_A):
        print("Button A!")
        time.sleep(1)
