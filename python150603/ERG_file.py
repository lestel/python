__author__ = 'estel'
def my_ERG_operations(image,way,thea):
    import cv2
    import numpy
    import math
    image_tmp=image
    image_size1=image_tmp.shape[1]
    image_size0=image_tmp.shape[0]
    kernal=numpy.array([(1,1,1), (1,1,1), (1,1,1)],numpy.uint8)
    kernal_small=numpy.array([(0,1,0), (1,1,1), (0,1,0)],numpy.uint8)
    if way==1:#edge detection
       word='edge detection'
       if thea==1:
          result_tmp= cv2.dilate(image_tmp,kernal)-cv2.erode(image_tmp,kernal)
       elif thea==2:
          result_tmp= cv2.dilate(image_tmp,kernal)-image_tmp
       elif thea==3:
          result_tmp= image_tmp-cv2.erode(image_tmp,kernal)
       result=result_tmp
    elif way==2:#Morphological Reconstruction
       word='Morphological Reconstruction grayscale'
       result_tmp= cv2.erode(image_tmp,kernal)
       result_M= cv2.dilate(result_tmp,kernal)


       result_T=result_M
       result_M=cv2.dilate(result_M,kernal_small)
       for i in range(image_size0):
           for j in range(image_size1):
               if result_M[i,j]>image_tmp[i,j]:
                  result_M[i,j]=image_tmp[i,j]

       result=numpy.zeros((image_tmp.shape[0],image_tmp.shape[1]),numpy.uint8)
       while sum(sum(result_M-result_T))!=0:
             result_T=result_M
             result_M=cv2.dilate(result_M,kernal_small)
             for i in range(image_size0):
                 for j in range(image_size1):
                     if result_M[i,j]>image_tmp[i,j]:
                        result_M[i,j]=image_tmp[i,j]
       result=result_M
    elif way==3:#Morphological gradient
       word='Morphological gradient'
       if thea==1:
          result_tmp= cv2.dilate(image_tmp,kernal)-cv2.erode(image_tmp,kernal)
       elif thea==2:
          result_tmp= cv2.dilate(image_tmp,kernal)-image_tmp
       elif thea==3:
          result_tmp= image_tmp-cv2.erode(image_tmp,kernal)
       result=result_tmp*0.5
    return result,word



