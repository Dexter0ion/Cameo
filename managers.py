#-*-coding:utf-8-*-

import cv2
import numpy as np
import time


class CaptureManager(object):
    def __init__(self, capture, preiviewWindowManager=None, shouldMirrorPreview=False):
        self.preiviewWindowManager = preiviewWindowManager
        self.shouldMirrorPreview = shouldMirrorPreview

        self._capture = capture
        self._channel = 0
        self._enteredFrame = False

        self._frame = None
        self._imageFilename = None
        self._videoFilename = None
        self._videoENcoding = None
        self._videoWriter = None

        self._startTime = None
        self._frameElapsed = int(0)  # exchange long() to int()?
        self._fpsEstimate = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def chanel(self, value):
        if self._channel != value:
            self._channel = value
            self._frame = None

    @property
    def frame(self):
        if self._enteredFrame and self._frame is None:
            _, self._frame = self._capture.retrieve()  # what does retrieve() mean?
            return self._frame

    @property
    def isWritingImage(self):
        return self._imageFilename is not None

    @property
    def isWritingVideo(self):
        return self._videoFilename is not None

    def enterFrame(self):
        ''' Capture the next frame,if any.  
            捕获存在的下一帧
        '''
        # 首先检查先前帧是否存在
        assert not self._enteredFrame
        print("previous enterFrame had no matching exitFrame()")

        if self._capture is not None:
            self._enteredFrame = self._capture.grab()


def main():
    cm = CaptureManager(None)
    cm.enterFrame()
    print(cm.frame)
    print(cm.isWritingImage)
    print(cm.isWritingVideo)


if __name__ == '__main__':
    main()
