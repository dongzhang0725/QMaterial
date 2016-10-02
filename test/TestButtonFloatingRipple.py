#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年10月2日
@author: Irony."[讽刺]
@site: alyl.vip, orzorz.vip, irony.coding.me , irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: test.TestButtonFloatingRipple
@description: 
'''

import os
import sys

sys.path.insert(0, os.path.dirname(os.getcwd()))
print(sys.path)
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QScrollArea

from QMaterial.Utils import Colors
from QMaterial.Widget.Button import RippleFloatingButton, RippleFloatingButtonBig
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
            which = randrange(0, 2)
            layout.addWidget(RippleFloatingButtonBig(
                key, self) if which else RippleFloatingButton(key, self), row, 0, 1, 1)
            for column, value in enumerate(colors.get(key)):
                b = RippleFloatingButtonBig(
                    value._name, self) if which else RippleFloatingButton(value._name, self)
                b.backgroundColor = value
                b.setEnabled(which)
                layout.addWidget(b, row, column + 1, 1, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("RippleFloatingButton")
    app.setApplicationName("RippleFloatingButton")
    window = QScrollArea()
    window.setWidgetResizable(True)
    window.setWidget(Window())
    window.show()
    sys.exit(app.exec_())
