#-*-coding:utf-8-*-


class Screen(object):
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width*self._height


def main():
    s = Screen(1280, 1024)
    #s.width = 1280
    #s.height = 1024
    print(s.resolution)


if __name__ == '__main__':
    main()
