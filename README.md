# Image concatenation.  

I can't find how to concatenate images using cv2 or PIL.  

Although in jupyter, using plt.subplot it's possible.  

However is there any method to save such concatenated images??  

Let me know if someone knows how to do.  

I think I will use it a lot later, so pushed here.  

I used only numpy and cv2.  

And just slicing numpy.array I concatenated such images.  

Note that results will be very large to preserve the originals.  
Because original result is too large, 4 more version will be saved and one can set interpolatrion mode  

`python concat.py --w 10 --h 6 --resize True`  

### Make sure all images will be concatenated must have same sizes.  
And they have to colored images. If not change code, 3 -> 1  
