from PyQt5.QtWidgets import QErrorMessage


def show_error(parent, s: str):
    error_dialog = QErrorMessage(parent)
    error_dialog.showMessage(f"Oopsy daisy!\n{s}")
