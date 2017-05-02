
# -*- coding: utf-8 -*-

from light import *
from Reader import *
from Sensor import *

def main():
    data = []#データ配列
    light = []
    sensor = []
    cd = 0
    lx = 0
    hcd = 50
    flag = 0
    data = reader()

    #初期値設定
    for num in range(15):
        light.append(Light(num,cd,hcd))

    for num in range(97):
        sensor.append(Sensor(num,lx))
    # print light[0].hcd
    # print data[1]

    #照明の値変更
    # Light.setcd(light[1])
    # print light[1].cd

if __name__=='__main__':
    main()


# print list[1]
# for w in list:
#     print (w)
