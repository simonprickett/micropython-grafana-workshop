import network
import os
import sys
import time
from gfx_pack import GfxPack

gp = GfxPack()
display = gp.display

DISPLAY_WIDTH, DISPLAY_HEIGHT = display.get_bounds()
SPINNER_CHARS = [ "\\", "|", "/", "-" ]

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

clear()
gp.set_backlight(0, 0, 0, 0)
display_centered("Checking...", 25, 2)
display.update()

issues_found = False

# Get the MicroPython version.
mp_version = f"{sys.implementation.version[0]}.{sys.implementation.version[1]}.{sys.implementation.version[2]}"

# What hardware are we on?
if sys.implementation._build == "RPI_PICO_W":
    model = "Pico W"
elif sys.implementation._build == "rpi_pico2_w":
    model = "Pico 2W"
else:
    model = "??????"
    issues_found = True

# Are our dependencies installed?
libraries_status = "Libraries missing :("
try:
    libraries_installed = "prometheus_remote_write_payload" in os.listdir("/lib")
    libraries_status = "Libraries installed :)"
except OSError:
    issues_found = True

# Now check the WiFi credentials...
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("iamberyl", "goodlife")

n = 0
while not wlan.isconnected() and wlan.status() >= 0:
    clear()
    display.text(f"Checking... {SPINNER_CHARS[n]}", 2, 25, DISPLAY_WIDTH, 2)
    display.update()
    
    n = n + 1 if n < len(SPINNER_CHARS) - 1 else 0
    
    time.sleep(0.2)

wifi_status = "Unknown WiFi error :("
if wlan.status() == network.STAT_GOT_IP:
    wifi_status = "WiFi connected :)"
elif wlan.status() == network.STAT_WRONG_PASSWORD:
    wifi_status = "Incorrect WiFi password :("
    issues_found = True
elif wlan.status() == network.STAT_NO_AP_FOUND:
    wifi_status = "Can't see WiFi SSID :("
    issues_found = True
else:
    issues_found = True

clear()

if issues_found:
    display_centered("Error :(", 6, 2)
    gp.set_backlight(255, 0, 0, 0)
else:
    display_centered("Ready! :)", 6, 2)
    gp.set_backlight(128, 107, 0, 0)
    
display_centered(f"MicroPython {mp_version}", 25, 1)
display_centered(libraries_status, 35, 1)
display_centered(f"Raspberry Pi {model}", 45, 1)
display_centered(wifi_status, 55, 1)
display.update()

while True:
    time.sleep(1)