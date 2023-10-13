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
