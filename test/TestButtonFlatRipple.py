#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年10月2日
@author: Irony."[讽刺]
@site: alyl.vip, orzorz.vip, irony.coding.me , irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: test.TestButtonFlatRipple
@description: 
'''

import os
import sys

sys.path.insert(0, os.path.dirname(os.getcwd()))
print(sys.path)
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QScrollArea

from QMaterial.Utils import Colors
from QMaterial.Widget.Button import RippleFlatButton
from random import randrange


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QGridLayout(self)
        colors = Colors.alls()
        for row, key in enumerate(colors):
            layout.addWidget(RippleFlatButton(key, self), row, 0, 1, 1)
            for column, value in enumerate(colors.get(key)):
                b = RippleFlatButton(value._name, self)
                b.backgroundColor = value
                b.setEnabled(randrange(0, 2))
                if not b.isEnabled():
                    b.fontColorDisable = value
                layout.addWidget(b, row, column + 1, 1, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("RippleFlatButton")
    app.setApplicationName("RippleFlatButton")
    window = QScrollArea()
    window.setWidgetResizable(True)
    window.setWidget(Window())
    window.show()
    sys.exit(app.exec_())
