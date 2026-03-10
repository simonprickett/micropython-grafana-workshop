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

Try some other colours!  Note you can use the up and down cursor keys to scroll through previous lines of code.

When you're done, turn off the backlight like so:

```python
gfx.set_backlight(0, 0, 0, 0)
```

## Handling a Button Press

Next we'll see how to handle a button press, and enter code that loops into the REPL.  In this case, the code won't always execute immediately, as the REPL needs to see the complete loop code before it can run it.

First, let's import a couple more things we'll need.  Type the following commands into the REPL, pressing return after each:

```python
from gfx_pack import SWITCH_A
```

Then:

```python
import time
```

Now we're going to tell the REPL we want to loop forever.  Enter this command and press return:

```python
while True:
```

What happens now?  Nothing's exceuted yet, and the REPL prints:

```
...
```

which means that it's waiting for the body of the loop.  Now type this and press return:

```python
if gp.switch_pressed(SWITCH_A):
```

and note that the REPL indents the cursor some more as it now wants the conditional statement to execute when the `if` condition matches.  Type these lines of code, pressing return after each:

```python
print("Button A!")
time.sleep(1)
```

That's all the code we need... but how do we tell the REPL we're done here and it's time to execute it?  Press return twice... and note that the prompt is no longer indented.  We've told the REPL that's the end of the loop.  To run the code, press return again...

Nothing will happen, but note that we aren't back at the `>>>` prompt.  This is because the REPL is running the loop continuously.  

Press button A on the device.  Note that the REPL prints "Button A!" every time you do this.

How do we stop the REPL from running this loop so we can return to the `>>>` prompt?  Press `Ctrl+C` to generate a KeyboardInterrupt event.

## Exiting the REPL Session

When you're done experimenting with the REPL, exit it by pressing `Ctrl+]`.

