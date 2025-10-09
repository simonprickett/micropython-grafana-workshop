# Dice Roll (Using an API)

TODO

## Server Setup

Before running this code on a device, you'll need to [follow the instructions](../server_side/dice_roller/) to get the dice roll server running. Once the server is up and running, make a note of the IP address that it is running on, as you'll need that for the next step.

If your instructor tells you the IP address of a server that's already running the dice roller, use that instead of setting up your own server.

## Configuration

Open `dice_roll.py` in your code editor and find line 98 which looks like this:

```python
response_doc = requests.get("http://192.168.8.100:8000/roll").json()
```

Change `192.168.8.100` for the IP address that your dice roll server is running on. Save your changes.

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