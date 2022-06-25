import os
import subprocess

INPUT_DIR = "graphics"
OUTPUT_DIR = "reexported_graphics"
DPI = 300
WIDTH = 294
HEIGHT = 76

file_list = os.listdir(INPUT_DIR)
for file in file_list:
    file_path = os.path.join(INPUT_DIR, file)
    export_path = os.path.join(OUTPUT_DIR, file)

    # subprocess.call(["inkscape", "--export-filename={0}".format(export_path), "-w", str(
    #     WIDTH), "-h", str(HEIGHT), "-d", str(DPI), file_path], shell=True)

    subprocess.call(["inkscape", "--export-filename={0}".format(export_path), "-d", str(DPI), file_path], shell=True)
