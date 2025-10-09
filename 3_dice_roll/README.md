# Dice Roll (Using an API)

This is a basic demonstration showing how to call an API from MicroPython with the `requests` library and process the resulting JSON on the device.

## Server Setup

Skip this section if you're taking part in an instructor-led workshop.

Before running this code on a device, you'll need to [follow the instructions](../server_side/dice_roller/) to get the dice roll server running. Once the server is up and running, make a note of the IP address that it is running on, as you'll need that for the next step.

## Configuration

If you're taking part in an instructor-led workshop, you can skip this section as the wifi and server details you need are pre-configured.  If you're running the code outside of a workshop, open `dice_roll.py` in your code editor and change these values:

```python
SERVER_IP_ADDRESS = "192.168.8.100"
WIFI_SSID = "iamberyl"
WIFI_PASSWORD = "goodlife"
```

Replace `192.168.8.100` with the IP address of the machine that you're running the dice roll server on.  Replace the values of `WIFI_SSID` and `WIFI_PASSWORD` with the correct values for the wifi network that the machine you're running the dice roll server on is connected to.

Save your changes.

## Run the Code

You can either run the software on the device without installing it:

```bash
mpremote run dice_roll.py
```

Or copy the software onto the device and run it (this will overwrite any existing `main.py` script on the device):

```bash
mpremote cp dice_roll.py :main.py
mpremote reset
```

Press the "A" button on the GFX pack to make an API call to the server, get a dice roll number, and display the result.  Study the code in `dice_roll.py` to make sure you understand how the connection to the wifi network is established, how the call to the server is made, and how the resulting JSON is processed.