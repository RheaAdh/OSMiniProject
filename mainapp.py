import GUI.app as app

from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView
from PyQt5.QtCore import Qt

import fcfs
import roundrobin

class appwindow(QMainWindow, app.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fcfstable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.sjftable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.rrtable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.calculatebutton.clicked.connect(self.calculate)

    def calculate(self):
        bursttimetext = self.burstfield.text()
        bursttime = [int(burst.strip()) for burst in bursttimetext.split(',')]
        numprocess = len(bursttime)
        processes = [num for num in range(1, numprocess + 1)]
        
        fcfs.findAverageTime(processes, numprocess, bursttime)
        roundrobin.findavgTime(processes, numprocess, bursttime, 2)


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

app = QApplication([])

mainwindow = appwindow()
mainwindow.show()

app.exec_()