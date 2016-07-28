#!/usr/bin/env python
# encoding: utf-8

import requests
import sys
import os
import base64
import json
import yaml
# 其他
# https://github.com/tesseract-ocr/tesseract
# https://github.com/tmbdev/ocropy
from os.path import expanduser,join

home = expanduser("~")
with open(join(home,".img2txt.yml")) as f:
    config = yaml.load(f)
    _apikey = config["apikey"]

_url = 'http://apis.baidu.com/apistore/idlocr/ocr'

def img_to_word(path):
    """
    # todo
    #将path下的所有jpg格式的图片中的问题识别为文本
    """
    #filename="test2.jpg"
    #output_filename = filename.split(".")[0]+"_words.txt"
    #output_file = open(output_filename,"w")
    headers = {}
    headers['content-type'] = 'application/x-www-form-urlencoded'
    headers['apikey'] =  _apikey
    payload = {}
    payload['fromdevice'] = "pc"
    payload['clientip'] = "10.10.10.0"
    payload['detecttype'] = "LocateRecognize"
    payload['languagetype'] = "CHN_ENG"
    payload['imagetype'] = "1"
    with open(path, "rb") as image_file:
        payload['image'] = base64.b64encode(image_file.read())

    r = requests.post(_url, data=payload, headers=headers)
    r_json = json.loads(r.text)
    #print r.text
    if r_json["errNum"] == "0":
        print("ok")
        for line in r_json["retData"]:
            print line["word"]
            #output_file.write(line["word"]+"\n")
        #output_file.close()
    else:
        print("error:{}".format(str(r_json["errNum"])))

def main():
    path = sys.argv[1]
    img_to_word(path)
