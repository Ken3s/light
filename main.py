
# -*- coding: utf-8 -*-
import random
from light import *
from Reader import *
from Sensor import *

def main():
    data = []#データ配列
    light = []
    sensor = []
    SENSOR_NUM = 97
    LIGHT_NUM = 15
    minlight = [0 for i in range(SENSOR_NUM)]
    minsensor = [0 for i in range(SENSOR_NUM)]
    COUNT = 10000
    Weight = 1
    cd = 0.0#初期照明光度
    lx = 0.0
    hcd = 50.0
    flag = 0.0
    hlx = 0.0
    g = [0 for i in range(SENSOR_NUM)]
    data = reader()
    # print data
    # print len(data)

    del data[0:16]
    c=0
    for i in range(SENSOR_NUM):
        c = i * LIGHT_NUM
        # print (data[c])
        del data[c]
    # print data

    #初期値設定
    for num in range(LIGHT_NUM):
        light.append(Light(num,cd,hcd))

    for num in range(SENSOR_NUM):
        sensor.append(Sensor(num,lx,hlx))

    #目標照度設定
    locationa = 21
    locationb = 79
    locationc = 96
    sensor[locationa].set_lx(500);
    sensor[locationb].set_lx(500);
    sensor[locationc].set_lx(500);
    # print light[0].hcd
    # print data[1]


    #照明の値変更
    # Light.setcd(light[1])
    # print light[1].cd
    min =99999999
    for k in range(COUNT):
        #初期化
        for j in range(SENSOR_NUM):
            sensor[j].lx =0
        P = 0
        s = 0

        for i in range(LIGHT_NUM):
            light[i].cd = random.randint(0,1000)

        #照度，光度変換
        for j in range(SENSOR_NUM):
            if j ==locationa or j == locationb or j == locationc:
                for i in range(LIGHT_NUM):
                    sensor[j].lx += light[i].cd * float(data[i+LIGHT_NUM*j])

        for i in range(SENSOR_NUM):
            if i ==locationa or i == locationb or i == locationc:
                tmp = (sensor[i].lx - sensor[i].hlx)
                if tmp >= 0:
                    g[i] = 0
                else:
                    g[i] =  tmp * tmp
            # print(i)
            # print (g[i])

        for i in range(LIGHT_NUM):
            P += light[i].cd
        for i in range(SENSOR_NUM):
            s += g[i]
        f = P + Weight * s

        # print (f)
        if COUNT == 0:
            min = f
            for i in range(LIGHT_NUM):
                minlight[i] = light[i].cd
            for i in range(SENSOR_NUM):
                minsensor[i] = sensor[i].lx

        if min>f:
            min = f
            for i in range(LIGHT_NUM):
                minlight[i] = light[i].cd
            for i in range(SENSOR_NUM):
                minsensor[i] = sensor[i].lx

    # print (min)

    # 最小値の時のセンサと照明の値
    for i in range(LIGHT_NUM):
        print (minlight[i])
    for i in range(SENSOR_NUM):
        if i ==locationa or i == locationb or i == locationc:
            print(minsensor[i])

if __name__=='__main__':
    main()


# print list[1]
# for w in list:
#     print (w)
