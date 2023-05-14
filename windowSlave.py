from PyQt6.QtWidgets import QLabel, QPushButton, QWidget, QWidget, QLabel, QRadioButton, QPushButton

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        self.question_label = QLabel(self)
        self.answer1_radio = QRadioButton(self)
        self.answer2_radio = QRadioButton(self)
        self.answer3_radio = QRadioButton(self)
        self.check_button = QPushButton(self)
        self.check_button2 = QPushButton(self)
        self.check_button3 = QPushButton(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Тест ")

        self.question_label.setGeometry(50, 50, 500, 100)
        self.question_label.setText('Вопрос 1: ...')
        self.question_label.setWordWrap(True)

        self.answer1_radio.setGeometry(100, 150, 400, 30)
        self.answer1_radio.setText('...')
        self.answer1_radio.setChecked(False)

        self.answer2_radio.setGeometry(100, 200, 400, 30)
        self.answer2_radio.setText('...')
        self.answer2_radio.setChecked(False)

        self.answer3_radio.setGeometry(100, 250, 400, 30)
        self.answer3_radio.setText('...')
        self.answer3_radio.setChecked(False)

        self.check_button.setGeometry(200, 350, 200, 30)
        self.check_button.setText('Проверить')
        self.check_button2.setGeometry(0, 350, 250, 30)
        self.check_button2.setText('Назад')
        self.check_button3.setGeometry(400, 350, 250, 30)
        self.check_button3.setText('Далее')
        self.check_button.clicked.connect(self.checkAnswer)
        
    def checkAnswer(self):
        if self.answer2_radio.isChecked():
            self.question_label.setText('Ответ верный!')
        else:
            self.question_label.setText('Ответ неверный!')



