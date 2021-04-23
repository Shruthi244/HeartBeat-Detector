# HeartBeat-Detector
# Identifying the face tone
The idea of determining the heart rate is that the skin tone changes slightly due to the blood flow in the vessels. So we need a picture crop, which contains only a fragment of the skin
# Image Processing
Once we have the camera stream, it’s pretty simple. For the selected image fragment, we get the average brightness value and add it to the array along with the measurement timestamp.
# Detecting the heart beat with the help of webcam
The numpy.average function calculates the average of a two-dimensional array, at the output, we get a number, which is the average brightness of our 100x100 square frame.

# Result
Even at this distance, the change in skin tone is confidently captured by the camera! As we can see from the graph, the real difference in brightness is less than 0.5% and, of course, it is not visible to the “naked eye”, but confidently distinguishable on the graph. The approximate pulse turned out to be about 75bpm.
