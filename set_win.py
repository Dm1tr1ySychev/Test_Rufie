from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QPushButton,QLabel, QListWidget, QLineEdit)

from instruct import *
from fin_win import *

class Experiment():
    def __init__(self, age, res1, res2, res3):
        self.age = age
        self.res1 = res1
        self.res2 = res2
        self.res3 = res3

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_apper()
        self.initUI()
        self.connects()
        self.show()
    def set_apper(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.text_name = QLabel(txt_name)
        self.age = QLabel(txt_age)
        self.test1 = QLabel(txt_test1)
        self.test2 = QLabel(txt_test2)
        self.test3 = QLabel(txt_test3)
        self.timer = QLabel(txt_timer)

        self.butt_next = QPushButton(txt_sendresults, self)
        self.butt_test1 = QPushButton(txt_starttest1, self)
        self.butt_test2 = QPushButton(txt_starttest2, self)
        self.butt_test3 = QPushButton(txt_starttest3, self)

        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        self.l_line = QVBoxLayout() 
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        self.l_line.addWidget(self.text_name, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.test1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.butt_test1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment= Qt.AlignLeft)

        self.l_line.addWidget(self.test2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.butt_test2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.test3, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.butt_test3, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment= Qt.AlignLeft)

        self.l_line.addWidget(self.butt_next, alignment= Qt.AlignCenter)
        self.r_line.addWidget(self.timer, alignment= Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        self.setLayout(self.h_line)
    def next_click(self):
        self.exp = Experiment(int(self.line_age.text()), self.line_test1.text(), self.line_test2.text(), self.line_test3.text())
        self.finv = FinalWin(self.exp)
        self.hide()
        #print('почему ты не работаешь...')
    def timer_test(self):
        global time
        time = QTime(0, 0, 16)
        self.reverse_time = QTimer()
        self.reverse_time.timeout.connect(self.eventTest1)
        self.reverse_time.start(1000)
    def eventTest1(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString("hh:mm:ss"))
        self.timer.setFont(QFont("Times", 36, QFont.Bold))
        self.timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.reverse_time.stop()
    def timer_sits(self):
        global time
        time = QTime(0, 0, 31)
        self.reverse_time = QTimer()
        self.reverse_time.timeout.connect(self.eventTest2)
        self.reverse_time.start(1500)
    def eventTest2(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString("hh:mm:ss")[6:8])
        self.timer.setFont(QFont("Times", 36, QFont.Bold))
        self.timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.reverse_time.stop()
    def timer_final(self):
        global time
        time = QTime(0, 1, 1)
        self.reverse_time = QTimer()
        self.reverse_time.timeout.connect(self.eventTest3)
        self.reverse_time.start(1000)
    def eventTest3(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString("hh:mm:ss"))
        if int((time.toString("hh:mm:ss")[6:8])) >= 45:
            self.timer.setStyleSheet("color: rgb(0,255,0)")
        elif int((time.toString("hh:mm:ss")[6:8])) <= 15:
            self.timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.timer.setStyleSheet("color: rgb(0,0,0)")
        self.timer.setFont(QFont("Times", 36, QFont.Bold))   
        if time.toString("hh:mm:ss") == "00:00:00":
            self.reverse_time.stop()
    def connects(self):
        self.butt_next.clicked.connect(self.next_click)
        self.butt_test1.clicked.connect(self.timer_test)
        self.butt_test2.clicked.connect(self.timer_sits)
        self.butt_test3.clicked.connect(self.timer_final)












        