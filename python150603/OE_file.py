__author__ = 'estel'

    #====
def my_OE_thresholdoperation(image,way,value):
    import cv2
    import numpy
    import math



    image_tmp=image

    numGray1=cv2.calcHist([image_tmp],[0],None, [256],[0.0,255.0])
    numGray=numGray1.astype(numpy.uint8)
    from DOE_file import my_drawHist
    histogram=my_drawHist(numGray1)
    if way==1:
       from DOE_file import  my_OSTU_getThres
       bestTh=my_OSTU_getThres(numGray)
       word='OSTU'
    elif way==2:
       from DOE_file import  my_Entropy_getThres
       bestTh=my_Entropy_getThres(numGray)
       word='Entropy'
    elif way==3:
       bestTh=value
       word='Manual'
    image_size1=image_tmp.shape[1]
    image_size0=image_tmp.shape[0]
    result_tmp=numpy.zeros([image_size0,image_size1],numpy.int32)

    for i in range(image_size0):
        for j in range(image_size1):
            if image_tmp[i,j]<=bestTh:
               result_tmp[i,j]=0
            else:
               result_tmp[i,j]=255


    result=result_tmp.astype(numpy.uint8)





    return result,histogram,word

