from PyQt6.QtWidgets import  QWidget, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QDialog, QMessageBox, QApplication
from PyQt6.QtGui import QPixmap 
from PyQt6.QtCore import  QTimer
import sys
a = "1234"
b = "4321"



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Блокировка")
        self.setFixedSize(640, 480)

        self.first_lbl2 = QLabel("Введите цифры:")
        self.first_lineEdit = QLineEdit()
        photo = QLabel()
        pix = QPixmap("PyQt6/new/1234.png")
        photo.setPixmap(pix)
        
        self.layout = QVBoxLayout()
        widget = QWidget()
        
        self.btn = QPushButton("Проверить")
        self.btn.clicked.connect(self.btn_clicked)
        self.layout.addWidget(self.first_lbl2)
        self.layout.addWidget(self.first_lineEdit)
        self.layout.addWidget(photo)
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.layout.addWidget(self.btn)
   
        self.captcha_dialog = CaptchaDialog(parent=self)
        self.captcha_dialog.setModal(True)  

    def btn_clicked(self):
        if self.first_lineEdit.text() == a:
            self.close()
        else:
        
            self.captcha_dialog.start_timer()
                
            if self.captcha_dialog.exec() == QDialog.DialogCode.Accepted:
                QMessageBox.information(self, "Внимание", "Дополнительная блокировка снята")
                
            else:
                QMessageBox.warning(self, "ОШИБКА!!!", "Попробуйте ввести правильно")
                self.login_attempts = 0

                 

class CaptchaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(640, 480)
        self.setWindowTitle("Двойная блокировка")
        self.label = QLabel("Введите цифры:")
        self.textbox = QLineEdit()
        self.button = QPushButton("Проверить")
        self.button.clicked.connect(self.verify_captcha)

        photo2 = QLabel()
        pix2 = QPixmap("PyQt6/new/4321.png")
        photo2.setPixmap(pix2)

        self.timer_label = QLabel("Таймер: 10")
        self.timer_counter = 10
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.button)
        layout.addWidget(photo2)
        self.setLayout(layout)
       

    def verify_captcha(self):
        captcha = self.textbox.text()
        print("Проверка капчи:", captcha)
        
        if captcha.lower() == b:  
            self.accept()
        else:
            self.textbox.setDisabled(True)  
            self.timer_counter = 11
            self.timer.start()
            QMessageBox.critical(self, "ОШИБКА!!!", "Попробуйте ввести правильно")

    def start_timer(self):
        self.timer_counter = 10
        self.timer.start()

    def update_timer(self):
        self.timer_counter -= 1
        self.timer_label.setText(f"Вы заблокированы на: {self.timer_counter}")

        if self.timer_counter == 0 :
            self.timer.stop()
            self.textbox.setDisabled(False)
  