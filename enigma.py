import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow():
    def setupUi(self, MainWindow):
        '''this function initialize the main ui setup'''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 660)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/b/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 821, 41))
        self.frame.setStyleSheet("background-color: rgb(157, 195, 255);\n" "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(250, -30, 301, 101))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.plaintext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plaintext.setEnabled(True)
        self.plaintext.setGeometry(QtCore.QRect(20, 170, 771, 161))
        self.plaintext.setReadOnly(True)
        self.plaintext.setPlainText("")
        self.plaintext.setObjectName("plaintext")
        self.ciphertext = QtWidgets.QTextBrowser(self.centralwidget)
        self.ciphertext.setGeometry(QtCore.QRect(20, 340, 621, 241))
        self.ciphertext.setObjectName("ciphertext")
        self.filename_file = QtWidgets.QTextEdit(self.centralwidget)
        self.filename_file.setGeometry(QtCore.QRect(20, 100, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.filename_file.setFont(font)
        self.filename_file.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.filename_file.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.filename_file.setObjectName("filename_file")
        self.filename_extension = QtWidgets.QTextEdit(self.centralwidget)
        self.filename_extension.setGeometry(QtCore.QRect(200, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.filename_extension.setFont(font)
        self.filename_extension.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.filename_extension.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.filename_extension.setObjectName("filename_extension")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 110, 49, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.loadfile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.loadfile_btn.setGeometry(QtCore.QRect(330, 100, 81, 31))
        self.loadfile_btn.setObjectName("loadfile_btn")
        self.logtext = QtWidgets.QTextBrowser(self.centralwidget)
        self.logtext.setGeometry(QtCore.QRect(650, 340, 141, 241))
        self.logtext.setStyleSheet(
            "background-color: rgb(33, 33, 33);\n" "color: rgb(221, 221, 221);"
        )
        self.logtext.setObjectName("logtext")
        self.textconvert_btn = QtWidgets.QPushButton(self.centralwidget)
        # self.textconvert_btn.setEnabled(False)
        self.textconvert_btn.setGeometry(QtCore.QRect(650, 80, 141, 51))
        self.textconvert_btn.setObjectName("textconvert_btn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 595, 250, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(True)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(True)
        self.pattern_generator_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pattern_generator_btn.setEnabled(True)
        self.pattern_generator_btn.setGeometry(QtCore.QRect(500, 80, 141, 51))
        self.pattern_generator_btn.setObjectName("pattern_generator_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.loadfile_btn.clicked.connect(self.load_pattern)
        self.textconvert_btn.clicked.connect(self.input_process)
        self.pattern_generator_btn.clicked.connect(self.pattern_generator)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.rotor1 = ""
        self.rotor2 = ""
        self.rotor3 = ""
        self.textconvert_btn.setEnabled(False)
        self.logtext.append("> WAITING FOR SOURCE FILE")

    def load_pattern(self):
        '''this function loads the encoding/decoding pattern from file'''
        import pickle

        try:
            f = open(
                "./%s.%s"
                % (
                    self.filename_file.toPlainText(),
                    self.filename_extension.toPlainText(),
                ),
                "rb",
            )
            self.rotor1, self.rotor2, self.rotor3 = pickle.load(f)
            f.close()
            self.logtext.append("> File Loaded")
            self.logtext.append("> Ready For Convert")
            self.plaintext.setReadOnly(False)
            self.loadfile_btn.setEnabled(False)
            self.filename_file.setEnabled(False)
            self.filename_extension.setEnabled(False)
            self.pattern_generator_btn.setEnabled(False)
            self.textconvert_btn.setEnabled(True)
        except FileNotFoundError:
            self.logtext.append("> ERR: FILE NOT FOUND!")
            self.plaintext.setReadOnly(True)
            self.textconvert_btn.setEnabled(False)

    def input_process(self):
        '''this function converts the plain text to cypher'''
        self.logtext.append("> PROCESSING ...")
        self.textconvert_btn.setEnabled(False)

        global rotor1, rotor2, rotor3
        rotor1, rotor2, rotor3 = self.rotor1, self.rotor2, self.rotor3
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        def reflector(c):
            '''this function reflects one char in alphabet (ex: a -> z)'''
            return alphabet[len(alphabet) - alphabet.find(c) - 1]

        def enigma_one_char(c):
            '''this function does the translate operation for one charachter'''
            return alphabet[
                rotor1.find(
                    alphabet[
                        rotor2.find(
                            alphabet[
                                rotor3.find(
                                    reflector(
                                        rotor3[
                                            alphabet.find(
                                                rotor2[alphabet.find(rotor1[alphabet.find(c)])]
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    ]
                )
            ]

        def rotate_rotors():
            '''this function add one step to rotors for not getting same code for same char(ex: bbbb -> skcl)'''
            global rotor1, rotor2, rotor3
            rotor1 = rotor1[1:] + rotor1[0]
            if state % 26:
                rotor2 = rotor2[1:] + rotor2[0]
            if state % (26 * 26):
                rotor3 = rotor3[1:] + rotor3[0]

        plain = self.plaintext.toPlainText()

        plain = plain.lower()
        cipher = ""
        state = 0

        for char in plain:
            specials = "1234567890!@#$%^&*()_+<>?,.|\\/`~;\"'{}[]:"
            if char == " ":
                cipher += "~"
                continue
            elif char == "~":
                cipher += " "
                continue
            elif char in specials:
                cipher += specials[len(specials) - specials.find(char) - 1]
                continue
            state += 1
            cipher += enigma_one_char(char)
            rotate_rotors()

        self.ciphertext.setPlainText(cipher)
        self.textconvert_btn.setEnabled(True)
        self.logtext.append("> OUTPUT READY")

    def pattern_generator(self):
        '''this function generates new pattern randomly and saves it'''
        self.plaintext.setReadOnly(True)
        self.loadfile_btn.setEnabled(False)
        self.filename_file.setEnabled(False)
        self.filename_extension.setEnabled(False)
        self.pattern_generator_btn.setEnabled(False)
        import random
        import pickle

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        rotor1 = list(alphabet)
        random.shuffle(rotor1)
        rotor1 = "".join(rotor1)

        rotor2 = list(alphabet)
        random.shuffle(rotor2)
        rotor2 = "".join(rotor2)

        rotor3 = list(alphabet)
        random.shuffle(rotor3)
        rotor3 = "".join(rotor3)

        try:
            f = open(
                "./%s.%s"
                % (
                    self.filename_file.toPlainText(),
                    self.filename_extension.toPlainText(),
                ),
                "wb",
            )
            pickle.dump((rotor1, rotor2, rotor3), f)
            f.close()
            self.logtext.append("> NEW PATTERN GENERATED")

            self.filename_file.setEnabled(True)
            self.filename_extension.setEnabled(True)
            self.loadfile_btn.setEnabled(True)
            self.pattern_generator_btn.setEnabled(True)
        except:
            self.logtext.append("> ERR: CAN NOT GENERATE!")

    def retranslateUi(self, MainWindow):
        '''this function is for ui texts'''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text Decoder/Encoder"))
        self.label.setText(_translate("MainWindow", "Text Encoder/Decoder"))
        self.plaintext.setPlaceholderText(_translate("MainWindow", "Plain Text"))
        self.ciphertext.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.ciphertext.setPlaceholderText(_translate("MainWindow", "Cipher"))
        self.filename_file.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Roboto'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">pattern_name</p></body></html>',
            )
        )
        self.filename_extension.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Roboto'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">enigma</p></body></html>',
            )
        )
        self.label_2.setText(_translate("MainWindow", "."))
        self.label_3.setText(_translate("MainWindow", "File Name:"))
        self.loadfile_btn.setText(_translate("MainWindow", "LOAD"))
        self.logtext.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.logtext.setPlaceholderText(_translate("MainWindow", "Log:"))
        self.textconvert_btn.setText(_translate("MainWindow", "CONVERT"))
        self.label_4.setText(_translate("MainWindow", "By: ALIREZASH2004 (github)"))
        self.pattern_generator_btn.setText(_translate("MainWindow", "GENERATE PATTERN"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
