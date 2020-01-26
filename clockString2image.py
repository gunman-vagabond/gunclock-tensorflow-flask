import os,csv
import sys
import numpy as np
from PIL import Image,ImageDraw,ImageFont

def clockString2image(clockString):

  text = clockString 
  text_split = text.split("\n")
  clocksize = len(text_split) - 1
  img = Image.new("RGB", (clocksize*12, clocksize*12), (255,255,255))
  draw = ImageDraw.Draw(img)
  for i in range(clocksize):
    draw.text((0,i*12),text_split[i],(0,0,0))
  img = img.resize((80,80))

  return img

