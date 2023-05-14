import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, QApplication, QWidget, QLabel, QRadioButton, QPushButton


class FirstWidget(QWidget):
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
        self.label = QWidget('First Widget', self)
    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Тест ...")

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
        self.check_button.setText('...')
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

class SecondWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QWidget.QLabel('Second Widget', self)
        

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QWidget.QStackedWidget(self)
        self.first_widget = FirstWidget()
        self.second_widget = SecondWidget()

        self.stacked_widget.addWidget(self.first_widget)
        self.stacked_widget.addWidget(self.second_widget)

        self.button1 = QWidget.QPushButton('Go to Second Widget', self)
        self.button2 = QWidget.QPushButton('Go to First Widget', self)

        v_box = QWidget.QVBoxLayout()
        v_box.addWidget(self.stacked_widget)
        v_box.addWidget(self.button1)
        v_box.addWidget(self.button2)

        self.setLayout(v_box)

        self.button1.clicked.connect(self.go_to_second_widget)
        self.button2.clicked.connect(self.go_to_first_widget)

    def go_to_second_widget(self):
        self.stacked_widget.setCurrentIndex(1)

    def go_to_first_widget(self):
        self.stacked_widget.setCurrentIndex(0)


app = QApplication(sys.argv)
main_window = FirstWidget()
main_window.show()
sys.exit(app.exec_())

