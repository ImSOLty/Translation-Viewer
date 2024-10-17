from PyQt5.QtWidgets import QMainWindow

from table_widget import TableWidget

WINDOW_NAME = "Vocabulary"


class VocabularyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(WINDOW_NAME)
        self.setMinimumSize(600, 800)
        self.central_widget = TableWidget()
        self.setCentralWidget(self.central_widget)
