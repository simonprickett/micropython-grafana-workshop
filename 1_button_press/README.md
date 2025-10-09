# Button Press Example

This is a basic button press example that shows how the MicroPython library for the GFX Pack works.  The GFX pack has 5 buttons, the code updates the text on screen when each button is pressed and sets the backlight to different colours.

## Run the Code

You can either run the software on the device without installing it:

```bash
mpremote run button_press.py
```

Or copy the software onto the device and run it (this will overwrite any existing `main.py` script on the device):

```bash
mpremote cp button_press.py :main.py
mpremote reset
```

Once the code's up and running, try pressing the buttons on the GFX pack to see what happens.  Study the code to make sure that you understand how it works.
