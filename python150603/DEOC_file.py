__author__ = 'estel'
def my_DEOC_operations(image,way,k1,iterations):
    #i give up
    import cv2
    import numpy
    import math
    image_tmp=image
    if way==1:
       result=image_tmp
       for i in range(iterations):#Eroded
             result= cv2.erode(result,k1)
       word='Eroded Image'
    elif way==2:
       result=image_tmp
       for i in range(iterations):#Dilated
          result= cv2.dilate(result,k1)
       word='Dilated Image'
    elif way==3:
       result=image_tmp
       for i in range(iterations):#open
          result= cv2.erode(result,k1)
          result= cv2.dilate(result,k1)
       word='Open Image'
    elif way==4:
       result=image_tmp
       for i in range(iterations):#close
          result= cv2.dilate(result,k1)
          result= cv2.erode(result,k1)
       word='Close Image'
    return result,word


