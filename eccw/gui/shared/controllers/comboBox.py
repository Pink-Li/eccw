#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from eccw.gui.shared.viewers.comboBox_line import Ui_Form as UiLine
from eccw.gui.shared.viewers.comboBox_point import Ui_Form as UiPoint
from eccw.gui.shared.viewers.comboBox_colorMap import Ui_Form as UiCmap
from eccw.gui.shared.viewers.comboBox_context import Ui_Form as UiContext


class ComboBox(object):
    """Abstract class."""
    def get_params(self):
        return self.comboBox.currentText()

    def set_params(self, value):
        i = self.comboBox.findText(str(value))
        if i >= 0:
            self.comboBox.setCurrentIndex(i)
        else:
            raise TypeError(self.__class__.__name__
                            + "() gets unknown style argument '"
                            + str(value)+"'.")

    def get_select(self):
        return self.get_params()


class ComboBoxLine(QtGui.QWidget, UiLine, ComboBox):
    """Combo box widget for line style settings.

    Arguments:
    Awaits a single string value among the following list:
    * continous
    * dotted
    * dashed
    * dash dotted

    This is a Qt derived object.
    """
    def __init__(self, *args):
        super(ComboBoxLine, self).__init__()
        self.setupUi(self)
        # Fill values with args
        if args:
            self.set_params(*args)
        self.show()


class ComboBoxPoint(QtGui.QWidget, UiPoint, ComboBox):
    """Combo box widget for point style settings.

    Arguments:
    Awaits a single string value among the following list:
    * circle   or c
    * square   or s
    * diamond  or d
    * triangle or t
    * star     or *
    * cross    or +
    * pentagon or p

    This is a Qt derived object.
    """
    def __init__(self, *args):
        super(ComboBoxPoint, self).__init__()
        self.setupUi(self)
        # Fill values with args
        self.shortcuts_parser = {'c': 'circle', 's': 'square', 'd': 'triangle',
                                 't': 'triangle', '*': 'star', '+': 'cross',
                                 'p': 'pentagon'}
        if args:
            self.set_params(*args)
        self.show()

    def set_params(self, value):
        value = self.shortcuts_parser.get(value, value)
        ComboBoxLine.set_params(self, value)


class ComboBoxColorMap(QtGui.QWidget, UiCmap, ComboBox):
    """Combo box widget for colormap settings.

    Arguments:
    Awaits a single string value among the following list
    (All are matplotlib colormaps):
    * Gray
    * Hot
    * Winter
    * Gnuplot
    * Gnuplot2
    * Magma
    * Inferno
    * Plasma
    * Viridis

    This is a Qt derived object.
    """
    def __init__(self, *args):
        super(ComboBoxColorMap, self).__init__()
        self.setupUi(self)
        # Fill values with args
        if args:
            self.set_params(*args)
        self.show()


class ComboBoxContext(QtGui.QWidget, UiContext, ComboBox):
    """Combo box widget for tectonic context settings.

    Arguments:
    Awaits a single string value among the following list
    * Compression
    * Extension

    This is a Qt derived object.
    """
    def __init__(self, *args):
        super(ComboBoxContext, self).__init__()
        self.setupUi(self)
        # Fill values with args
        if args:
            self.set_params(*args)
        self.show()


if __name__ == "__main__":
    import sys
    try:
        app = QtGui.QApplication(sys.argv)
#        myapp = ComboBoxContext("Extension")
#        myapp = ComboBoxColorMap("Inferno")
        myapp = ComboBoxPoint('z')
#        myapp = ComboBoxLine("dashed")
        sys.exit(app.exec_())
    finally:
        print("params =", myapp.get_params())
        print("select =", myapp.get_select())
