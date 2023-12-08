import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, \
    QColorDialog, QFontDialog, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class TextEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Текстовый редактор")

        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        rightLayout = QVBoxLayout()
        buttonLayout = QVBoxLayout()

        self.textEdit = QTextEdit()
        self.textEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        topLayout.addWidget(self.textEdit, 2)

        buttonFont = QFont()
        buttonFont.setPointSize(18)

        def createButton(text, handler):
            def wrapper():
                handler()
                self.textEdit.setFocus()
            button = QPushButton(text)
            button.setFont(buttonFont)
            button.clicked.connect(wrapper)
            buttonLayout.addWidget(button)
            return button

        createButton("Шрифт", self.changeFont)
        createButton("Цвет текста", self.changeColor)
        createButton("Левое выравнивание (CTRL + G)", lambda: self.textEdit.setAlignment(Qt.AlignLeft))
        createButton("Центральное выравнивание (CTRL + H)", lambda: self.textEdit.setAlignment(Qt.AlignCenter))
        createButton("Правое выравнивание (CTRL + J)", lambda: self.textEdit.setAlignment(Qt.AlignRight))
        createButton("Сохранить файл (CTRL + E)", self.saveText)
        createButton("Открыть файл (CTRL + Q)", self.openText)

        rightLayout.addLayout(buttonLayout)
        topLayout.addLayout(rightLayout, 1)
        mainLayout.addLayout(topLayout)

        exitButton = createButton("Выход (Esc)", self.close)
        mainLayout.addWidget(exitButton)

        self.setLayout(mainLayout)

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def changeColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.textEdit.setTextColor(color)

    def saveText(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.textEdit.toPlainText())
        self.textEdit.clear()

    def openText(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.textEdit.setText(file.read())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_E and event.modifiers() == Qt.ControlModifier:
            self.saveText()
        if event.key() == Qt.Key_Q and event.modifiers() == Qt.ControlModifier:
            self.openText()
        if event.key() == Qt.Key_G and event.modifiers() == Qt.ControlModifier:
            self.textEdit.setAlignment(Qt.AlignLeft)
        if event.key() == Qt.Key_H and event.modifiers() == Qt.ControlModifier:
            self.textEdit.setAlignment(Qt.AlignCenter)
        if event.key() == Qt.Key_J and event.modifiers() == Qt.ControlModifier:
            self.textEdit.setAlignment(Qt.AlignRight)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextEditor()
    ex.show()
    sys.exit(app.exec_())
