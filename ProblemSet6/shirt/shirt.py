import sys
import os
from PIL import Image, ImageOps

def main():
    end_name = [".jpeg", ".jpg", ".png"]
    if (len(sys.argv) < 3):
        sys.exit("Too few command-line arguments.")
    elif (len(sys.argv) > 3):
        sys.exit("Too many command-line arguments.")
    else:
        input_end = os.path.splitext(sys.argv[1])
        output_end = os.path.splitext(sys.argv[2])

        if ((input_end[1].lower() not in end_name) or (output_end[1].lower() not in end_name)):
            sys.exit("Not a jpeg/jpg/png file.")
        else:
            change(sys.argv[1], sys.argv[2])

def change(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask = shirt)
            input_cropped.save(output)

    except FileNotFoundError:
        sys.exit("File does not exit.")

if __name__ == "__main__":
    main()