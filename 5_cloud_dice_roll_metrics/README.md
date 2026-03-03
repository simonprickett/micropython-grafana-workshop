# Dice Rolls (Metrics Creation - Grafana Cloud Version)

This demo is a different take on the dice roll. Instead of calling an API to get the dice roll, the device generates a number itself and sends it as a metric to Grafana Cloud using the Prometheus remote write library.

## Sign up for the Grafana Cloud Free Forever Plan

TODO

## Install Dependencies on the Device

This example uses a MicroPython library that makes sending metrics to Prometheus or Grafana Cloud easier.  **If your instructor provided the hardware for this workshop, you can skip this step as the library is already installed.**

If you're using your own hardware, you'll need to install the library ([details here](https://github.com/ttk1/prometheus_remote_write_payload)) like so with your device connected to your machine:

```bash
mpremote mip install github:ttk1/prometheus_remote_write_payload
```

## Configuration

TODO

## Run the Code

You can either run the software on the device without installing it:

```bash
mpremote run cloud_dice_roll_metrics.py
```

Or copy the software onto the device and run it (this will overwrite any existing `main.py` script on the device):

```bash
mpremote cp cloud_dice_roll_metrics.py :main.py
mpremote reset
```

Press button "A" to roll the dice and send the metric to Grafana Cloud.