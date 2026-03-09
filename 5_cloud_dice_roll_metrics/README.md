# Dice Rolls (Metrics Creation - Grafana Cloud Version)

This demo is a different take on the dice roll. Instead of calling an API to get the dice roll, the device generates a number itself and sends it as a metric to Grafana Cloud using the Prometheus remote write library.

## Sign up for the Grafana Cloud Free Forever Plan

You'll need to sign up for the Grafana Cloud Free Forever plan.  [Start here](https://grafana.com/get).

## Install Dependencies on the Device

This example uses a MicroPython library that makes sending metrics to Prometheus or Grafana Cloud easier.  **If your instructor provided the hardware for this workshop, you can skip this step as the library is already installed.**

If you're using your own hardware, you'll need to install the library ([details here](https://github.com/ttk1/prometheus_remote_write_payload)) like so with your device connected to your machine:

```bash
mpremote mip install github:ttk1/prometheus_remote_write_payload
```

## Configuration

There are a couple of constants that you'll need to set to have values appropriate for your Grafana Cloud environment.  Open `cloud_dice_roll_metrics.py` in your editor.

Find the line:

```python
CLOUD_ENDPOINT = "TODO your Grafana Cloud Prometheus Remote Write Endpoint"
```

and replace the value with the URL of your Grafana Cloud Prometheus Remote Write endpoint.  Ask your instructor for help with finding this.

Find the lines:

```python
CLOUD_AUTH = (
    "TODO your Grafana Cloud Prometheus username.",  # Example 2223456
    "TODO your Grafana Cloud API Token"
)
```

and replace the values with your Grafana Cloud username and API token.   Ask your instructor for help with finding these.

Save your changes.

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