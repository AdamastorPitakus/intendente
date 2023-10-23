# O ponto de entrada principal para o aplicativo de gerenciamento de estoques.
# Este arquivo contém o código para criar o aplicativo e executá-lo.

# Importações
import sys # Importa o módulo sys
from PyQt5.QtWidgets import QApplication # Importa a classe QApplication do módulo PyQt5.QtWidgets

from gui.main_window import MainWindow # Importa a classe MainWindow do arquivo main_window.py

# Função principal

def main():
    # Cria uma instância da classe QApplication
    app = QApplication(sys.argv)

    # Cria uma instância da classe MainWindow
    main_window = MainWindow()

    # Exibe a janela principal
    main_window.show()

    # Executa o aplicativo
    sys.exit(app.exec_())

# Executa a função main
if __name__ == "__main__":
    main()

# Fim do arquivo main.py



