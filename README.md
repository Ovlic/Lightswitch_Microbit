Lightswitch_Microbit
=====
Lightswitch-powered microbit connected to a Mac to trigger an applescript file  

Prerequiries
--------------------
* Install [brightness](https://github.com/nriley/brightness) for display brightness with `brew install brightness` or clone from source (Instructions in the repo)
* Install the [serial](https://pypi.org/project/pyserial/) module with `pip install pyserial`
* Make sure the light_on and light_off applescript files work, otherwise specify the file path in the command
* Make sure the pins plugged in are `P0` and `GND`
* Transfer the `microbit_lightswitch.hex` file to the microbit (View the original code [here](https://makecode.microbit.org/_MJkdoy6zXJt7))

Executing
--------
run `python3 lightswitch.py` to start the script
