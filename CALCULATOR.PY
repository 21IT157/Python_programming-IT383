#implementation of Calculator using PyQT
#UI LAYOUT SETUP 
class Calculator(QMainWindow):
   def __init__(self):
       ...
       self.layout.addWidget(self.display, 0, 0, 1, 4)
       for row in range(4):
           for column in range(4):
               self.layout.addWidget(self.buttons[row * 4 + column], row + 1, column)
       self.setLayout(self.layout)
       self.setWindowTitle('Calculator')
#Button Connection
for button in self.buttons.values():
   button.clicked.connect(self.on_button_clicked)
#Button Click(Event) Hnadling 
def on_button_clicked(self, button):
   text = button.text()
   if text == '=':
       expression = self.display.text()
       result = eval(expression)
       self.display.setText(str(result))
   else:
       self.display.setText(self.display.text() + text)

#Application Setup and Execution 
app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
app.exec()

