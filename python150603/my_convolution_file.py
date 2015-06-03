__author__ = 'estel'
def my_convolution(image, kernal):

    import numpy
    image_tmp=image
    image_size1=image_tmp.shape[1]
    image_size0=image_tmp.shape[0]
    kernal_size0=kernal.shape[0]
    kernal_size1=kernal.shape[1]
    if (kernal_size0!=kernal_size1  or image_size0<=kernal_size0):
        print "Error: import wrong"
        result=[]
    else:
        result_tmp=image_tmp.astype(numpy.int32)
        if (kernal_size0%2)==1:
      # odd
            left_d=(kernal_size0-1)/2
            right_d=(kernal_size0-1)/2

            for i in range(1-1+left_d,image_size0-1-right_d+1,1):
                for j in range(1-1+left_d,image_size1-1-right_d+1,1):
                   tmp_block=image_tmp[(i-left_d):(i-left_d+kernal_size0),(j-left_d):(j-left_d+kernal_size1)]
                   tmp_pix=sum(sum(tmp_block*kernal))
                   result_tmp[i,j]=tmp_pix
        else:
         # even
            left_d=kernal_size0/2-1
            right_d=kernal_size0-1-left_d

            for i in range(1-1+left_d,image_size0-1-right_d+1,1):
                for j in range(1-1+left_d,image_size1-1-right_d+1,1):
                    tmp_block=image_tmp[(i-left_d):(i-left_d+kernal_size0),(j-left_d):(j-left_d+kernal_size1)]
                    tmp_pix=sum(sum(tmp_block*kernal))
                    result_tmp[i,j]=tmp_pix
    result=result_tmp
    return result


