import os,csv
import sys
import numpy as np
from PIL import Image,ImageDraw,ImageFont

def csv2image(csvname):
  np.set_printoptions(threshold=np.inf)
  with open(csvname) as f:
    reader = csv.reader(f)
    for row in reader:
      mytime = row[0]
      mytime_hour = int(mytime[0:2])
      mytime_minute = int(mytime[3:5])
      mytime_int = mytime_hour * 60 + mytime_minute

      text = row[1]
      text_split = text.split("\n")
      clocksize = len(text_split) - 1
      img = Image.new("RGB", (clocksize*12, clocksize*12), (255,255,255))
      draw = ImageDraw.Draw(img)
      for i in range(clocksize):
        draw.text((0,i*12),text_split[i],(0,0,0))
      img = img.resize((80,80))

#      imgFileName = sys.argv[2]
#      img.save(imgFileName)

  return img

