# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 20:26:27 2016

@author: Rainer Jacob

General setup class
"""
try:
    from PyQt4 import QtGui
    from PyQt4 import uic
except ImportError:
    from PyQt5 import QtWidgets as QtGui
    from PyQt5 import uic


class GeneralSetup(QtGui.QDialog):
    """Class that provides the General setup dialog and its functionality"""

    def __init__(self, path_forms):
        """Constructor.

        Args:
        -----
        path_forms: str
            String containing the path to the ui-files defining the look of the
            window.
        """
        super(GeneralSetup, self).__init__()
        uic.loadUi(path_forms.joinpath("generalsetup.ui"), self)
        self.simulationFreeTextEdit.setText("Use Mesh Names = Logical True")
        self.acceptButton.clicked.connect(self.applyChanges)

    def applyChanges(self):
        """Apply button hit"""
        # Hide window, but keep contents in memory
        self.hide()
