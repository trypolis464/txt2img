# txt2img
# Make images out of basic text.
#
# Copyright (C) 2020-2021, Ty Gillespie. All rights reserved.
# MIT License.

from PIL import Image, ImageDraw
from typing import Optional, Any


def generate(
    width: int,
    height: int,
    text: str,
    bg: Optional[str] = "white",
    text_x: Optional[int] = 10,
    text_y: Optional[int] = 10,
    fg: Optional[str] = "black",
    filename: Optional[str] = "image.png",
):
    """Generate an image.
    Parems:
        width: the width (in pixels), of the image.
        height: the height (in pixels) of the image.
        text: the text that goes on the image.
        bg (optional): the background color (by default white).
        text_x (optional): the top x of the text. By default 10.
        text_y (optional): the top y of the text. By default 10.
        fg (optional): the foreground color. By default black.
        filename (optional): the output filename (by default image.png).
    """
    i: Any = Image.new("RGB", (width, height), color=bg)
    d: Any = ImageDraw.Draw(i)
    d.text((text_x, text_y), text, fill=fg)
    i.save(filename)
