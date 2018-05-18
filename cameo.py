import cv2
from managers import WindowManager, CaptureManager


class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(
            cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        '''
        主函数循环
        '''
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            '''
            进入帧
            '''
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            '''
            目标：处理帧
            '''

            '''
            结束帧
            '''
            self._captureManager.exitFrame()
            self._windowManager.preocessEvent()

    def onKeypress(self, keycode):
        '''
        监测按键
        SPACE 截屏
        TAB   开始/停止录制视频
        ESC   退出
        '''

        if keycode == 32:  # SPACE
            self._captureManager.writeImage('screenshot.png')

        elif keycode == 27:  # ESC
            self._windowManager.destroyWindow()


if __name__ == "__main__":
    Cameo().run()
