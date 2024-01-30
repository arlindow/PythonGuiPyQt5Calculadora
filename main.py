import PyQt5
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QGridLayout




class Calculadora(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculadora')
        self.setGeometry(100, 100, 300, 400)

        self.init_ui()

    def init_ui(self):
        # Widget de exibição
        self.display = QLineEdit(self)
        self.display.setFixedHeight(40)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.display)

        # Botões
        buttons = [
            '7', '8', '9', '/',''
            '4', '5', '6', '*',''
            '1', '2', '3', '-',''
            '0', '.', '=', '+', 'C'
        ]

        grid_layout = QGridLayout()

        # Mapeamento dos botões para suas posições no layout
        button_positions = [
            (0, 0, 1, 1), (0, 1, 1, 1), (0, 2, 1, 1), (0, 3, 1, 1),
            (1, 0, 1, 1), (1, 1, 1, 1), (1, 2, 1, 1), (1, 3, 1, 1),
            (2, 0, 1, 1), (2, 1, 1, 1), (2, 2, 1, 1), (2, 3, 1, 1),
            (3, 0, 1, 1), (3, 1, 1, 1), (3, 2, 1, 1), (3, 3, 1, 1),
            (4, 0, 1, 2)  # Botão "C" ocupa 2 colunas
        ]

        for button_text, (row, col, rowspan, colspan) in zip(buttons, button_positions):
            button = QPushButton(button_text, self)
            button.clicked.connect(self.button_click)
            grid_layout.addWidget(button, row, col, rowspan, colspan)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def button_click(self):
        button = self.sender()
        current_text = self.display.text()
        button_text = button.text()

        if button_text == '=':
            try:
                result = str(eval(current_text))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Erro')
        elif button_text == 'C':
            self.display.clear()
        else:
            new_text = current_text + button_text
            self.display.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    sys.exit(app.exec_())
    


