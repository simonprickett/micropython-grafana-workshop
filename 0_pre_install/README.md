# Device Setup Check

This script checks that the device is correctly set up for the workshop.  It verifies that the required libraries are installed and displays the result on the GFX Pack screen.  It will also tell you whether your device is an original Raspberry Pi Pico W or the newer 2W model.  Both types of device work equally well for this workshop.

## Pre-installed Software

**If you're attending an instructor-led workshop, this software is already installed on your device.**  Simply connect the device to power (or your laptop's USB port) and it will run automatically.

## Reading the Display

When the device starts up, the backlight colour tells you whether everything is set up correctly:

- **Yellowish green** — the device is ready to go.  The required libraries are installed and you're good to start the workshop.
- **Red** — something is wrong.  The required libraries are missing.  Let your instructor know.

The screen also shows the MicroPython version and the Raspberry Pi Pico model, along with a short status message.

## Instructor Notes

### Installing the Setup Check Script

To install this script onto a device, connect it to your machine and copy the file across using `mpremote`:

```bash
mpremote fs cp main.py :main.py
```

Then reset the device so the script runs automatically on startup:

```bash
mpremote reset
```

### Installing the Required Library

The setup check script looks for the `prometheus_remote_write_payload` library in `/lib` on the device.  If it is missing, the backlight will show red.  Install the library like so:

```bash
mpremote mip install github:ttk1/prometheus_remote_write_payload
```

After installing the library, reset the device and confirm the backlight shows yellowish green.
