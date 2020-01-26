from flask import Flask, request, render_template
import datetime
from pytz import timezone
import requests
from io import BytesIO
from PIL import Image

from GunClock import GunClock
import clockString2image as cs2i
import gunmanpredict as gp

def gunclockPrediction(request):

    size = ""
    hour = ""
    minute = ""
    imgurl = ""
    doAI = ""
    doAI2 = ""
    gunClock = ""
    AIOut = ""
    AIOut2 = ""
    AIOut3 = ""
    hantei = ""

    if request.method == 'POST':
#    try:
        if 'size' in request.form:
          size = request.form['size']
        if 'hour' in request.form:
          hour = request.form['hour']
        if 'minute' in request.form:
          minute = request.form['minute']
        if 'imgurl_copy' in request.form:
          imgurl = request.form['imgurl_copy']
        if 'gunClock' in request.form:
          gunClock = request.form['gunClock']

#        doAI = request.form['doAI']
#        doAI2 = request.form['doAI2']

#    except:
#    else:
#        url = request.args.get('url', 'http://fc.jpn.org/ryuba/gunman/pic/Gunman.3Dmodel.jpg')

    if size == "" :
      size = "17"

    size_int = int(size)

    if hour == "" or minute == "" :
      now = datetime.datetime.now(timezone('Asia/Tokyo'))
      hour = ("0" + str(now.hour))[-2:]
      minute = ("0" + str(now.minute))[-2:]

    hour_int = int(hour)
    minute_int = int(minute)

    if ( hour_int > 12 ) :
      hour_int_diff12 = hour_int - 12
    else :
      hour_int_diff12 = hour_int + 12

    hour_diff12 = str(hour_int_diff12)

    if imgurl == "" :
      imgurl = "https://img.muji.net/img/item/4547315915217_1260.jpg"

    if 'doAI' in request.form :

      print ( gunClock )

      img = cs2i.clockString2image(gunClock)
      AIOut = gp.predict(img)

      print ( "[AIOut] " + AIOut )

      AIOut_hour_int = int(AIOut[0:2])
      print ( AIOut_hour_int )
      print ( "[AIOut 3:5 ] " + AIOut[3:5] )
      AIOut_minute_int = int(AIOut[3:5])

      hantei = "残念!正解は " + hour+":"+minute + " もしくは " + hour_diff12+":"+minute

      if ( hour_int % 12 == AIOut_hour_int % 12 ):
        if ( minute_int == AIOut_minute_int ) :
          hantei = "正解！"
        else :
          hantei = "おしい！正解は " + hour+":"+minute + " もしくは " + hour_diff12+":"+minute
      else :
        if ( minute_int == AIOut_minute_int ) :
          hantei = "おしい！正解は " + hour+":"+minute + " もしくは " + hour_diff12+":"+minute

    if 'doAI2' in request.form :
      imageDataResponse = requests.get(imgurl)
      img = Image.open(BytesIO(imageDataResponse.content))
      AIOut2 = gp.predict(img)

    img3filename="static/gray.jpg"
    if 'file' in request.files:
      file = request.files['file']
      img = Image.open(file)
      img3filename = "static/" + file.filename 
      img.save(img3filename);
      AIOut3 = gp.predict(img)

    if gunClock == "" :
      gunClock = GunClock(
                  gunClockSize=size_int,
                  timezone='Asia/Tokyo',
                  digitalTime='no',
                  hourStr = hour,
                  minuteStr = minute
               ).toString()

    return render_template(
        'gunclockPrediction.html', 
        size_int=size_int,
        hour=hour,
        minute=minute,
        gunClock=gunClock,
        AIOut=AIOut,
        hantei=hantei,
        imgurl=imgurl,
        AIOut2=AIOut2,
        AIOut3=AIOut3,
        img3filename=img3filename
    )
