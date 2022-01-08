""" CHAPTER 1: Intro to Images/ Installation """

""" Image Resolution (in pixels)
VGA = 640 x 480
HD = 1280 x 720
FHD = 1920 x 1080
4K = 3840 x 2160

This means VGA has 640 boxes (pixels) as width or length and 480
(pixels) is the height of the box.

Currently the image we drew has only 2 colours i.e. white and 
black. This is known as an Binary Image, because it is stored
in Black and White i.e. 2 levels only.

0 - Black
1 - White

In real Life we will be using a 8 bit value i.e. 2^8 = 256 levels
(resolution) images.
0 - White
255 - Black   (254 colours btw white and black)

Gray Scale Image = 8 bits or 256 levels

For a coloured image we have 3 gray scaled images presenting the 
intensities of RGB colors. Adding these images gives us the full
color.

This means a coloured VGA image is 640x480x3 (3 channels - RGB)
"""