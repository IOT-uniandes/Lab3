# Import all the modules
import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

def assign(num:int):
    main(num, cascaded=1, block_orientation=90, rotate=0)

def main(num:int, cascaded, block_orientation, rotate):    
    # create matrix device
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=cascaded or 1, block_orientation=block_orientation, rotate=rotate or 0)
    # debugging purpose
    print("[-] Matrix incializando")

    coords = {
        1: (0,0,3,3),
        2: (4,0,7,3),
        3: (0,4,3,7),
        4: (4,4,7,7),
    }

    with canvas(device) as draw:
        draw.rectangle(coords[num], outline="red", fill="red")

    time.sleep(1)
