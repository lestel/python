__author__ = 'estel'

def my_MMB_NoiseReduction(image,way,size,value):
    import cv2
    import numpy
    import math
    image_tmp=image

    image_size1=image_tmp.shape[1]
    image_size0=image_tmp.shape[0]
    kernal_size0=size
    kernal_size1=size
    if  image_size0<=kernal_size0:
        print "Error: import wrong"
        result=[]
    else:
        result_tmp=image_tmp.astype(numpy.int32)
        if (kernal_size0%2)==1:
      # odd
            left_d=(kernal_size0-1)/2
            right_d=(kernal_size0-1)/2
        else:
      # even
            left_d=kernal_size0/2-1
            right_d=kernal_size0-1-left_d
        if  way==1:
            word='Mean Noise Reduction'
            kernal=numpy.ones([kernal_size0,kernal_size1])*1.0/9
            for i in range(1-1+left_d,image_size0-1-right_d+1,1):
                for j in range(1-1+left_d,image_size1-1-right_d+1,1):
                    tmp_block=image_tmp[(i-left_d):(i-left_d+kernal_size0),(j-left_d):(j-left_d+kernal_size1)]
                    tmp_pix=sum(sum(tmp_block*kernal))
                    result_tmp[i,j]=tmp_pix

        elif way==2:
            word='Median Noise Reduction'
            for i in range(1-1+left_d,image_size0-1-right_d+1,1):
                for j in range(1-1+left_d,image_size1-1-right_d+1,1):
                    tmp_block=image_tmp[(i-left_d):(i-left_d+kernal_size0),(j-left_d):(j-left_d+kernal_size1)]
                    tmp_block2=numpy.reshape(tmp_block,[kernal_size0*kernal_size1,1])
                    lst=sorted(tmp_block2)
                    if len(lst)%2==1:
                       tmp=lst[len(lst)//2]
                    else:
                       tmp=(lst[len(lst)//2-1]+lst[len(lst)//2])/2.0
                    tmp_pix=tmp[0]
                    result_tmp[i,j]=tmp_pix

        elif way==3:
            word='Gaussian Noise Reduction'
            if (kernal_size0%2)==1:
                ruler1=range(0-(kernal_size0-1)/2,0+(kernal_size0-1)/2+1,1)
            else:
                ruler1=range(0-(kernal_size0)/2+1,0+(kernal_size0)/2+1,1)
            Gaussian_kernel=numpy.ones([kernal_size0,kernal_size1],numpy.int32)*1.0
            for ii in range(0,kernal_size0,1):
                for jj in range(0,kernal_size1,1):
                    Gaussian_kernel[ii,jj]=1.0/2/math.pi/value/value*math.exp(-1.0*(ruler1[ii]*ruler1[ii]+ruler1[jj]*ruler1[jj])/2/value/value)

            for i in range(1-1+left_d,image_size0-1-right_d+1,1):
                for j in range(1-1+left_d,image_size1-1-right_d+1,1):
                    tmp_block=image_tmp[(i-left_d):(i-left_d+kernal_size0),(j-left_d):(j-left_d+kernal_size1)]
                    tmp_pix=sum(sum(tmp_block*Gaussian_kernel))
                    result_tmp[i,j]=tmp_pix

    result=result_tmp.astype(numpy.uint8)
    return result,word
