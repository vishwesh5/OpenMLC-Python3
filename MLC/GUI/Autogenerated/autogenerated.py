# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './untitled/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MLCManager(object):
    def setupUi(self, MLCManager):
        MLCManager.setObjectName("MLCManager")
        MLCManager.resize(749, 585)
        self.centralWidget = QtWidgets.QWidget(MLCManager)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projects_box = QtWidgets.QGroupBox(self.centralWidget)
        self.projects_box.setObjectName("projects_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.projects_box)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.projects_box)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.new_button = QtWidgets.QToolButton(self.frame)
        self.new_button.setObjectName("new_button")
        self.horizontalLayout_3.addWidget(self.new_button)
        self.open_button = QtWidgets.QToolButton(self.frame)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout_3.addWidget(self.open_button)
        self.clone_button = QtWidgets.QToolButton(self.frame)
        self.clone_button.setObjectName("clone_button")
        self.horizontalLayout_3.addWidget(self.clone_button)
        self.remove_button = QtWidgets.QToolButton(self.frame)
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout_3.addWidget(self.remove_button)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.experiment_list = QtWidgets.QListView(self.projects_box)
        self.experiment_list.setObjectName("experiment_list")
        self.verticalLayout.addWidget(self.experiment_list)
        self.horizontalLayout.addWidget(self.projects_box)
        self.description_box = QtWidgets.QGroupBox(self.centralWidget)
        self.description_box.setObjectName("description_box")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.description_box)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.experiment_description = QtWidgets.QTextBrowser(self.description_box)
        self.experiment_description.setObjectName("experiment_description")
        self.horizontalLayout_2.addWidget(self.experiment_description)
        self.horizontalLayout.addWidget(self.description_box)
        MLCManager.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MLCManager)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 749, 19))
        self.menuBar.setObjectName("menuBar")
        self.menuMLC = QtWidgets.QMenu(self.menuBar)
        self.menuMLC.setObjectName("menuMLC")
        self.menuProperties = QtWidgets.QMenu(self.menuBar)
        self.menuProperties.setObjectName("menuProperties")
        MLCManager.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MLCManager)
        self.statusBar.setObjectName("statusBar")
        MLCManager.setStatusBar(self.statusBar)
        self.menu_properties = QtWidgets.QAction(MLCManager)
        self.menu_properties.setObjectName("menu_properties")
        self.menu_close = QtWidgets.QAction(MLCManager)
        self.menu_close.setObjectName("menu_close")
        self.menu_about = QtWidgets.QAction(MLCManager)
        self.menu_about.setObjectName("menu_about")
        self.menuMLC.addAction(self.menu_properties)
        self.menuMLC.addSeparator()
        self.menuMLC.addAction(self.menu_close)
        self.menuProperties.addAction(self.menu_about)
        self.menuBar.addAction(self.menuMLC.menuAction())
        self.menuBar.addAction(self.menuProperties.menuAction())

        self.retranslateUi(MLCManager)
        self.menu_close.triggered.connect(MLCManager.close)
        self.clone_button.clicked.connect(MLCManager.on_clone_button_clicked)
        self.new_button.clicked.connect(MLCManager.on_new_button_clicked)
        self.remove_button.clicked.connect(MLCManager.on_remove_button_clicked)
        self.open_button.clicked.connect(MLCManager.on_open_button_clicked)
        self.experiment_list.clicked['QModelIndex'].connect(MLCManager.on_experiment_list_clicked)
        self.menu_properties.triggered.connect(MLCManager.edit_gui_config)
        self.experiment_list.activated['QModelIndex'].connect(MLCManager.on_experiment_list_clicked)
        # QtCore.QMetaObject.connectSlotsByName(MLCManager)

    def retranslateUi(self, MLCManager):
        _translate = QtCore.QCoreApplication.translate
        MLCManager.setWindowTitle(_translate("MLCManager", "MLC Project Manager"))
        self.projects_box.setTitle(_translate("MLCManager", "Projects"))
        self.new_button.setText(_translate("MLCManager", "New"))
        self.open_button.setText(_translate("MLCManager", "Open"))
        self.clone_button.setText(_translate("MLCManager", "Clone"))
        self.remove_button.setText(_translate("MLCManager", "Remove"))
        self.description_box.setTitle(_translate("MLCManager", "Description"))
        self.menuMLC.setTitle(_translate("MLCManager", "MLC"))
        self.menuProperties.setTitle(_translate("MLCManager", "Help"))
        self.menu_properties.setText(_translate("MLCManager", "Properties"))
        self.menu_properties.setToolTip(_translate("MLCManager", "Manager Properties"))
        self.menu_close.setText(_translate("MLCManager", "Close"))
        self.menu_close.setToolTip(_translate("MLCManager", "Close MLC Manager"))
        self.menu_about.setText(_translate("MLCManager", "About"))
        self.menu_about.setToolTip(_translate("MLCManager", "Project Information"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './untitled/experiment.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Experiment(object):
    def setupUi(self, Experiment):
        Experiment.setObjectName("Experiment")
        Experiment.resize(555, 447)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Experiment)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Experiment)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.config_tab = QtWidgets.QWidget()
        self.config_tab.setObjectName("config_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.config_tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.config_tab)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.config_table = QtWidgets.QTableView(self.groupBox)
        self.config_table.setObjectName("config_table")
        self.horizontalLayout_3.addWidget(self.config_table)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.frame)
        self.tabWidget.addTab(self.config_tab, "")
        self.results_tab = QtWidgets.QWidget()
        self.results_tab.setObjectName("results_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.results_tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graph_frame = QtWidgets.QFrame(self.results_tab)
        self.graph_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph_frame.setObjectName("graph_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.graph_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.graph_frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gen_count_label = QtWidgets.QLabel(self.frame_5)
        self.gen_count_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gen_count_label.sizePolicy().hasHeightForWidth())
        self.gen_count_label.setSizePolicy(sizePolicy)
        self.gen_count_label.setAutoFillBackground(True)
        self.gen_count_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.gen_count_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gen_count_label.setLineWidth(2)
        self.gen_count_label.setText("")
        self.gen_count_label.setTextFormat(QtCore.Qt.RichText)
        self.gen_count_label.setScaledContents(False)
        self.gen_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gen_count_label.setObjectName("gen_count_label")
        self.verticalLayout_6.addWidget(self.gen_count_label)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.prev_gen_button = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.prev_gen_button.setFont(font)
        self.prev_gen_button.setIconSize(QtCore.QSize(8, 8))
        self.prev_gen_button.setObjectName("prev_gen_button")
        self.horizontalLayout_5.addWidget(self.prev_gen_button)
        self.next_gen_button = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.next_gen_button.setFont(font)
        self.next_gen_button.setIconSize(QtCore.QSize(8, 8))
        self.next_gen_button.setAutoDefault(True)
        self.next_gen_button.setObjectName("next_gen_button")
        self.horizontalLayout_5.addWidget(self.next_gen_button)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.log_check = QtWidgets.QCheckBox(self.frame_4)
        self.log_check.setObjectName("log_check")
        self.verticalLayout_4.addWidget(self.log_check)
        self.show_all_check = QtWidgets.QCheckBox(self.frame_4)
        self.show_all_check.setObjectName("show_all_check")
        self.verticalLayout_4.addWidget(self.show_all_check)
        self.dimension_check = QtWidgets.QCheckBox(self.frame_4)
        self.dimension_check.setObjectName("dimension_check")
        self.verticalLayout_4.addWidget(self.dimension_check)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.verticalLayout_6.setStretch(1, 3)
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.indiv_graph_frame = QtWidgets.QFrame(self.graph_frame)
        self.indiv_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.indiv_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.indiv_graph_frame.setObjectName("indiv_graph_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.indiv_graph_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.indiv_graph_frame)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout_4.addWidget(self.indiv_graph_frame)
        self.verticalLayout_3.addWidget(self.graph_frame)
        self.frame_3 = QtWidgets.QFrame(self.results_tab)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.db_view = QtWidgets.QTableView(self.frame_3)
        self.db_view.setObjectName("db_view")
        self.verticalLayout_5.addWidget(self.db_view)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_7 = QtWidgets.QFrame(self.results_tab)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_6.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_6.addWidget(self.pushButton_7)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.tabWidget.addTab(self.results_tab, "")
        self.experiment_tab = QtWidgets.QWidget()
        self.experiment_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.experiment_tab.setObjectName("experiment_tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.experiment_tab)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_9 = QtWidgets.QFrame(self.experiment_tab)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_12 = QtWidgets.QFrame(self.frame_9)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_12)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_12)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_4.addWidget(self.pushButton_9, 0, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_4.addWidget(self.pushButton_10, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_12, 2, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.experiment_tab)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.test_button = QtWidgets.QPushButton(self.frame_11)
        self.test_button.setObjectName("test_button")
        self.gridLayout_2.addWidget(self.test_button, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_11)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.test_edit = QtWidgets.QLineEdit(self.frame_11)
        self.test_edit.setObjectName("test_edit")
        self.gridLayout_2.addWidget(self.test_edit, 0, 1, 1, 1)
        self.verticalLayout_9.addWidget(self.frame_11)
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.from_gen_combo = QtWidgets.QComboBox(self.frame_10)
        self.from_gen_combo.setObjectName("from_gen_combo")
        self.gridLayout_5.addWidget(self.from_gen_combo, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 1, 1, 1)
        self.to_gen_combo = QtWidgets.QComboBox(self.frame_10)
        self.to_gen_combo.setObjectName("to_gen_combo")
        self.gridLayout_5.addWidget(self.to_gen_combo, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_10)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 1, 1, 1)
        self.start_button = QtWidgets.QPushButton(self.frame_10)
        self.start_button.setObjectName("start_button")
        self.gridLayout_5.addWidget(self.start_button, 1, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.frame_10)
        self.verticalLayout_8.addWidget(self.frame_8)
        self.tabWidget.addTab(self.experiment_tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Experiment)
        self.tabWidget.setCurrentIndex(1)
        Experiment.finished['int'].connect(Experiment.on_closed_dialog)
        self.start_button.clicked.connect(Experiment.on_start_button_clicked)
        self.next_gen_button.clicked.connect(Experiment.on_next_gen_button_clicked)
        self.prev_gen_button.clicked.connect(Experiment.on_prev_gen_button_clicked)
        self.show_all_check.clicked.connect(Experiment.on_show_all_check_clicked)
        self.log_check.clicked.connect(Experiment.on_log_check_clicked)
        self.dimension_check.clicked.connect(Experiment.on_dimension_check_clicked)
        # QtCore.QMetaObject.connectSlotsByName(Experiment)

    def retranslateUi(self, Experiment):
        _translate = QtCore.QCoreApplication.translate
        Experiment.setWindowTitle(_translate("Experiment", "Dialog"))
        self.pushButton.setText(_translate("Experiment", "Import"))
        self.pushButton_2.setText(_translate("Experiment", "Export"))
        self.groupBox.setTitle(_translate("Experiment", "Experiment properties"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config_tab), _translate("Experiment", "Configuration"))
        self.gen_count_label.setWhatsThis(_translate("Experiment", "Current population"))
        self.prev_gen_button.setText(_translate("Experiment", "<<"))
        self.next_gen_button.setText(_translate("Experiment", ">>"))
        self.log_check.setText(_translate("Experiment", "Log"))
        self.show_all_check.setText(_translate("Experiment", "Show all"))
        self.dimension_check.setText(_translate("Experiment", "3D"))
        self.pushButton_5.setText(_translate("Experiment", "Create"))
        self.pushButton_6.setText(_translate("Experiment", "Cut"))
        self.pushButton_7.setText(_translate("Experiment", "Import"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.results_tab), _translate("Experiment", "Results"))
        self.label_4.setText(_translate("Experiment", "Evaluation Script:"))
        self.label_3.setText(_translate("Experiment", "Preevaluation Script:"))
        self.pushButton_9.setText(_translate("Experiment", "Edit"))
        self.pushButton_10.setText(_translate("Experiment", "Edit"))
        self.test_button.setText(_translate("Experiment", "Test"))
        self.label_2.setText(_translate("Experiment", "Test Individual:"))
        self.label_5.setText(_translate("Experiment", "To Generation:"))
        self.label_6.setText(_translate("Experiment", "From Generation:"))
        self.start_button.setText(_translate("Experiment", "Start Experiment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.experiment_tab), _translate("Experiment", "Experiment"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './untitled/edit_properties.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PropertiesDialog(object):
    def setupUi(self, PropertiesDialog):
        PropertiesDialog.setObjectName("PropertiesDialog")
        PropertiesDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        PropertiesDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(PropertiesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(PropertiesDialog)
        self.tableView.setFrameShape(QtWidgets.QFrame.HLine)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setSortIndicatorShown(True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableView)
        self.buttonBox = QtWidgets.QDialogButtonBox(PropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PropertiesDialog)
        self.buttonBox.accepted.connect(PropertiesDialog.accept)
        self.buttonBox.rejected.connect(PropertiesDialog.reject)
        # QtCore.QMetaObject.connectSlotsByName(PropertiesDialog)

    def retranslateUi(self, PropertiesDialog):
        _translate = QtCore.QCoreApplication.translate
        PropertiesDialog.setWindowTitle(_translate("PropertiesDialog", "MLC Manager Properties"))

