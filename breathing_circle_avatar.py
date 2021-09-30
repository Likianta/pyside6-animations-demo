import re
import sys

from PySide6.QtCore import *
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import *
from lk_logger import lk
from lk_lambdex import lambdex
from scaffold import Application


class StyleSheetHolder:
    
    def __init__(self, stylesheet: str):
        stylesheet = stylesheet.strip()
        self.stylesheet = re.sub(r'<(\w+) *= *\w+>', r'{\1}', stylesheet)
        self.props = dict(self.parse_stylesheet(stylesheet))
        
    @staticmethod
    def parse_stylesheet(stylesheet):
        for m in re.finditer(r'<(\w+) *= *(\w+)>', stylesheet):
            key, val = m.groups()
            yield key, val
        
    def update(self, **kwargs):
        return self.stylesheet.format(**(self.props | kwargs))
    
    def __str__(self):
        return self.stylesheet.format(**self.props)
        

def main():
    app = Application()
    
    circle = QWidget(app.root)
    styles = StyleSheetHolder('''
        background-color: #ffffff;
        border: <w=1px> solid #000000;
        border-radius: <r=50px>;
    ''')
    lk.loga(styles.stylesheet)
    lk.loga(styles.props)
    circle.setStyleSheet(str(styles))
    circle.setGeometry(10, 20, 100, 100)
    
    anim = QVariantAnimation()
    anim.setStartValue(1)
    anim.setEndValue(4)
    anim.setDuration(400)
    anim.setEasingCurve(QEasingCurve.OutCubic)
    anim.valueChanged.connect(lambdex('val', '''
        # lk.logtx('[D4323]', val)
        circle.setStyleSheet(styles.update(w=val))
    '''))
    
    setattr(circle, 'enterEvent', lambdex(('event',), '''
        lk.loga('the mouse enters circle zone')
        anim.setDirection(QAbstractAnimation.Forward)
        anim.start()
    '''))
    setattr(circle, 'leaveEvent', lambdex(('event',), '''
        lk.loga('the mouse leaves circle zone')
        anim.setDirection(QAbstractAnimation.Backward)
        anim.start()
    '''))
    
    btn_test = QPushButton('Test Anim', app.root)
    btn_test.setGeometry(100, 100, 120, 30)
    # def _start_anim():
    #     lk.loga('start')
    #     anim.start()
    btn_test.clicked.connect(lambdex((), '''
        lk.loga('start')
        anim.start()
    '''))
    
    app.start()


if __name__ == '__main__':
    main()
