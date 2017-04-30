# -*- coding: utf-8 -*-
# MLC (Machine Learning Control): A genetic algorithm library to solve chaotic problems
# Copyright (C) 2015-2017, Thomas Duriez (thomas.duriez@gmail.com)
# Copyright (C) 2015, Adrian Durán (adrianmdu@gmail.com)
# Copyright (C) 2015-2017, Ezequiel Torres Feyuk (ezequiel.torresfeyuk@gmail.com)
# Copyright (C) 2016-2017, Marco Germano Zbrun (marco.germano@intraway.com)
# Copyright (C) 2016-2017, Raúl Lopez Skuba (raulopez0@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import os
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from MLC.GUI.Autogenerated.autogenerated import Ui_MLCAboutDialog


class MLCAboutDialog(QDialog):
    MLC_ABOUT = """
    MLC (Machine Learning Control), A genetic algorithm library to solve chaotic problems<br>
    <br>
    Version:%s<br>
    <br>
    Copyright (C) 2015-2017, Thomas Duriez (thomas.duriez@gmail.com)<br>
    Copyright (C) 2015, Adrian Durán (adrianmdu@gmail.com)<br>
    Copyright (C) 2015-2017, Ezequiel Torres Feyuk (ezequiel.torresfeyuk@gmail.com)<br>
    Copyright (C) 2016-2017, Marco Germano Zbrun (marco.germano@intraway.com)<br>
    Copyright (C) 2016-2017, Raúl Lopez Skuba (raulopez0@gmail.com)<br>
    <br>
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    <br>
    <br>
    <div style="text-align: center">
        <a href=\"https://github.com/Ezetowers/MLC\">https://github.com/Ezetowers/MLC</a>
    </div>
    <br>
    <br>
    """ % "3.0"

    def __init__(self, parent=None):
        super(MLCAboutDialog, self).__init__(parent)
        icon_path = os.path.join(*[os.path.dirname(os.path.abspath(__file__)),
                                   "images",
                                   "mlc_icon.png"])

        self.ui = Ui_MLCAboutDialog()
        self.ui.setupUi(self)
        pixmap = QPixmap(icon_path)
        self.ui.mlcimage.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))
        self.ui.labelabout.setText(self.MLC_ABOUT)
