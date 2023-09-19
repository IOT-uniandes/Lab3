# Import all the modules
import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message, draw
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

def paint(msg):
    main(msg, cascaded=1, block_orientation=90, rotate=0)

def main(msg, cascaded, block_orientation, rotate):    
    # create matrix device
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=cascaded or 1, block_orientation=block_orientation, rotate=rotate or 0)
    # debugging purpose
    print("[-] Matrix incializando")

    # debugging purpose
    print("[-] Imprimiendo: %s" % msg)
    #show_message(device, msg, fill="red", font=proportional(CP437_FONT),scroll_delay=0.1)
    draw.rectangle((1,1,7,7), fill="red")

if __name__ == "__main__":
    try:
        main("Hola mundo de la electronica en el internet de todas las cosas", cascaded=1, block_orientation=90, rotate=0)
    except KeyboardInterrupt:
        pass


