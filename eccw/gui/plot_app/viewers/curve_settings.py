# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uis/curve_settings.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(901, 257)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.groupBox_friction = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_friction.sizePolicy().hasHeightForWidth())
        self.groupBox_friction.setSizePolicy(sizePolicy)
        self.groupBox_friction.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_friction.setCheckable(False)
        self.groupBox_friction.setChecked(False)
        self.groupBox_friction.setObjectName(_fromUtf8("groupBox_friction"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_friction)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_phiB = QtGui.QLabel(self.groupBox_friction)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_phiB.sizePolicy().hasHeightForWidth())
        self.label_phiB.setSizePolicy(sizePolicy)
        self.label_phiB.setMaximumSize(QtCore.QSize(20, 24))
        self.label_phiB.setText(_fromUtf8(""))
        self.label_phiB.setPixmap(QtGui.QPixmap(_fromUtf8("../../../images/icon_params_phiB.png")))
        self.label_phiB.setScaledContents(True)
        self.label_phiB.setObjectName(_fromUtf8("label_phiB"))
        self.gridLayout.addWidget(self.label_phiB, 0, 0, 1, 1)
        self.horizontalLayout_phiB = QtGui.QHBoxLayout()
        self.horizontalLayout_phiB.setSpacing(0)
        self.horizontalLayout_phiB.setObjectName(_fromUtf8("horizontalLayout_phiB"))
        self.gridLayout.addLayout(self.horizontalLayout_phiB, 0, 1, 1, 1)
        self.label_phiD = QtGui.QLabel(self.groupBox_friction)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_phiD.sizePolicy().hasHeightForWidth())
        self.label_phiD.setSizePolicy(sizePolicy)
        self.label_phiD.setMaximumSize(QtCore.QSize(20, 24))
        self.label_phiD.setPixmap(QtGui.QPixmap(_fromUtf8("../../../images/icon_params_phiD.png")))
        self.label_phiD.setScaledContents(True)
        self.label_phiD.setObjectName(_fromUtf8("label_phiD"))
        self.gridLayout.addWidget(self.label_phiD, 1, 0, 1, 1)
        self.horizontalLayout_phiD = QtGui.QHBoxLayout()
        self.horizontalLayout_phiD.setSpacing(0)
        self.horizontalLayout_phiD.setObjectName(_fromUtf8("horizontalLayout_phiD"))
        self.gridLayout.addLayout(self.horizontalLayout_phiD, 1, 1, 1, 1)
        self.horizontalLayout_11.addWidget(self.groupBox_friction)
        self.groupBox_fluids = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_fluids.sizePolicy().hasHeightForWidth())
        self.groupBox_fluids.setSizePolicy(sizePolicy)
        self.groupBox_fluids.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_fluids.setCheckable(True)
        self.groupBox_fluids.setChecked(False)
        self.groupBox_fluids.setObjectName(_fromUtf8("groupBox_fluids"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_fluids)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_lamdaB = QtGui.QLabel(self.groupBox_fluids)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_lamdaB.sizePolicy().hasHeightForWidth())
        self.label_lamdaB.setSizePolicy(sizePolicy)
        self.label_lamdaB.setMaximumSize(QtCore.QSize(30, 24))
        self.label_lamdaB.setPixmap(QtGui.QPixmap(_fromUtf8("../../../images/icon_params_lamdaB.png")))
        self.label_lamdaB.setScaledContents(True)
        self.label_lamdaB.setObjectName(_fromUtf8("label_lamdaB"))
        self.gridLayout_2.addWidget(self.label_lamdaB, 0, 0, 1, 1)
        self.horizontalLayout_lamdaB = QtGui.QHBoxLayout()
        self.horizontalLayout_lamdaB.setSpacing(0)
        self.horizontalLayout_lamdaB.setObjectName(_fromUtf8("horizontalLayout_lamdaB"))
        self.gridLayout_2.addLayout(self.horizontalLayout_lamdaB, 0, 1, 1, 1)
        self.label_rhof = QtGui.QLabel(self.groupBox_fluids)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rhof.sizePolicy().hasHeightForWidth())
        self.label_rhof.setSizePolicy(sizePolicy)
        self.label_rhof.setMaximumSize(QtCore.QSize(24, 24))
        self.label_rhof.setText(_fromUtf8(""))
        self.label_rhof.setPixmap(QtGui.QPixmap(_fromUtf8("../../../images/icon_params_rhof.png")))
        self.label_rhof.setScaledContents(True)
        self.label_rhof.setObjectName(_fromUtf8("label_rhof"))
        self.gridLayout_2.addWidget(self.label_rhof, 0, 2, 1, 1)
        self.horizontalLayout_rhof = QtGui.QHBoxLayout()
        self.horizontalLayout_rhof.setSpacing(0)
        self.horizontalLayout_rhof.setObjectName(_fromUtf8("horizontalLayout_rhof"))
        self.gridLayout_2.addLayout(self.horizontalLayout_rhof, 0, 3, 1, 1)
        self.label_lamdaD = QtGui.QLabel(self.groupBox_fluids)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_lamdaD.sizePolicy().hasHeightForWidth())
        self.label_lamdaD.setSizePolicy(sizePolicy)
        self.label_lamdaD.setMaximumSize(QtCore.QSize(30, 24))
        self.label_lamdaD.setText(_fromUtf8(""))
        self.label_lamdaD.setPixmap(QtGui.QPixmap(_fromUtf8("../../../images/icon_params_lamdaD.png")))
        self.label_lamdaD.setScaledContents(True)
        self.label_lamdaD.setObjectName(_fromUtf8("label_lamdaD"))
        self.gridLayout_2.addWidget(self.label_lamdaD, 1, 0, 1, 1)
        self.label_rhosr = QtGui.QLabel(self.groupBox_fluids)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rhosr.sizePolicy().hasHeightForWidth())
        self.label_rhosr.setSizePolicy(sizePolicy)
        self.label_rhosr.setMaximumSize(QtCore.QSize(24, 24))
        self.label_rhosr.setText(_fromUtf8(""))
        self.label_rhosr.setPixmap(QtGui.QPixmap(_fromUtf8("../../../images/icon_params_rhosr.png")))
        self.label_rhosr.setScaledContents(True)
        self.label_rhosr.setObjectName(_fromUtf8("label_rhosr"))
        self.gridLayout_2.addWidget(self.label_rhosr, 1, 2, 1, 1)
        self.horizontalLayout_rhosr = QtGui.QHBoxLayout()
        self.horizontalLayout_rhosr.setSpacing(0)
        self.horizontalLayout_rhosr.setObjectName(_fromUtf8("horizontalLayout_rhosr"))
        self.gridLayout_2.addLayout(self.horizontalLayout_rhosr, 1, 3, 1, 1)
        self.horizontalLayout_lamdaD = QtGui.QHBoxLayout()
        self.horizontalLayout_lamdaD.setSpacing(0)
        self.horizontalLayout_lamdaD.setObjectName(_fromUtf8("horizontalLayout_lamdaD"))
        self.gridLayout_2.addLayout(self.horizontalLayout_lamdaD, 1, 1, 1, 1)
        self.horizontalLayout_11.addWidget(self.groupBox_fluids)
        self.verticalLayout_context = QtGui.QVBoxLayout()
        self.verticalLayout_context.setObjectName(_fromUtf8("verticalLayout_context"))
        self.horizontalLayout_11.addLayout(self.verticalLayout_context)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.dummyVerticalLayout = QtGui.QVBoxLayout()
        self.dummyVerticalLayout.setObjectName(_fromUtf8("dummyVerticalLayout"))
        self.pushButton_kill = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_kill.sizePolicy().hasHeightForWidth())
        self.pushButton_kill.setSizePolicy(sizePolicy)
        self.pushButton_kill.setMaximumSize(QtCore.QSize(28, 28))
        self.pushButton_kill.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../images/icon_close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_kill.setIcon(icon)
        self.pushButton_kill.setObjectName(_fromUtf8("pushButton_kill"))
        self.dummyVerticalLayout.addWidget(self.pushButton_kill)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.dummyVerticalLayout.addItem(spacerItem1)
        self.horizontalLayout_11.addLayout(self.dummyVerticalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_curve = QtGui.QHBoxLayout()
        self.horizontalLayout_curve.setObjectName(_fromUtf8("horizontalLayout_curve"))
        self.checkBox_splittedCurves = QtGui.QCheckBox(Form)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_splittedCurves.setFont(font)
        self.checkBox_splittedCurves.setObjectName(_fromUtf8("checkBox_splittedCurves"))
        self.horizontalLayout_curve.addWidget(self.checkBox_splittedCurves)
        self.checkBox_reverseColormap = QtGui.QCheckBox(Form)
        self.checkBox_reverseColormap.setEnabled(False)
        self.checkBox_reverseColormap.setObjectName(_fromUtf8("checkBox_reverseColormap"))
        self.horizontalLayout_curve.addWidget(self.checkBox_reverseColormap)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_curve.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_curve)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_settings = QtGui.QVBoxLayout()
        self.verticalLayout_settings.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_settings.setSpacing(0)
        self.verticalLayout_settings.setObjectName(_fromUtf8("verticalLayout_settings"))
        self.horizontalLayout_6.addLayout(self.verticalLayout_settings)
        self.horizontalLayout_label = QtGui.QHBoxLayout()
        self.horizontalLayout_label.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_label.setObjectName(_fromUtf8("horizontalLayout_label"))
        self.horizontalLayout_6.addLayout(self.horizontalLayout_label)
        spacerItem3 = QtGui.QSpacerItem(150, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem4 = QtGui.QSpacerItem(20, 25, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_curvepoints = QtGui.QHBoxLayout()
        self.horizontalLayout_curvepoints.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_curvepoints.setObjectName(_fromUtf8("horizontalLayout_curvepoints"))
        self.pushButton_addCurvePoint = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_addCurvePoint.sizePolicy().hasHeightForWidth())
        self.pushButton_addCurvePoint.setSizePolicy(sizePolicy)
        self.pushButton_addCurvePoint.setMaximumSize(QtCore.QSize(28, 28))
        self.pushButton_addCurvePoint.setObjectName(_fromUtf8("pushButton_addCurvePoint"))
        self.horizontalLayout_curvepoints.addWidget(self.pushButton_addCurvePoint)
        self.label_CurvePoint = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_CurvePoint.setFont(font)
        self.label_CurvePoint.setObjectName(_fromUtf8("label_CurvePoint"))
        self.horizontalLayout_curvepoints.addWidget(self.label_CurvePoint)
        self.line = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_curvepoints.addWidget(self.line)
        self.pushButton_killAllCurvePoints = QtGui.QPushButton(Form)
        self.pushButton_killAllCurvePoints.setEnabled(False)
        self.pushButton_killAllCurvePoints.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_killAllCurvePoints.setObjectName(_fromUtf8("pushButton_killAllCurvePoints"))
        self.horizontalLayout_curvepoints.addWidget(self.pushButton_killAllCurvePoints)
        self.verticalLayout.addLayout(self.horizontalLayout_curvepoints)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setMinimumSize(QtCore.QSize(28, 0))
        self.line_2.setBaseSize(QtCore.QSize(50, 0))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_points_settings = QtGui.QVBoxLayout()
        self.verticalLayout_points_settings.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_points_settings.setSpacing(6)
        self.verticalLayout_points_settings.setObjectName(_fromUtf8("verticalLayout_points_settings"))
        self.horizontalLayout.addLayout(self.verticalLayout_points_settings)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_kill, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox_friction.setTitle(_translate("Form", "Frictional parameters", None))
        self.label_phiB.setToolTip(_translate("Form", "Bulk friction angle [deg]", None))
        self.label_phiD.setToolTip(_translate("Form", "Basal friction angle [deg]", None))
        self.groupBox_fluids.setToolTip(_translate("Form", "Check to activate fluids pore pressure parameters", None))
        self.groupBox_fluids.setTitle(_translate("Form", "Fluids pore pressure", None))
        self.label_lamdaB.setToolTip(_translate("Form", "Bulk fluids overpressure ratio", None))
        self.label_rhof.setToolTip(_translate("Form", "Volumetric mass density of fluids", None))
        self.label_lamdaD.setToolTip(_translate("Form", "Basal fluids overpressure ratio", None))
        self.label_rhosr.setToolTip(_translate("Form", "Volumetric mass density of saturated rock", None))
        self.pushButton_kill.setToolTip(_translate("Form", "Delete this curve", None))
        self.checkBox_splittedCurves.setToolTip(_translate("Form", "Check to draw with separate settings normal and inverse faulting mechanisms", None))
        self.checkBox_splittedCurves.setText(_translate("Form", "Distinguish mechanisms", None))
        self.checkBox_reverseColormap.setToolTip(_translate("Form", "Check to reverse colormap", None))
        self.checkBox_reverseColormap.setText(_translate("Form", "Reverse colormap", None))
        self.pushButton_addCurvePoint.setToolTip(_translate("Form", "Add a new point on current curve", None))
        self.pushButton_addCurvePoint.setText(_translate("Form", "+", None))
        self.label_CurvePoint.setText(_translate("Form", "Points on this curve", None))
        self.pushButton_killAllCurvePoints.setToolTip(_translate("Form", "Delete all points on current curve", None))
        self.pushButton_killAllCurvePoints.setText(_translate("Form", "Clear all", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

