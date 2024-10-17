from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout


ROW_HTML_CONTENT = """<tr>
    <td style='padding: 2px; border: 1px solid #e6e6e6; border-collapse: collapse; font-size: 16px'>{original}</td>
    <td style='padding: 2px; border: 1px solid #e6e6e6; border-collapse: collapse; font-size: 16px'>{translated}</td>
</tr>
"""
TABLE_HTML = """<table width="100%" style="border: 1px solid #e6e6e6; border-collapse: collapse;">{content}</table>"""


class TableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.text_edit = QTextEdit(self)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        self.setLayout(layout)

        self.original_paragraphs = []
        self.translated_paragraphs = []
        self.update_table()

    def update_table(self):
        html_content = ''
        for original, translated in zip(self.original_paragraphs, self.translated_paragraphs):
            outer_tag = '<p>{text}</p>'
            if original[0] == '#':
                prev_len = len(original)

                original = original.lstrip('#').strip()
                translated = translated.lstrip('#').strip()

                heading_count = prev_len - len(original)
                outer_tag = f'<h{heading_count}>' + '{text}' + f'</h{heading_count}>'

            html_content += ROW_HTML_CONTENT.format(original=outer_tag.format(text=original),
                                                    translated=outer_tag.format(text=translated))
        self.text_edit.setHtml(TABLE_HTML.format(content=html_content))

    def update_content(self, original, translated):
        self.original_paragraphs = original
        self.translated_paragraphs = translated
        self.update_table()
