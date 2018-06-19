'''
Created on Aug 28, 2017

@author: root
'''

import datetime
from picamera import PiCamera

FOLDER_BASE = '/home/pi/pictures/'
FILENAME_BASE = "photo_"

class Camera:

    def __init__( self, folderBase, filenameBase ):
        # initialize class variables
        self.camera = PiCamera()
	self.camera.hflip = True
	self.camera.vflip = True

	self.folderBase = folderBase
	self.filenameBase = filenameBase

    def close( self ):

	self.camera.close()

    def takePicture( self ):
        # take picture
        now = datetime.datetime.now()
        filename = "%s/%s%d%02d%02d_%02d%02d%02d.jpg" % (self.folderBase, self.filenameBase, now.year, now.month, now.day, now.hour, now.minute, now.second)
        
        self.camera.capture( filename )

class CameraTest:

	def runTest( self ):
		camera = Camera( FOLDER_BASE, FILENAME_BASE )
		camera.takePicture()

#//////////////////////////////////////////////////////////////////////////////
#// main()
#//////////////////////////////////////////////////////////////////////////////

def main():
	test = CameraTest()
	test.runTest()
	

if __name__ == '__main__':
    main()

