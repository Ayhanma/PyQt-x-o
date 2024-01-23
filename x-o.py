import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,QRadioButton, QMessageBox
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(700, 300, 330, 430)
        self.setWindowTitle('Крестики-нолики')

        self.x = QRadioButton('X', self)
        self.x.setGeometry(100, 20, 40, 40)
        self.o = QRadioButton('O', self)
        self.o.setGeometry(170, 20, 40, 40)
        
        self.button1 = QPushButton('1', self)
        self.button1.setGeometry(50, 80, 70, 70)
        self.button2 = QPushButton('2', self)
        self.button2.setGeometry(130, 80, 70, 70)
        self.button3 = QPushButton('3', self)
        self.button3.setGeometry(210, 80, 70, 70)
        self.button4 = QPushButton('4', self)
        self.button4.setGeometry(50, 160, 70, 70)
        self.button5 = QPushButton('5', self)
        self.button5.setGeometry(130, 160, 70, 70)
        self.button6 = QPushButton('6', self)
        self.button6.setGeometry(210, 160, 70, 70)
        self.button7 = QPushButton('7', self)
        self.button7.setGeometry(50, 240, 70, 70)
        self.button8 = QPushButton('8', self)
        self.button8.setGeometry(130, 240, 70, 70)
        self.button9 = QPushButton('9', self)
        self.button9.setGeometry(210, 240, 70, 70)

        winner = QLabel(self)
        winner.move(100, 330)
        winner.resize(200, 20)
        winner.setText('Победитель: ')

        self.again = QPushButton('Играть заново', self)
        self.again.setGeometry(100, 370, 100, 30)
        
# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        self.side = ['X' , 'O']
        self.a = 0
        self.main = ['X' , 'O']
        
        self.button9.clicked.connect(lambda: self.bp(9))
        self.button8.clicked.connect(lambda: self.bp(8))
        self.button7.clicked.connect(lambda: self.bp(7))
        self.button6.clicked.connect(lambda: self.bp(6))
        self.button5.clicked.connect(lambda: self.bp(5))
        self.button4.clicked.connect(lambda: self.bp(4))
        self.button3.clicked.connect(lambda: self.bp(3))
        self.button2.clicked.connect(lambda: self.bp(2))
        self.button1.clicked.connect(lambda: self.bp(1))
        self.button9.clicked.connect(lambda: self.check())
        self.button8.clicked.connect(lambda: self.check())
        self.button7.clicked.connect(lambda: self.check())
        self.button6.clicked.connect(lambda: self.check())
        self.button5.clicked.connect(lambda: self.check())
        self.button4.clicked.connect(lambda: self.check())
        self.button3.clicked.connect(lambda: self.check())
        self.button2.clicked.connect(lambda: self.check())
        self.button1.clicked.connect(lambda: self.check())

    #Фукнция проверки кто ходит и выполнение хода
    def bp(self, num):
        if  self.a == 0:
            exec(f'self.button{num}.setText("X")')      
            self.a = 1
        else:
            exec(f'self.button{num}.setText("O")')
            self.a = 0
        self.setStyleSheet("QPushButton[text='X'] {color: rgb(255, 0, 0);font-size: 25px;}")
        self.setStyleSheet("QPushButton[text='O'] {color: rgb(0, 0, 255);font-size: 25px;}")

    def check(self):
        if  self.button1.text() == self.button2.text() == self.button3.text() or \
            self.button4.text() == self.button5.text() == self.button6.text() or \
            self.button7.text() == self.button8.text() == self.button9.text() or \
            self.button1.text() == self.button5.text() == self.button9.text() or \
            self.button3.text() == self.button5.text() == self.button9.text() or \
            self.button1.text() == self.button4.text() == self.button7.text() or \
            self.button2.text() == self.button5.text() == self.button8.text() or \
            self.button3.text() == self.button6.text() == self.button9.text():
            
            if self.a == 0:
                self.a = 1
            else:
                self.a = 0

            result = QMessageBox.question(
                None, 
                "Игра завершена", 
                "Победил игрок: {}\n Хотите сыграть еще раз?".format(self.main[self.a]), 
                buttons = QMessageBox.Ok | QMessageBox.No, defaultButton = QMessageBox.Ok)
 
            if result == 1024:
                self.refresh()
                self.restart()
            else:
                self.close()

    def refresh(self):
        self.button1.setText('1')
        self.button2.setText('2')
        self.button3.setText('3')
        self.button4.setText('4')
        self.button5.setText('5')
        self.button6.setText('6')
        self.button7.setText('7')
        self.button8.setText('8')
        self.button9.setText('9')    
        self.setStyleSheet("QPushButton {font-size: 10px;}")

    def restart(self):
        self.side = self.side[::-1]
        self.a = abs(self.a - 1)


qss = '''
QPushButton[text='X'] {
    color: rgb(255, 0, 0);
    font-size: 25px;
}
QPushButton[text='O'] {
    color: rgb(0, 0, 255);
    font-size: 25px;
}
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qss)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())