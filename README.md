# MicroPython Grafana Workshop

## Introduction

This is the GitHub repository containing code and resources for a MicroPython / Grafana workshop.  

If you're interested in having me run this workshop for your Meetup Group, work team or other gathering, please [get in touch](https://simonprickett.dev/contact/) and we'll see what we can do!  I have around 25 sets of the hardware needed for this.

There are 4 main exercises in this workshop:

1. Discover some of the capabilities of MicroPython with the Pimoroni GFX Pack for the Raspberry Pi Pico W.
1. Try out the MicroPython REPL on a Pico W and experience immediate feedback.
1. Learn how to use the `requests` library to call a simple API and display results returned from it.
1. Putting everything together, we conclude by sending basic metrics from the Pico W devices to Prometheus, and visualizing them with Grafana.

This workshop is suitable for all, some Python experience is handy but not strictly required.  Everyone (attendees and instructor) need to bring laptops and have the ability to install software on them.  If I'm running the workshop, I bring USB A to micro USB cables for attendees to connect the Pico W devices to their laptops: attendees must bring their own port adapter / hub / anything required to ensure there's a USB A port available on their machines.  The venue needs to provide wifi.  If I'm running the workshop, I bring my own additional travel router to ensure a smooth experience with connecting the devices to a network. 

## Pre-Requisites

### Workshop Attendee

To get the most from this workshop, you'll need to install the following software:

* A recent version of [Python 3](https://www.python.org/downloads/) (this project has been tested with Python 3.13.12 on macOS Tahoe 26.0.1).
* [Git command line tools](https://git-scm.com/downloads).
* A code editor of your choice ([VSCode](https://code.visualstudio.com/) is a good all-rounder).  Anything that you're comfortable using to browse and do minor editing on Python files is fine.
* The MicroPython [`mpremote`](https://docs.micropython.org/en/latest/reference/mpremote.html) remote control utility.

**Proceed once you have all of these installed.**

Now, open your terminal and clone the GitHub repository to wherever you like to keep coding projects on your machine:

```bash
git clone https://github.com/simonprickett/micropython-grafana-workshop.git
```

Then open this folder with your code editor and your terminal.

### Workshop Instructor

**If you are attending an instructor led workshop and aren't the instructor, you can skip this section!**

If you're following this alone, or leading a workshop then you'll need to completed the Attendee requirements above, then do a few extra setup tasks on your machine.  These are:

#### Get Your IP Address

* Connect to the wifi network that you're going to use for the workshop.  The Pico devices should also be able to connect to the same network - meaning that it needs to be one that has an SSID and password only.  Networks with captive portal / agree to terms and conditions joining steps won't work.  For that I recommend using your own router.  I use [this excellent travel router](https://www.gl-inet.com/products/gl-mt3000/).
* Make a note of your machine's IP version 4 address on the wifi network. On macOS, you can get this by running `ipconfig getifaddr en0` in the terminal.

#### Docker

You'll need Docker Desktop as some components run inside Docker containers to simplify setup.

* Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

#### NTP Server

Some of the example code requires the Pico devices to have an idea of the current time.  The devices don't have a built in real time clock sync, but can get the time from an NTP server on boot up.  So, you'll need to run an NTP server for them to talk to.

Start the NTP server from the terminal using Docker:

```bash
docker run --name=ntp --restart=always --publish=123:123/udp cturra/ntp
```

#### Prometheus

TODO why?

* TODO Prometheus setup

#### Grafana

* TODO Get Grafana set up
* TODO import Grafana dashboard

**Before starting the workshop, make sure that the NTP server, Prometheus, Grafana and the dice roll server are all running.**

#### MicroPython Script Configuration

A couple of the MicroPython scripts need to know the SSID and password for your wifi network, and the IP address of the machine that you're running the server side components on.

Edit each of these scripts in turn:

* `3_dice_roll/dice_roll.py`
* `4_dice_roll_metrics/dice_roll_metrics.py`

In each file, replace the section:

```python
SERVER_IP_ADDRESS = "192.168.8.100"
WIFI_SSID = "iamberyl"
WIFI_PASSWORD = "goodlife"
```

with the details for your wifi network and machine's IP address. Save your changes in these files before continuing.

## Hardware

Your instructor will have all of the hardware that you need. If you're using these materials outside of the workshop, you'll need to get these items:

* Either a [Raspberry Pi Pico W](https://shop.pimoroni.com/products/raspberry-pi-pico-w?variant=40059369652307) or [Pico 2W](https://shop.pimoroni.com/products/raspberry-pi-pico-2-w?variant=54852253024635).  You'll need to solder headers to it, or just buy the "WH" variant with the headers pre-attached.
* A [Pimoroni GFX Pack display](https://shop.pimoroni.com/products/pico-gfx-pack?variant=40414469062739).
* A micro USB to USB A or C data cable: you'll use this to connect the Pico to your machine.

You only need one set of these, but if you have multiple it makes for a more interesting demo.

Prepare the hardware by attaching the GFX Pack to the Pico's headers, ensuring that the USB port on the Pico aligns with the picture of the USB port on the back of the GFX Pack.

You'll then need to install the MicroPython runtime, using Pimoroni's "batteries included" build of MicroPython: this ensures that you have the drivers needed to work with the GFX Pack screen, backlight and buttons.

* Pimoroni MicroPython: [Raspberry Pi Pico W version](https://github.com/pimoroni/pimoroni-pico/releases) (filename begins `picow-`).
* Pimoroni MicroPython: [Raspberry Pi Pico 2W version](https://github.com/pimoroni/pimoroni-pico-rp2350/releases) (filename begins `rpi_pico2_w-`).

**Be sure to choose the "W" version otherwise you won't get wifi support!**

Once you've downloaded the correct MicroPython runtime image, install it on your device like this:

* Hold down the white "BOOTSEL" button on the top of the device and keep it held down while connecting the device to your machine using a micro USB to USB A or C data cable.
* Your device appears as a mounted disk on your machine.  You can now release the "BOOTSEL" button.
* Drag the `.uf2` file that you downloaded to that drive and keep the device attached until copying completes.

Then, use `mpremote` to check your installation. With the Pico still connected, enter the following command on your machine:

```bash
mpremote repl
```

You should see output similar to this (MicroPython version and the device path may vary). The output below is from a Pico W, Pico 2W output will differ slightly.

```
Connected to MicroPython at /dev/cu.usbmodem31401
Use Ctrl-] or Ctrl-x to exit this shell
MicroPython v1.25.0, picow v1.25.0 on 2025-05-12; Raspberry Pi Pico W with RP2040
Type "help()" for more information.
>>>
```

Press `Ctrl-X` to exit and disconnect the Pico from your system.

## Agenda

TODO