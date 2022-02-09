import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QLineEdit, QSizePolicy



class Calculadora(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw )

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5) #primeira linha, primeira coluna - vai ocupar uma linha e cinco colunas 
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '*{background: #B5B5B5; color: #061107; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.adc_botao(QPushButton('AC'), 1, 0, 1, 1, lambda: self.display.setText(''), 
        'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton('+/-'), 1, 1, 1, 1, None, 'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton('%'), 1, 2, 1, 1, None, 'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton('/'), 1, 3, 1, 2, None, 'background: #B5B5B5; font-weight: bold;')

        self.adc_botao(QPushButton('7'), 2, 0, 1, 1, None, 'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton('8'), 2, 1, 1, 1, None, 'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton('9'), 2, 2, 1, 1, None, 'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton('*'), 2, 3, 1, 2, None, 'background: #B5B5B5; font-weight: bold;')
        
        self.adc_botao(QPushButton('4'), 3, 0, 1, 1, None, 'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton('5'), 3, 1, 1, 1, None, 'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton('6'), 3, 2, 1, 1, None, 'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton('-'), 3, 3, 1, 2, None, 'background: #B5B5B5; font-weight: bold;')
        
        self.adc_botao(QPushButton('1'), 4, 0, 1, 1, None, 'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton('2'), 4, 1, 1, 1, None, 'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton('3'), 4, 2, 1, 1, None, 'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton('+'), 4, 3, 1, 2, None, 'background: #B5B5B5; font-weight: bold;')
        
        self.adc_botao(QPushButton('0'), 5, 0, 1, 2, None, 'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton(','), 5, 2, 1, 1, None, 'background: #B5B5B5; font-weight: bold;')
        self.adc_botao(QPushButton('='), 5, 3, 1, 2, self.eval_igual, 'background: #B5B5B5; font-weight: bold;')
        
        self.setCentralWidget(self.cw)

    def adc_botao(self, btn, row, col, rowspan, colspan, funcao = None, style = None  ): #rowspan = linhas ocupadas, colspan = colunas ocupadas
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                    lambda: self.display.setText( #seta o texto que for iserido no display
                        self.display.text() + btn.text()
                    )
                )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText('Conta inválida')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()