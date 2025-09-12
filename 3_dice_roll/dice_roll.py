import network
import requests
import sys
import time

from gfx_pack import SWITCH_A, GfxPack

SPINNER_CHARS = [ "\\", "|", "/", "-" ]

gfx = GfxPack()
display = gfx.display

DISPLAY_WIDTH, DISPLAY_HEIGHT = display.get_bounds()
display.set_backlight(0)
display.set_font("bitmap8")

def clear_screen():
    display.set_pen(0)
    display.clear()
    display.set_pen(15)


def set_backlight(r, g, b, w):
    gfx.set_backlight(r, g, b, w)


def flash_backlight(how_many, r, g, b, w):
    for _ in range(how_many):
        gfx.set_backlight(r, g, b, w)
        time.sleep(0.2)
        gfx.set_backlight(0, 0, 0, 0)
        time.sleep(0.2)


def display_centered(text_to_display, y_pos, scale):
    width = display.measure_text(text_to_display, scale)
    x_pos = (DISPLAY_WIDTH - width) // 2
    display.text(text_to_display, x_pos, y_pos, DISPLAY_WIDTH, scale)
    return x_pos

clear_screen()
gfx.set_backlight(128, 16, 0, 0)
display_centered("STARTING UP!", 25, 2)
display.update()

# Connect to the network.
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("iamberyl", "goodlife")

n = 0
while not wlan.isconnected() and wlan.status() >= 0:
    clear_screen()
    display.text(f"CONNECTING {SPINNER_CHARS[n]}", 2, 25, DISPLAY_WIDTH, 2)
    display.update()
    
    n = n + 1 if n < len(SPINNER_CHARS) - 1 else 0
    
    time.sleep(0.2)

clear_screen()

if wlan.status() == network.STAT_GOT_IP:
    display_centered("CONNECTED!", 25, 2)
elif wlan.status() == network.STAT_WRONG_PASSWORD:
    display_centered("WRONG WIFI PASSWORD!", 25, 1)
elif wlan.status() == network.STAT_NO_AP_FOUND:
    display_centered("WRONG WIFI SSID!", 25, 1)
else:
    display_centered("WIFI CONNECTION ERROR!", 25, 1)

display.update()

if wlan.status() == network.STAT_GOT_IP:
    flash_backlight(5, 0, 64, 0, 0)
    gfx.set_backlight(0, 0, 0, 80)
    time.sleep(1)
else:
    flash_backlight(5, 128, 0, 0, 0)
    gfx.set_backlight(128, 0, 0, 0)
    
    # Stop as we can't do anything without wifi.
    sys.exit(1)

gfx.set_backlight(0, 0, 0, 80)
clear_screen()
ip_address = wlan.ifconfig()[0]
display_centered(ip_address, 8, 2)
display_centered("A - ROLL DICE!", 27, 1)
display.update()

while True:
    if gfx.switch_pressed(SWITCH_A): 
        clear_screen()
        gfx.set_backlight(128, 16, 0, 0)

        # Make an API request to get the dice roll...
        response_doc = requests.get("http://192.168.8.100:8000/roll").json()
        number = response_doc["number"]

        # Display the result.
        display_centered(ip_address, 8, 2)
        display_centered("A - ROLL DICE!", 27, 1)
        display_centered(f"{number}", 40, 3)
        display.update()

        flash_backlight(5, 0, 64, 0, 0)

    time.sleep(0.02)