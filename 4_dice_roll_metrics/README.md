# TODO

## Install Dependencies on the Device

TODO

Install the Prometheus Remote Write library ([details here](https://github.com/ttk1/prometheus_remote_write_payload)) like so:

```bash
mpremote mip install github:ttk1/prometheus_remote_write_payload
```

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
