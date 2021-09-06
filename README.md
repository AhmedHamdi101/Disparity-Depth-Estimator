# Disparity-Depth-Estimator

Implement and testing of stereo algorithms, in each case I take two images Il and Ir (a left and a right image) and compute the horizontal disparity (ie., shift) of pixels along each scanline. This is the so-called baseline stereo
case, where the images are taken with a forward-facing camera, and the translation betwee cameras is along the horizontal axis.
To get the disparity value at each point in the left image, I search over a range disparities, and compare the windows using two different metrics: Sum of Absolute Differences (SAD) and
Sum of Squared Differences. I did this for windows of size w where w = 1, 5 and 9. 

### Input Example
The left image input: &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  The right image input:

![scene_l](https://user-images.githubusercontent.com/62859032/132206407-9120cb96-3352-4c2d-b6dd-1e99803a5168.jpg)
![scene_r](https://user-images.githubusercontent.com/62859032/132206456-98ec76ad-f549-4983-b27a-76f122d29843.jpg)

I used the numpy, openCV and matplotlib APIs 

