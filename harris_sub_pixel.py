#! /usr/bin/python3

'''
Sample Code for Sub Pixel Harris Corner Detector
'''

import cv2
import numpy as np
import os
import sys

def main():
    filename = 'sample.jpg'
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # find Harris corners
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    dst = cv2.dilate(dst,None)
    ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
    dst = np.uint8(dst)

    # find centroids
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

    # define the criteria to stop and refine the corners
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

    # Now draw them
    res = np.hstack((centroids,corners))
    res = np.int0(res)
    img[res[:,1],res[:,0]]=[0,0,255]
    img[res[:,3],res[:,2]] = [0,255,0]

    # Get Path and filename setup
    path = 'C:/Users/VIVTRIPATHI/Desktop/Projects/OpenCVLearn/output/'
    file_name = os.path.basename(sys.argv[0])

    cv2.imwrite(str(path)+'{0}.jpg'.format(file_name),img)

if __name__ == '__main__':
    main()