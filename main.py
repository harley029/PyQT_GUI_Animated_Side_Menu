# import os
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import *
from Custom_Widgets.Widgets import *

from src.ui_interface import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        loadJsonStyle(self, self.ui)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
