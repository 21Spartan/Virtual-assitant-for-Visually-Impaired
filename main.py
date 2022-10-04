import image
import video

print('1. Image 2.Video')
x=int(input())

if x == 1:
    image.read()
elif x == 2:
    video.detect()
    
