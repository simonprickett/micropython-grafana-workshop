# TODO

## Device Setup

TODO

First, install the Prometheus Remote Write library ([details here](https://github.com/ttk1/prometheus_remote_write_payload)):

```bash
mpremote mip install github:ttk1/prometheus_remote_write_payload
```

Then either run the software on the device without installing it:

```bash
mpremote run dice_roll_metrics.py
```

Or copy the software onto the device and run it (this will overwrite any existing `main.py` script on the device):

```bash
mpremote cp dice_roll_metrics.py :main.py
mpremote reset
```
