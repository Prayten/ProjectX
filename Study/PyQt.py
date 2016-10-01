import sys
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox, QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a QWidget')

        btn = QPushButton('Click me', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip('This is a PushButton')
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.resize(500,500)
        self.setWindowTitle('Application')
        self.setWindowIcon(QIcon('icon.png'))
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    #w = QWidget()
    #print(w.setWindowIcon(QIcon='icon.png'))
    # w = QWidget()
    # w.resize(250,150)
    # w.move(300,300)
    # w.setWindowTitle('Simple')
    # w.show()

    sys.exit(app.exec_())