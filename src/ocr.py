import sys
sys.path.append(r"C:\\Users\\Mayank\\Documents\\Project\\Personal\\Python\\WordSegmentation\\src")
# sys.path.append(r"C:\\Users\\Mayank\\Documents\\Project\\Personal\\Python\\SimpleHTR\\src")
from main import ocr
import os
import argparse
from split import split

wordSegmentationPath = "C:/Users/Mayank/Documents/Project/Personal/Python/WordSegmentation"
ocrPath = "C:/Users/Mayank/Documents/Project/Personal/Python/SimpleHTR"

total_count = split(wordSegmentationPath)
print("Word Count = %s"%total_count)

directory = wordSegmentationPath + "/out/"
for dirname in os.listdir(directory):
    for filename in os.listdir(directory + dirname):
        if filename.endswith(".png"): 
            print(ocr(directory + dirname + "/" + filename, ocrPath), end=" ")
    print("\n")