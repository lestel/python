__author__ = 'estel'
import cv2
import numpy
import math

#===+
def my_drawHist(hist):
        img = numpy.zeros((256,256),numpy.uint8)
        r = max(hist)/255
        for i in range (0,256):
            hist[i] = hist[i]/r
            cv2.line(img,(i,255),(i,255-hist[i]),255)
        return img
#====

def my_OSTU_getThres(gray):
        maxV=0
        bestTh=0
        w=[0 for i in range(len(gray))]
        px=[0 for i in range(len(gray))]
        w[0]=gray[0]
        px[0]=0
        for m in range(1,len(gray)):
            w[m]=w[m-1]+gray[m]
            px[m]=px[m-1]+gray[m]*m
        for th in range(len(gray)):
            w1=w[th]
            w2=w[len(gray)-1]-w1
            if(w1*w2==0):
                 continue
            u1=px[th]/w1
            u2=(px[len(gray)-1]-px[th])/w2
            v=w1*w2*(u1-u2)*(u1-u2)
            if v>maxV:
                 maxV=v
                 bestTh=th
        return bestTh
    #====
def my_Entropy_getThres(gray):

        bestTh_array=numpy.zeros([len(gray),1],numpy.int32)
        for t in range(len(gray)):
            sum_o=0
            sum_b=0
            if gray[t]!=0:
                for i in range(t+1):

                    tmp_o=(float(gray[i]))/(gray[t])
                    if gray[i]!=0:
                       value_o=math.log(tmp_o)*tmp_o
                       sum_o=sum_o+value_o

                for j in range(t+1,len(gray)):
                    tmp_b=(float(gray[j]))/(sum(gray)-gray[t])
                    if gray[j]!=0:
                       value_b=math.log(tmp_b)*tmp_b
                       sum_b=sum_b+value_b
                bestTh_array[t]=-1*(sum_o+sum_b)
            else:
                bestTh_array[t]=-9999
        index=0
        first_num=bestTh_array[index,0]
        while first_num!=numpy.max(bestTh_array):
               index=index+1
               first_num=bestTh_array[index,0]
        bestTh=index
        return bestTh





                  #####??????????????????????????????????