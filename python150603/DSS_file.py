__author__ = 'estel'

def my_DSS_operation(image,way):
    import cv2
    import numpy
    import math
    from OE_file import my_OE_thresholdoperation

    image_tmp,his_tmp,word_tmp=my_OE_thresholdoperation(image,1,0)
    image_tmp=image_tmp/255
    #image_tmp=numpy.array([(0,0,0,0,0,0,0), (0,1,1,1,1,1,0), (0,1,1,1,1,1,0),(0,1,1,1,1,1,0),(0,1,1,1,1,1,0)],numpy.uint8)
    image_size1=image_tmp.shape[1]
    image_size0=image_tmp.shape[0]

    itera=0

    kernal=numpy.array([(1,1,1), (1,1,1), (1,1,1)],numpy.uint8)
    kernal_small=numpy.array([(0,1,0), (1,1,1), (0,1,0)],numpy.uint8)

    if way==1:
        result=image_tmp
        result1=image_tmp
        result_tmp=image_tmp
        while sum(sum(result_tmp))!=0:
            result_tmp=cv2.erode(result_tmp,kernal)
            itera=itera+1
            result1=result1+result_tmp
        print itera

        result=result1
        word='Distance Transform'

    elif way==2:
        result1=numpy.zeros((image_tmp.shape[0],image_tmp.shape[1]),numpy.uint8)
        result_tmp=image_tmp
        result=result1
        while sum(sum(result_tmp))!=0:
            result_tmp=cv2.erode(result_tmp,kernal)
            tmp=cv2.erode(result_tmp,kernal_small)
            result_finopen=cv2.dilate(tmp,kernal_small)
            left_result=result_tmp-result_finopen
            itera=itera+1
            result1=result1+left_result
        print itera

        for i in range(image_size0):
            for j in range(image_size1):
                if result1[i,j]!=0:
                     result[i,j]=255

        word='Skeleton'

    elif way==3:
        result1=numpy.zeros((image_tmp.shape[0],image_tmp.shape[1]),numpy.uint8)
        result_tmp=image_tmp
        result=result1
        while sum(sum(result_tmp))!=0:
            result_tmp=cv2.erode(result_tmp,kernal)
            tmp=cv2.erode(result_tmp,kernal_small)
            result_finopen=cv2.dilate(tmp,kernal_small)
            left_result=result_tmp-result_finopen
            itera=itera+1
            result1=result1+cv2.dilate(left_result,kernal)
        print itera

        for i in range(image_size0):
            for j in range(image_size1):
                if result1[i,j]!=0:
                      result[i,j]=255
        word='Skeleton Reconstruction'
    elif way==4:
          result_tmp= cv2.erode(image_tmp,kernal)
          result_M= cv2.dilate(result_tmp,kernal)

          result_T=result_M
          result_M=cv2.dilate(result_M,kernal_small)
          result_M=result_M*image_tmp

          result=numpy.zeros((image_tmp.shape[0],image_tmp.shape[1]),numpy.uint8)

          while sum(sum(result_M-result_T))!=0:
             result_T=result_M
             result_M=cv2.dilate(result_M,kernal_small)
             result_M=result_M*image_tmp
          for i in range(image_size0):
            for j in range(image_size1):
                if result_T[i,j]!=0:
                     result[i,j]=255


          word='Morphological Reconstruction'


    return result,word