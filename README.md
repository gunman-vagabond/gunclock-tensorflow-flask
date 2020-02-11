# ガンマン時計読取りAI

tensorflow でガンマン時計を読取ります。
flaskでWebAP化しました。

## 導入方法

    $ git clone https://github.com/gunman-vagabond/gunclock-tensorflow-flask.git
    $ wget http://titech.sakura.ne.jp/ryutmp/model.ckpt.data-00000-of-00001 -O gunclock-tensorflow-flask/models/model.ckpt.data-00000-of-00001
    $ pip install -r gunclock-tensorflow-flask/requirements.txt
    $ cd gunclock-tensorflow-flask; python index.py  

## アクセス(例)

    http://xxxxxxx:18080/gunclockPrediction


## colaboratoryに仕込んだ例

    https://colab.research.google.com/drive/1bp9fnzLaF6EIAB2jkCvNs1L1_DNDJRFO?authuser=3&hl=ja#scrollTo=WVFjnwJR0daE

