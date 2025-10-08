# Dice Roller (Server)

This is a small [Flask](https://flask.palletsprojects.com/) server that exposes a single endpoint.  That endpoint returns a random dice roll between 1-6 inclusive as a JSON document. The server runs on your machine that needs to be on the same network as devices running the [`3_dice_roll`](../../3_dice_roll/) code, which will attempt to connect to it. That code should be updated to contain the IP address for your server, which Flask will log for you when you start it.

## Pre-Requisites

You'll need a recent version of [Python 3](https://www.python.org/downloads/) installed.  This has been tested using Python 3.13.2 on macOS Tahoe 26.0.1.

## Setup

First, create a virtual Python environment and activate it:

```bash
python -m venv venv
. ./venv/bin/activate
```

Next, install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the Server

Start the server like this:

```bash
python app.py
```

You should expect to see output similar to the following:

```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://192.168.5.22:8000
Press CTRL+C to quit
```

The IP address displayed will vary depending on the IP address of your system.

## Roll the Dice!

Open your browser and visit `http://127.0.0.1:8000/roll`

You should see JSON output containing a number from 1-6 inclusive.  Example:

```json
{
  "number": 4
}
```

## Stop the Server

* When you're ready to stop the server, press `Ctrl+C` to return to the terminal prompt. 
* You can deactivate the Python virtual envrionment by typing `deactivate` and hitting return.

## Clean Up

If you don't want to use this again, you can remove the virtual environment files like so:

```
rm -rf venv
```