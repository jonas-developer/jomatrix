#!/usr/bin/env python
# Display a runtext with double-buffering.
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time


def run(self):
    options = RGBMatrixOptions()

    options.hardware_mapping = "adafruit-hat"
    options.rows = 32
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.row_address_type = 0
    options.multiplexing = 0
    options.pwm_bits = 11
    options.brightness = 80
    options.pwm_lsb_nanoseconds = 130
    options.led_rgb_sequence = "RGB"
    options.pixel_mapper_config = ""
    options.panel_type = ""

    # options.show_refresh_rate = 1
    # options.gpio_slowdown = 1
    # options.disable_hardware_pulsing = True
    # options.drop_privileges=False

    matrix = RGBMatrix(options = options)
    offscreen_canvas = matrix.CreateFrameCanvas()
    font = graphics.Font()
    font.LoadFont("./fonts/7x13.bdf")
    textColor = graphics.Color(255, 255, 0)
    pos = offscreen_canvas.width
    my_text = self.args.text

    while True:
        offscreen_canvas.Clear()
        len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
        pos -= 1
        if (pos + len < 0):
            pos = offscreen_canvas.width

        time.sleep(0.05)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
