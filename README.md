# VID-ART
 > _Creating an image from an input video's frames_
  
## Table of Contents

- [Install](#Install)
- [How does it work](#How-Does-It-Work)
  - [Frame information](#Frame-information)
  - [Timeline](#timeline)
  - [Output](#output)
- [Other examples](#Other-Examples)

---

### Install

This project uses [NumPy](https://numpy.org), [tkinter](https://docs.python.org/3/library/tkinter.html) and [cv2](https://opencv.org). Go check them out if you don't have them locally installed.

```sh
pip install numpy
```

```sh
pip install tkinter
```

```sh
pip install cv2
```
---

### How does it work?

This program uses an input video and then it creates an image from every frame of the input video. Every vertical bar of the output image has a color that is calculated from the average color of each pixel of the frame. for example, we use this video as an input for our program(You can click on the image to watch it!):

[![sample-video](https://cdn.discordapp.com/attachments/732234196487241741/744582984539046008/unknown.png)](https://www.youtube.com/watch?v=9yD0KEi554c)

#### Frame information:

After the video starts playing, besides the original video we can simultaneously see the frame average color and also the frame number:

<p align="center">
 <img src="https://cdn.discordapp.com/attachments/732234196487241741/744586216405598258/unknown.png" alt="frame-info" width="200" height="">
</p>

This means that in the 88th frame of the video, the average color is `(124,119,139)` or ![#7C7788](https://via.placeholder.com/15/7C7788/000000?text=+) `#7C7788`; so the 88th vertical bar in the final picture has the color of `#7C7788`!

#### Timeline

You can also watch the process of the program in the timeline frame:
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/732234196487241741/744799641165496420/ezgif-7-d2c914fb3566.gif" alt="timeline" width="2000" height="200">
</p>

#### Output:

After the program detects all of the frames of the video and saves the average colors in a 2D array, then we can create our art:)
<p align="center">
 <img src="https://cdn.discordapp.com/attachments/732234196487241741/744590609943363604/only-man.jpg" alt="vid-art" width="2000" height="100">
</p>

> ℹ For enhancing the speed of the process, you can comment the **frame color** and **timeline** sections.
---

### Other examples:
Here are some other pictures that are created from other input videos:

<!--
###### _Family Guy: Season 11, Episode 4_
<p align="center">
 <img src="https://cdn.discordapp.com/attachments/732234196487241741/744804843801149480/unknown.png" alt="vid-art" width="2000" height="100">
</p>

###### _Rick and Morty: Season 4, Episode 9_
<p align="center">
 <img src="https://cdn.discordapp.com/attachments/732234196487241741/744815071296749648/VID-ART.jpg" alt="vid-art" width="2000" height="100">
</p>

###### _Money Heist: Season 3, Episode 1_
<p align="center">
 <img src="https://cdn.discordapp.com/attachments/732234196487241741/744831064752652298/VID-ART.jpg" alt="vid-art" width="2000" height="100">
</p>

-->

<details><summary> Family Guy: Season 11, Episode 4 </summary>
<p>
<p align="center">
 <img src="https://cdn.discordapp.com/attachments/732234196487241741/744804843801149480/unknown.png" alt="vid-art" width="2000" height="100">
</p>
</p>
</details>


<details><summary> Rick and Morty: Season 4, Episode 9 </summary>
<p>
<p align="center">
 <img src="https://cdn.discordapp.com/attachments/732234196487241741/744815071296749648/VID-ART.jpg" alt="vid-art" width="2000" height="100">
</p>
</p>
</details>


<details><summary> Money Heist: Season 3, Episode 1 </summary>
<p>
<p align="center">
 <img src="https://cdn.discordapp.com/attachments/732234196487241741/744831064752652298/VID-ART.jpg" alt="vid-art" width="2000" height="100">
</p>
</p>
</details>
