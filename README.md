# ImageStitcher
Script written by ChatGPT for gluing JPG&PNG images.

```
pip install pillow==9.5.0 tqdm pillow-avif-plugin
```

**USAGE: Drag and drop into the folder where the images to be glued are located and run .py**

V1 - Simply glues JPG and PNG in 1 row
![V1](https://raw.githubusercontent.com/CakeFlyCookie/ImageStitcher/main/Examples/v1.png)

V2 - Changes the size of all JPG and PNG to the smallest of the incoming ones, glues images no more than 5 in 1 row, the rest are moved to the next row. Signs in the middle-bottom with a filename without a file extension
![V2](https://github.com/CakeFlyCookie/ImageStitcher/blob/main/Examples/v2.png?raw=true)

V3 - Changes the size of all images in the folder to the smallest of the incoming ones, glues images no more than 5 in 1 row, the rest are moved to the next row. Signs in the middle-bottom with a filename without a file extension. Deletes itself after completion.
