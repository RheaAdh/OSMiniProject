import GUI.app as app

from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt

# IMPORTING THE PROCESS SCHEDULING ALGORITHMS
import fcfs
import roundrobin
import sjf


class appwindow(QMainWindow, app.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fcfstable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.sjftable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.rrtable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.calculatebutton.clicked.connect(self.calculate)

        self.numfield.setTextMargins(5, 0, 0, 0)
        self.burstfield.setTextMargins(5, 0, 0, 0)

    def calculate(self):
        bursttimetext = self.burstfield.text()
        bursttime = [int(burst.strip()) for burst in bursttimetext.split(',')]
        numprocess = len(bursttime)
        processes = [num for num in range(1, numprocess + 1)]

        self.fcfsOutput = fcfs.findAverageTime(
            processes, numprocess, bursttime)
        # print("!!!!!!!!!!!!FCSFS OUTPUT!!!!!!!!!!!!")
        # print(self.fcfsOutput)

        self.roundrobinOutput = roundrobin.findAverageTime(
            processes, numprocess, bursttime, 2)
        # print("!!!!!!!!!!!!RR OUTPUT!!!!!!!!!!!!")
        # print(self.roundrobinOutput)

        self.sjfOutput = sjf.findAverageTime(sorted(bursttime), bursttime)
        # print("!!!!!!!!!!!!SJF OUTPUT!!!!!!!!!!!!")
        # print(self.sjfOutput)

        self.createtable()

    def createtable(self):
        count = 0
        self.fcfstable.setRowCount(len(self.fcfsOutput))
        for item in self.fcfsOutput:
            self.fcfstable.setItem(count, 0, QTableWidgetItem(item['process']))
            self.fcfstable.setItem(
                count, 1, QTableWidgetItem(item['burstTime']))
            self.fcfstable.setItem(
                count, 2, QTableWidgetItem(item['waitingTime']))
            self.fcfstable.setItem(
                count, 3, QTableWidgetItem(item['turnAroundTime']))
            count = count + 1

        count = 0
        self.rrtable.setRowCount(len(self.roundrobinOutput))
        for item in self.roundrobinOutput:
            self.rrtable.setItem(count, 0, QTableWidgetItem(item['process']))
            self.rrtable.setItem(count, 1, QTableWidgetItem(item['burstTime']))
            self.rrtable.setItem(
                count, 2, QTableWidgetItem(item['waitingTime']))
            self.rrtable.setItem(
                count, 3, QTableWidgetItem(item['turnAroundTime']))
            count = count + 1

        count = 0
        self.sjftable.setRowCount(len(self.sjfOutput))
        for item in self.sjfOutput:
            self.sjftable.setItem(count, 0, QTableWidgetItem(item['process']))
            self.sjftable.setItem(count, 1, QTableWidgetItem(item['burstTime']))
            self.sjftable.setItem(
                count, 2, QTableWidgetItem(item['waitingTime']))
            self.sjftable.setItem(
                count, 3, QTableWidgetItem(item['turnAroundTime']))
            count = count + 1

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
QApplication.setHighDpiScaleFactorRoundingPolicy(
    Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

app = QApplication([])

mainwindow = appwindow()
mainwindow.show()

app.exec_()
