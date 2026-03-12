import os
import sys
import time
from gfx_pack import GfxPack

gp = GfxPack()
display = gp.display

DISPLAY_WIDTH, DISPLAY_HEIGHT = display.get_bounds()

def clear():
    display.set_pen(0)
    display.clear()
    display.set_pen(15)

def display_centered(text_to_display, y_pos, scale):
    width = display.measure_text(text_to_display, scale)
    x_pos = (DISPLAY_WIDTH - width) // 2
    display.text(text_to_display, x_pos, y_pos, DISPLAY_WIDTH, scale)
    return x_pos

display.set_backlight(0)
display.set_font("bitmap8")

mp_version = f"{sys.implementation.version[0]}.{sys.implementation.version[1]}.{sys.implementation.version[2]}"

if sys.implementation._build == "RPI_PICO_W":
    model = "Pico W"
elif sys.implementation._build == "rpi_pico2_w":
    model = "Pico 2W"
else:
    model = "??????"

try:
    libraries_installed = "prometheus_remote_write_payload" in os.listdir("/lib")
except OSError:
    libraries_installed = False

clear()
display_centered(f"MicroPython {mp_version}", 25, 1)
if libraries_installed:
    display_centered("Ready! :)", 6, 2)
    display_centered("Libraries installed :)", 35, 1)
    gp.set_backlight(128, 107, 0, 0)
else:
    display_centered("Error :(", 6, 2)
    display_centered("Libraries missing :(", 35, 1)
    gp.set_backlight(255, 0, 0, 0)

display_centered(f"Raspberry Pi {model}", 45, 1)

display.update()

while True:
    time.sleep(1)