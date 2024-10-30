import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

# 仅输入一个文件名 字体随机 
if (len(sys.argv) == 1):
    font = random.choice(fonts)
elif (len(sys.argv) == 3):
    if (sys.argv[1] != "-f" or sys.argv[1] != "-font"):
        print("Invalid usage")
        sys.exit
    elif (sys.argv[2] not in fonts):
        print("Invalid usage")
        sys.exit
    font = figlet.setFont(font = sys.argv[2])
else:
    print("Invalid usage")
    sys.exit

str = input("Input: ")
print(figlet.renderText(str))