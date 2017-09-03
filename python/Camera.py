'''
Created on Aug 28, 2017

@author: root
'''

import datetime
from picamera import PiCamera

FOLDER_BASE = '/home/pi/pictures/'
FILENAME_BASE = "photo_"

class Camera:

    def __init__(self):
        # initialize class variables
        self.camera = PiCamera()

    def takePicture(self):
        # take picture
        now = datetime.datetime.now()
        filename = "%s%s%d%02d%02d_%02d%02d%02d.jpg" % (FOLDER_BASE, FILENAME_BASE, now.year, now.month, now.day, now.hour, now.minute, now.second)
        
        self.camera.capture( filename )

class CameraTest:

	def runTest( self ):
		camera = Camera()
		camera.takePicture()

#//////////////////////////////////////////////////////////////////////////////
#// main()
#//////////////////////////////////////////////////////////////////////////////

def main():
	test = CameraTest()
	test.runTest()
	

if __name__ == '__main__':
    main()

