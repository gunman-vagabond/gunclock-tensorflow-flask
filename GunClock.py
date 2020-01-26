import math
import datetime
from pytz import timezone

class GunClock:

  gunClock = []

  class Cast:
    def __init__(self, image):
      self.image = image
  
    def display(self, x, y):
      global gunClock
      _x = int((x * 2) - ( len(self.image[0]) / 2 ))
      _y = int(y - ( len(self.image) /2 ))
      for i in range (0, len(self.image)):
        for j in range (0, len(self.image[i])):
          c = self.image[i][j]
          if c != "*" and (_x + j)>=0 and (_y + i) >=0 :

            tmp = GunClock.gunClock[_y + i]
            tmp_list = list(tmp)
            tmp_list[_x + j] = c
            GunClock.gunClock[_y + i] = "".join(tmp_list)


  def __init__(self, gunClockSize, gunClockTime="", timezone='Asia/Tokyo', hourStr='', minuteStr='', digitalTime='yes'):
    self.clockSize = gunClockSize
    self.clockTime = gunClockTime
    self.hourStr = hourStr
    self.minuteStr = minuteStr
    self.timezone = timezone
    self.digitalTime = digitalTime
    self.centerX = int(self.clockSize / 2);
    self.centerY = int(self.clockSize / 2);

    GunClock.gunClock = []
    for i in range(0, self.clockSize):
      GunClock.gunClock.append(" "*self.clockSize*2)

    self.createGunClock()

  def createGunClock(self):

    gunman = self.Cast([
      "** __ *", 
      " _|__|_",
      "b (@@) ",
      " V|~~|>",
      "* //T| "
    ])

    inu = self.Cast([
      "__AA  **",
      "| 6 |__P",
      "~~|    l",
      "*/_/~l_l"
    ])

    if self.hourStr == "" and self.minuteStr == "":
      (hour, minute, second) = self.getTime()
    else :
      hour = int(self.hourStr)
      minute = int(self.minuteStr)
      second = 0

    self.gunmanX = self.centerX + math.cos(self.hourToRadian(hour, minute)) * (self.clockSize * 2/3/2)
    self.gunmanY = self.centerY - math.sin(self.hourToRadian(hour, minute)) * (self.clockSize * 2/3/2)
    self.inuX = self.centerX + math.cos(self.minuteToRadian(minute, second)) * (self.clockSize * 4/5/2) 
    self.inuY = self.centerY - math.sin(self.minuteToRadian(minute, second)) * (self.clockSize * 4/5/2) 

    self.wakuDisplay( self.Cast(["+"]) )
    self.numDisplay( self.Cast(["3"]), self.Cast(["6"]), self.Cast(["9"]), self.Cast(["12"]) )
    self.longHandDisplay( self.Cast(["##"]) )
    self.shortHandDisplay( self.Cast(["::"]) )

    inu.display(self.inuX, self.inuY)
    gunman.display(self.gunmanX, self.gunmanY)
    if self.digitalTime == 'yes' :
      self.digitalTimeDisplay(hour, minute, second)

  def getTime(self):
    if ( self.clockTime == "" ):
#      now = datetime.datetime.now()
#      now = datetime.datetime.now(timezone('Asia/Tokyo'))
      now = datetime.datetime.now(timezone(self.timezone))
      return (now.hour, now.minute, now.second)
#      jst_now = timezone('Asia/Tokyo').localize(now)
#      return (jst_now.hour, jst_now.minute, jst_now.second)
    else:  # self.clockTime : (ex)12:34
#      print self.clockTime
#      print self.clockTime[0:2]
#      print self.clockTime[3:5]
      return ( int(self.clockTime[0:2]), int(self.clockTime[3:5]), 0)

  def wakuDisplay(self, waku):
    for i in range(0,360,30):
      if ( i % 90 == 0 ):
        continue

      radian = ( i * 2 * math.pi ) / 360
      wakuXdiff = self.clockSize/2 * math.cos(radian)
      wakuYdiff = self.clockSize/2 * math.sin(radian)

      if ( wakuXdiff >= 0 ) :
        wakuX = self.centerX + math.floor(wakuXdiff)
      else:
        wakuX = self.centerX + math.ceil(wakuXdiff)

      if ( wakuYdiff >= 0 ) :
        wakuY = self.centerY + math.floor(wakuYdiff)
      else:
        wakuY = self.centerY + math.ceil(wakuYdiff)

#    print "%s %s" % (wakuX , wakuY)

      waku.display(wakuX, wakuY)

  def numDisplay(self, num3, num6, num9, num12):
    num3.display(self.clockSize - 1, self.centerY)
    num6.display(self.centerX, self.clockSize - 1)
    num9.display(0, self.centerY)
    num12.display(self.centerX, 0)

  def longHandDisplay(self, longHand):
    for i in range(0,int(self.clockSize*2/3/2)):
      longHandX = self.centerX + ( ( (self.inuX - self.centerX) * i ) / (self.clockSize*2/3/2) )
      longHandY = self.centerY + ( ( (self.inuY - self.centerY) * i ) / (self.clockSize*2/3/2) )
      longHand.display(longHandX, longHandY)

  def shortHandDisplay(self, shortHand):
    for i in range(0,int(self.clockSize*5/6/2)):
      shortHandX = self.centerX + ( ( (self.gunmanX - self.centerX) * i ) / (self.clockSize*5/6/2) )
      shortHandY = self.centerY + ( ( (self.gunmanY - self.centerY) * i ) / (self.clockSize*5/6/2) )
      shortHand.display(shortHandX, shortHandY)

  def digitalTimeDisplay(self, hour, minute, second):
    digitalTime = self.Cast ([
#    "__________",
#    "|" + ("%02d:%02d:%02d" % (hour, minute, second) ) + "|" ,
#    "~~~~~~~~~~"
      "_______",
      "|" + ("%02d:%02d" % (hour, minute) ) + "|" ,
      "~~~~~~~"
    ])
    digitalTimeRadian = self.digitalRadian(hour,minute,second)
    digitalTime.display(
      self.centerX + (math.cos(digitalTimeRadian) * self.clockSize/2 * 1/2),
      self.centerY - (math.sin(digitalTimeRadian) * self.clockSize/2 * 1/2)
    )

  def digitalRadian(self, h, m, s):
    hRadian = self.hourToRadian(h, m)
    mRadian = self.minuteToRadian(m, s)
    aveRadian = (hRadian + mRadian) / 2
    if ( ( (hRadian > mRadian) and (hRadian - mRadian < math.pi) )
      or ( (mRadian > hRadian) and (mRadian - hRadian < math.pi) ) ) :
      return aveRadian + math.pi
    else :
      return aveRadian
 
  def hourToRadian(self, h, m):
    return math.pi * ( 90.0 - ( (h%12) + m/60 ) * 30 ) / 180.0

  def minuteToRadian(self, m, s):
    return math.pi * ( 90.0 - ( m + s/60 ) * 6 ) / 180.0

  def toString(self):
    retstr = "" 
    for i in range(0, len(GunClock.gunClock)):
#    retstr += ("%02i" % i) + ": \'"  + gunClock[i] + "\'\n"
       retstr += GunClock.gunClock[i] + "\n"
    return retstr

