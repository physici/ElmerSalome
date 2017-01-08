# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 19:51:49 2016

@author: Rainer Jacob

Solver paramter editor class
"""

from PyQt4 import QtGui
from PyQt4 import uic


class SolverParameterEditor(QtGui.QDialog):
    """Class that provides the Solver paramter editor and its functionality"""

    def __init__(self, path_forms):
        """Constructor"""
        super(SolverParameterEditor, self).__init__()
        uic.loadUi(path_forms + "solverparameters.ui", self)

        self.applyButton.clicked.connect(self.close)

        self.useHypre.stateChanged.connect(self._hypreStateChanged)
        self.useParasails.stateChanged.connect(self._parasailsStateChanged)
        self.useBoomerAMG.stateChanged.connect(self._boomerAMGStateChanged)

        self.solverName = ""
        self.generalOptions = None
        self._projectIO = None

        self._hypreStateChanged(0)

    def appendToProject(self):
        """ToDo"""
        return

    def readFromProject(self):
        """ToDo"""
        return

    def _hypreStateChanged(self, integer):
        if(self.useHypre.isChecked()):
            self.parasailsGroup.setEnabled(True)
            self.boomerAMGGroup.setEnabled(True)
        else:
            self.parasailsGroup.setEnabled(False)
            self.boomerAMGGroup.setEnabled(False)

    def _parasailsStateChanged(self):
        if(self.useParasails.isChecked()):
            self.boomerAMGGroup.setEnabled(True)
        else:
            self.boomerAMGGroup.setEnabled(True)

    def _boomerAMGStateChanged(self):
        if(self.useBoomerAMG.isChecked()):
            self.parasailsGroup.setEnabled(True)
        else:
            self.parasailsGroup.setEnabled(True)
