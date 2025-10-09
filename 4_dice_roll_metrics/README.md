# Dice Rolls (Metrics Creation)

This demo is a different take on the dice roll. Instead of calling an API to get the dice roll, the device generates a number itself and sends it as a metric to Prometheus using the Prometheus remote write library.

## Install Dependencies on the Device

This example uses a MicroPython library that makes sending metrics to Prometheus or Grafana Cloud easier.  If your instructor provided the hardware for this workshop, you can skip this step as the library is already installed. If you're using your own hardware, you'll need to install the library ([details here](https://github.com/ttk1/prometheus_remote_write_payload)) like so with your device connected to your machine:

```bash
mpremote mip install github:ttk1/prometheus_remote_write_payload
```

## Configuration

If you're taking part in an instructor-led workshop, you can skip this section as the wifi and server details you need are pre-configured.  If you're running the code outside of a workshop, open `dice_roll_metrics.py` in your code editor and change these values:

```python
SERVER_IP_ADDRESS = "192.168.8.100"
WIFI_SSID = "iamberyl"
WIFI_PASSWORD = "goodlife"
```

Replace `192.168.8.100` with the IP address of the machine that you're running Prometheus and the NTP server on.  Replace the values of `WIFI_SSID` and `WIFI_PASSWORD` with the correct values for the wifi network that the machine you're running the dice roll server on is connected to.

## Run the Code

You can either run the software on the device without installing it:

```bash
mpremote run dice_roll_metrics.py
```

Or copy the software onto the device and run it (this will overwrite any existing `main.py` script on the device):

```bash
mpremote cp dice_roll_metrics.py :main.py
mpremote reset
```

Press button "A" to roll the dice and send the metric to Prometheus / Google Cloud.
