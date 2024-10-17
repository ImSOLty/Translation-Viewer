from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMenu
from PyQt5.QtCore import QSize

from table_widget import TableWidget
from vocabulary_window import VocabularyWindow
from error_message import show_error

import os

WINDOW_NAME = "Side-by-Side Translation Viewer"

TRANSLATION = "translation"
ORIGINAL = "original"
VOCABULARY = "vocabulary"

TEMPLATE_ORIGINAL = [
            "#Hello, how are you?",
            "##I hope you're doing well.",
            "Today is a sunny day."
        ]

TEMPLATE_TRANSLATED = [
            "#Hola, ¿cómo estás?",
            "##Espero que estés bien.",
            "Hoy es un día soleado."
        ]

TEMPLATE_VOCABULARY = {"Hola": "Hello"}

SPLIT_SYMBOL = '~'


def parse_content(dictionary: dict[str, str]):
    assert len(dictionary.items()) == 3
    paragraphs_translation = [line.strip() for line in dictionary[TRANSLATION].splitlines() if len(line.strip())]
    paragraphs_original = [line.strip() for line in dictionary[ORIGINAL].splitlines() if len(line.strip())]
    pairs = [line.strip().split(SPLIT_SYMBOL) for line in dictionary[VOCABULARY].splitlines() if len(line.strip())]
    vocabulary_dict = {
        original: translation for original, translation in pairs
    }

    return {
            ORIGINAL: paragraphs_original,
            TRANSLATION: paragraphs_translation,
            VOCABULARY: vocabulary_dict,
    }


class MainWindow(QMainWindow):
    def __init__(self, screen_size: QSize):
        super().__init__()

        self.setWindowTitle(WINDOW_NAME)
        self.setMinimumSize(screen_size.width() // 2, screen_size.height() // 2)
        self._createMenuBar()
        self.central_widget = TableWidget()
        self.vocabulary_window = VocabularyWindow()
        self.setCentralWidget(self.central_widget)
        self.content = {
            ORIGINAL: TEMPLATE_ORIGINAL,
            TRANSLATION: TEMPLATE_TRANSLATED,
            VOCABULARY: TEMPLATE_VOCABULARY,
        }
        self.update_content()

    def _createMenuBar(self):
        menuBar = self.menuBar()

        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)

        action = fileMenu.addAction("Open Folder")
        action.triggered.connect(self.open_folder_action)

        action = fileMenu.addAction("Show vocabulary")
        action.triggered.connect(self.show_hide_vocabulary)

    def open_folder_action(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        content = {}
        needed_files = [TRANSLATION, ORIGINAL, VOCABULARY]
        for key in needed_files:
            target_file = f"_{key}.txt"
            path = os.path.join(folder, target_file)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content[key] = file.read()
            except Exception as e:
                show_error(e)
        if len(content.keys()) < len(needed_files):
            return

        self.content = parse_content(content)
        self.update_content()

    def show_hide_vocabulary(self):
        if self.vocabulary_window.isHidden:
            self.vocabulary_window.show()
        else:
            self.vocabulary_window.close()

    def update_content(self):
        self.central_widget.update_content(self.content[ORIGINAL], self.content[TRANSLATION])
        keys, values = [], []
        for key, value in self.content[VOCABULARY].items():
            keys.append(key)
            values.append(value)
        self.vocabulary_window.central_widget.update_content(keys, values)
