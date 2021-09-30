import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import *
# from __feature__ import snake_case
from lk_logger import lk


def main():
    app = QApplication()
    win = QWidget()
    win.setGeometry(0, 0, 600, 100)
    
    def center(wid):
        screen = QApplication.primaryScreen()
        center = QScreen.availableGeometry(screen).center()
        geo = wid.frameGeometry()
        geo.moveCenter(center)
        lk.loga(geo, geo.center())
        wid.move(geo.topLeft())
    
    center(win)
    
    line_edit = QLineEdit()
    line_edit.setPlaceholderText('Select a markdown file (.md) to convert...')
    
    hbox = QHBoxLayout(win)
    hbox.setAlignment(Qt.AlignTop)
    
    vbox = QVBoxLayout()
    vbox.setAlignment(Qt.AlignTop)
    vbox.addWidget(line_edit)
    hbox.addLayout(vbox)

    vbox1 = QVBoxLayout()
    # vbox1.setAlignment(Qt.AlignTop)
    button = QPushButton('browse')
    dialog = QFileDialog()
    button.clicked.connect(lambda : lk.loga('sdf'))
    vbox1.addWidget(button)
    hbox.addLayout(vbox1)

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
