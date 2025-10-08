# TODO

TODO

## Server Setup

TODO.

## Device Setup

You can either run the software on the device without installing it:

```bash
mpremote run dice_roll.py
```

Or copy the software onto the device and run it (this will overwrite any existing `main.py` script on the device):

```bash
mpremote cp dice_roll.py :main.py
mpremote reset
```