# Discovering the MicroPython REPL

Now it's time to try out MicroPython's REPL (Read, Evaluate, Print, Loop) interface.  This is where we get immediate execution of code we enter at the command line.

## Start a REPL Session

With the device connected to your laptop, start a REPL session like so:

```bash
mpremote repl
```

You may need to hit Ctrl-C a couple of times before you reach the REPL prompt which looks like this:

```bash
>>>
```

## Setting the Backlight Colour

Let's set the device's backlight colour from the REPL.  To do this, we'll need to import some library code.  Type the following into the REPL and hit return when done:

```python
from gfx_pack import GfxPack
```

As an `import` statement produces no output, you'll just see the `>>>` prompt again.  Now enter this code and press return:

```python
gp = GfxPack()
```

This instantiates an instance of the device's code library, assigning it to a variable called `gp`.  Again, this doesn't generate any output.

Now, set the backlight to the colour of your choice using red, green, blue values between 0 and 255.  the 4th parameter is for white and you can ignore that. For example, enter the following and press return to set the backlight to red:

```python
gp.set_backlight(255, 0, 0, 0)
```

Try some other colours!

When you're done, turn off the backlight like so:

```python
gfx.set_backlight(0, 0, 0, 0)
```

## Handling a Button Press

TODO point is we're handling a loop (non-immediate execution) and explaining how the REPL handles that.

```python
from gfx_pack import SWITCH_A
import time

while True:
    if gp.switch_pressed(SWITCH_A):
        print("Button A!")
        time.sleep(1)
```

## Exiting the REPL Session

When you're done, exit the REPL session by TODO.

