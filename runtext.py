#!/usr/bin/env python
# Display a runtext with double-buffering.
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time


def run(text):
    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 64
    matrix = RGBMatrix(options=options)
    offscreen_canvas = matrix.CreateFrameCanvas()
    font = graphics.Font()
    font.LoadFont("./fonts/7x13.bdf")
    textColor = graphics.Color(255, 255, 0)
    pos = offscreen_canvas.width
    my_text = text

    while True:
        offscreen_canvas.Clear()
        len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
        pos -= 1
        if (pos + len < 0):
            pos = offscreen_canvas.width

        time.sleep(0.05)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
