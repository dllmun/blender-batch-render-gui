# Blender Batch Render GUI
Graphical user interface for quickly writing blender batch render files

## How to use:
1. download & run blender_batch_render_gui.exe (alternatively run the blender_batch_render_gui.py file yourself)
2. ignore Windows warnings (Windows flags all unknown software as potentially dangerous)
3. select your blender version folder (only needed when using the program for the first time or when changing blender versions otherwise the program will save this information)
4. add blend files (press the "( + )  ADD BLEND FILES" button and select as many blend files as you like)
5. remove unwanted blend files if you made a mistake or changed your mind (simply select the files in the preview and press the "( - )  REMOVE BLEND FILES" button)
6. repeat step 4 & 5 as many times as you like
7. decide if you want the cmd window to close after the rendering process is finished (the cmd window will not be closed by default)
8. export the bat file (choose a folder as export location)
9. curse my questionable code if you encounter the error window & check if you have writing permissions (Error, Program failed to export .bat file. <- this will also show when you cancel the export in which case you simply ignore it)
10. locate your bat file and run it

(using tkinter, tested for Windows 10)
