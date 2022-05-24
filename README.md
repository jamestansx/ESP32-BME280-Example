# BME280 with ESP32
## Installing MicroPython
### Installation of firmware

Download the firmware from [here](https://micropython.org/download/?port=esp32) (direct link to download: https://micropython.org/download/esp32)

## Deploying firmware

Install `esptool` from [GitHub](https://github.com/espressif/esptool/releases/) or via `pip`:

```
pip install esptool
```

Connect the board to computer and erase the flash with the command (hold the boot button while it erase the flash):
```
esptool --port COMx erase_flash
```

Then deploy the firmware using:
```
esptool --chip esp32 --port COMx write_flash -z 0x1000 /path/to/esp32.bin
```

> note:
> check the port that esp32 used by checking in the device manager
> should be COMx, where x is an integer

## Getting Started with REPL
### Via serial port

On Windows, install `TeraTerm` to access the prompt over USB-serial. [Download link](https://osdn.net/projects/ttssh2/releases/)

## Uploading files to ESP32
### Using rshell

Install `rshell` via `pip`:

```
pip install rshell
```

Use `rshell` to connect to ESP32:

```
rshell -p COMx -e notepad
```

> the filepath of ESP32 is /pyboard/

To copy file to ESP32: (inside rshell)

```
# cp /path/to/file_to_copy /pyboard/
```

## Reference

1. [Micropython Documentation](https://docs.micropython.org/en/latest/esp32/quickref.html)
2. [rshell GitHub](https://github.com/dhylands/rshell)
3. [BME280 tutorial](https://randomnerdtutorials.com/micropython-bme280-esp32-esp8266/)

