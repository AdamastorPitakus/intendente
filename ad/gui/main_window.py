
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from Ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conecta os sinais aos slots
        self.actionAbrir.triggered.connect(self.abrir_arquivo)
        self.actionSalvar.triggered.connect(self.salvar_arquivo)
        self.actionSair.triggered.connect(self.close)

        #configurações basicas de janela
        self.setWindowTitle("Gerenciador de Estoque")
        self.setGeometry(100, 100, 800, 600)
        self.show()

        # adiciona um widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # cria um layout vertical
        self.vertical_layout = QVBoxLayout()
        self.central_widget.setLayout(self.vertical_layout)

        #qdiciona um rótulo como exemplo ao layout
        self.label = QLabel("Olá, mundo!")
        self.vertical_layout.addWidget(self.label)

        #define o layout como o layout central
        self.central_widget.setLayout(self.vertical_layout)

        #adiciona um botão ao layout
        self.button = QPushButton("Clique aqui!")
        self.vertical_layout.addWidget(self.button)

    # Define o slot para o sinal triggered do menu Abrir
    def abrir_arquivo(self):
        # Abre uma caixa de diálogo para selecionar um arquivo
        filename, _ = QFileDialog.getOpenFileName(
            self, "Abrir arquivo", "", "Arquivos de texto (*.txt)"
        )

        # Verifica se o usuário selecionou um arquivo
        if filename:
            # Abre o arquivo no modo leitura
            with open(filename, "r") as f:
                # Lê o conteúdo do arquivo
                data = f.read()

                # Exibe o conteúdo do arquivo na caixa de texto
                self.textEdit.setText(data)

    # Define o slot para o sinal triggered do menu Salvar
    def salvar_arquivo(self):
        # Abre uma caixa de diálogo para selecionar um arquivo
        filename, _ = QFileDialog.getSaveFileName(
            self, "Salvar arquivo", "", "Arquivos de texto (*.txt)"
        )

        # Verifica se o usuário selecionou um arquivo
        if filename:
            # Abre o arquivo no modo escrita
            with open(filename, "w") as f:
                # Escreve o conteúdo da caixa de texto no arquivo
                f.write(self.textEdit.toPlainText())

                # Exibe uma mensagem de sucesso
                QMessageBox.information(self, "Sucesso", "Arquivo salvo com sucesso!")

    # Define o slot para o sinal triggered do menu Sair
    def close(self):
        # Fecha a janela
        self.close()

        # Define o slot para o sinal clicked do botão
    def on_button_clicked(self):
        # Altera o texto do rótulo
        self.label.setText("Você clicou no botão!")

        # Exibe uma mensagem de sucesso
        QMessageBox.information(self, "Sucesso", "Você clicou no botão!")

        # Define o slot para o sinal textChanged da caixa de texto
    def on_text_changed(self):
        # Altera o texto do rótulo
        self.label.setText(self.textEdit.toPlainText())

        # Exibe uma mensagem de sucesso
        QMessageBox.information(self, "Sucesso", "Você alterou o texto!")


