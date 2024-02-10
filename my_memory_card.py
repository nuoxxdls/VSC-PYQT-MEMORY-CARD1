#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton,QPushButton,QLabel,QButtonGroup)
from random import shuffle

class Question():
    def __init__(self, question, right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3



questions_list=[]
questions_list.append(Question('Сколько будет 2+2?','4','5','40','-4'))
questions_list.append(Question('Какте цвета на флаге Казахстана?','Синий и желтый','Красный и фиолетовый','Желтый','Синий'))
questions_list.append(Question('Сколько пальцев есть у человека?','20','5','10','16'))

app= QApplication([])

btn_OK=QPushButton('Ответить')
vaprosik=QLabel('Какой страны не существует?')

RadioGroupBox = QGroupBox('Варианты ответов')

var1=QRadioButton("Казахстан")
var2=QRadioButton("Австралия")
var3=QRadioButton("Азия")
var4=QRadioButton("Япония")

RadioGroup = QButtonGroup()
RadioGroup.addButton(var1)
RadioGroup.addButton(var2)
RadioGroup.addButton(var3)
RadioGroup.addButton(var4)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Был ли твой ответ правильным?')
lb_Correct = QLabel('Ответ тут!                 \/')
layout_res = QVBoxLayout()
layvar1=QHBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)
AnsGroupBox.setLayout(layout_res)

layvar2=QVBoxLayout()
layvar3=QVBoxLayout()

layvar2.addWidget(var1)
layvar2.addWidget(var2)
layvar3.addWidget(var3)
layvar3.addWidget(var4)

layvar1.addLayout(layvar2)
layvar1.addLayout(layvar3)

RadioGroupBox.setLayout(layvar1)

layline3 = QHBoxLayout()
layline2 = QHBoxLayout()
layline1 = QHBoxLayout()

layline1.addWidget(vaprosik)
layline2.addWidget(RadioGroupBox)
layline2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layline1.addWidget(vaprosik)
layline2.addWidget(RadioGroupBox)

layline3.addStretch(1)
layline3.addWidget(btn_OK, stretch=2)
layline3.addStretch(1)

layout_card=QVBoxLayout()

layout_card.addLayout(layline1, stretch=2)
layout_card.addLayout(layline2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layline3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    var1.setChecked(False)
    var2.setChecked(False)
    var3.setChecked(False)
    var4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [var1,var2,var3,var4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    vaprosik.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res) 
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked():
            show_correct('Неверно!')

def next_question():
    window.cur_question - window.cur_question + 1
    if window.cur_question >= len(questions_list):
        windonw.cur_question = 0
    q =questions_list[window.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()



btn_OK.clicked.connect(click_OK)
window=QWidget()
window.setWindowTitle("Memory Card")
window.cur_question = -1
next_question()
window.resize(400,300)
window.setLayout(layout_card)
window.show()
app.exec()
