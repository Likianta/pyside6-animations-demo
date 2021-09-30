import sys

from PySide6.QtGui import QScreen
from PySide6.QtWidgets import *
from lk_logger import lk


class PrettyKwargs:
    
    def __init__(self, **kwargs):
        self.update(self.__dict__, kwargs)
    
    @staticmethod
    def update(main, additional):
        def _update(node: dict, subject: dict):
            for k, v in node.items():
                if isinstance(v, dict):
                    _update(v, subject[k])
                elif isinstance(v, list):
                    subject[k].extend(v)
                else:
                    subject[k] = v
        
        _update(additional, main)
        return main


class Application:
    
    def __init__(self, **kwargs):
        class Config(PrettyKwargs):
            appname = 'Python Application'
            width = 600
            height = 400
        
        conf = Config(**kwargs)
        
        self.app = QApplication()
        self.app.setApplicationName(conf.appname)
        
        self.win = QWidget()
        self.win.setGeometry(0, 0, conf.width, conf.height)
        
        def _center_window(win):
            screen = QApplication.primaryScreen()
            center = QScreen.availableGeometry(screen).center()
            geo = win.frameGeometry()
            geo.moveCenter(center)
            lk.loga(geo, geo.center())
            win.move(geo.topLeft())
        
        _center_window(self.win)
    
    @property
    def root(self):
        return self.win
    
    def start(self):
        self.win.show()
        sys.exit(self.app.exec())


if __name__ == '__main__':
    _app = Application()
    _app.start()
