# Disparity-Depth-Estimator

Implement and testing of stereo algorithms, in each case I take two images Il and Ir (a left and a right image) and compute the horizontal disparity (ie., shift) of pixels along each scanline. This is the so-called baseline stereo
case, where the images are taken with a forward-facing camera, and the translation betwee cameras is along the horizontal axis.
To get the disparity value at each point in the left image, I search over a range disparities, and compare the windows using two different metrics: Sum of Absolute Differences (SAD) and
Sum of Squared Differences. I did this for windows of size w where w = 1, 5 and 9. 
