import sys
from PyQt6.QtWidgets import QApplication,QWidget, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout 
from windowSlave import SecondWindow
from kapcha import Window 

#окно авторизации
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(320, 200)
        self.setWindowTitle("Войти")

        self.first_lbl = QLabel("Логин")
        self.first_lineEdit = QLineEdit()
        self.first_lb2 = QLabel("Пароль")
        self.first_lineEdit2 = QLineEdit()

        self.btn = QPushButton("Вход")
        self.btn2 = QPushButton("Выход")
        self.btn2.clicked.connect(self.exit)
        self.btn.clicked.connect(self.btn_clicked)
        self.layout = QVBoxLayout()
        widget = QWidget()

        self.layout.addWidget(self.first_lbl)
        self.layout.addWidget(self.first_lineEdit)
        self.layout.addWidget(self.first_lb2)
        self.layout.addWidget(self.first_lineEdit2)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn2)
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn2)

    def btn_clicked(self):
        self.window2 = SecondWindow()
        if self.first_lineEdit.text() == "1" and self.first_lineEdit2.text() == "1":
            self.window2.show()

        else:
            self.kapcha = Window()
            self.kapcha.show()
            
    def exit(self):
        self.close()

#Стили
style = (
    """
    *{
        background-color: lightblue;
    }
    QPushButton{
        background-color: indigo;
    }
    """
)

app = QApplication(sys.argv)
window = MainWindow()
window.setStyleSheet(style)
window.show()
app.exec()