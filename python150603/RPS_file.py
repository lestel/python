__author__ = 'estel'

def my_RPS_edge_detection(image,way):

    from my_convolution_file import my_convolution
    import numpy
    import cv2

    image_tmp=image.astype(numpy.int32)
    if way==1:
       kernal_x=numpy.array([(-1,0), (0,1)])
       kernal_y=numpy.array([(0,-1), (1,0)])
       Gx=my_convolution(image_tmp, kernal_x)
       Gy=my_convolution(image_tmp, kernal_y)
       tmp=Gx*Gx+Gy*Gy
       result_tmp=tmp**0.5
       word='Roberts Edge Detection'
       result=result_tmp.astype(numpy.uint8)
    elif way==2:
       kernal_x=numpy.array([(-1,-1,-1), (0,0,0), (1,1,1)])
       kernal_y=numpy.array([(-1,0,1), (-1,0,1), (-1,0,1)])
       Gx=my_convolution(image_tmp, kernal_x)
       Gy=my_convolution(image_tmp, kernal_y)
       tmp=Gx*Gx+Gy*Gy
       result_tmp=tmp**0.5
       word='Prewitt Edge Detection'
       result=result_tmp.astype(numpy.uint8)

    elif way==3:
       kernal_x=numpy.array([(-1,-2,-1), (0,0,0), (1,2,1)])
       kernal_y=numpy.array([(-1,0,1), (-2,0,2), (-1,0,1)])
       Gx=my_convolution(image_tmp, kernal_x)
       Gy=my_convolution(image_tmp, kernal_y)
       tmp=Gx*Gx+Gy*Gy
       result_tmp=tmp**0.5
       word='Sobel Edge Detection'
       result=result_tmp.astype(numpy.uint8)



    else:
       result=[]
       print "Error: choose way is not exist"

    return result,word
