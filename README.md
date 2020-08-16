# VID-ART
 _Creating an image from an input video's frames_
## Install

This project uses [NumPy](https://numpy.org) and [cv2](https://opencv.org). Go check them out if you don't have them locally installed.

```sh
pip install numpy
```

```sh
pip install cv2
```
## How does it work?

This program uses an input video and then it creates an image from every frame of the input video. Every vertical bar of the output image has a color that is calculated from the average color of each pixel of the frame. for example, we use this video as an input for our program(You can click on the image to watch it!):

[![IMAGE ALT TEXT HERE](https://cdn.discordapp.com/attachments/732234196487241741/744582984539046008/unknown.png)](https://www.youtube.com/watch?v=9yD0KEi554c)

After the video starts playing, besides the original video we can simultaneously see the frame average color and also the frame number:

<p align="center">
 <img src="https://cdn.discordapp.com/attachments/732234196487241741/744586216405598258/unknown.png">
</p>

This means that in the 88th frame of the video, the average color is `(124,119,139)` or ![#7C7788](https://via.placeholder.com/15/7C7788/000000?text=+) `#7C7788`; so the 88th vertical bar in the final picture has the color of `#7C7788`!

After the program detects all of the frames of the video and saves the average colors in a 2D array, then we can create our art:)
<p align="center">
 <img src="https://cdn.discordapp.com/attachments/732234196487241741/744590609943363604/only-man.jpg">
</p>
