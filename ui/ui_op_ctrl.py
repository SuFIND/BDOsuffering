# Form implementation generated from reading ui file 'designer\op.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OpCtrl(object):
    def setupUi(self, OpCtrl):
        OpCtrl.setObjectName("OpCtrl")
        OpCtrl.resize(561, 410)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(OpCtrl)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=OpCtrl)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.BasicTab = QtWidgets.QWidget()
        self.BasicTab.setObjectName("BasicTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.BasicTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(parent=self.BasicTab)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 2, 1, 1)
        self.AuditionAlarmButton = QtWidgets.QPushButton(parent=self.BasicTab)
        self.AuditionAlarmButton.setObjectName("AuditionAlarmButton")
        self.gridLayout.addWidget(self.AuditionAlarmButton, 13, 1, 1, 1)
        self.UseWarehouseMaidCheckBox = QtWidgets.QCheckBox(parent=self.BasicTab)
        self.UseWarehouseMaidCheckBox.setChecked(True)
        self.UseWarehouseMaidCheckBox.setObjectName("UseWarehouseMaidCheckBox")
        self.gridLayout.addWidget(self.UseWarehouseMaidCheckBox, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.BasicTab)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 2, 1, 1)
        self.RecycleTentkeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.BasicTab)
        self.RecycleTentkeySequenceEdit.setObjectName("RecycleTentkeySequenceEdit")
        self.gridLayout.addWidget(self.RecycleTentkeySequenceEdit, 7, 3, 1, 1)
        self.BackExchangeCheckBox = QtWidgets.QCheckBox(parent=self.BasicTab)
        self.BackExchangeCheckBox.setChecked(True)
        self.BackExchangeCheckBox.setObjectName("BackExchangeCheckBox")
        self.gridLayout.addWidget(self.BackExchangeCheckBox, 8, 1, 1, 1)
        self.RepairWeaponsCheckBox = QtWidgets.QCheckBox(parent=self.BasicTab)
        self.RepairWeaponsCheckBox.setChecked(True)
        self.RepairWeaponsCheckBox.setObjectName("RepairWeaponsCheckBox")
        self.gridLayout.addWidget(self.RepairWeaponsCheckBox, 5, 1, 1, 1)
        self.IntoHuttonCheckBox = QtWidgets.QCheckBox(parent=self.BasicTab)
        self.IntoHuttonCheckBox.setTristate(False)
        self.IntoHuttonCheckBox.setObjectName("IntoHuttonCheckBox")
        self.gridLayout.addWidget(self.IntoHuttonCheckBox, 10, 1, 1, 1)
        self.EmailEdit = QtWidgets.QLineEdit(parent=self.BasicTab)
        self.EmailEdit.setObjectName("EmailEdit")
        self.gridLayout.addWidget(self.EmailEdit, 13, 3, 1, 1)
        self.StartAtCallPlaceButton = QtWidgets.QRadioButton(parent=self.BasicTab)
        self.StartAtCallPlaceButton.setChecked(False)
        self.StartAtCallPlaceButton.setObjectName("StartAtCallPlaceButton")
        self.gridLayout.addWidget(self.StartAtCallPlaceButton, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.BasicTab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.BasicTab)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 11, 1, 1, 1)
        self.RepairWeaponskeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.BasicTab)
        self.RepairWeaponskeySequenceEdit.setObjectName("RepairWeaponskeySequenceEdit")
        self.gridLayout.addWidget(self.RepairWeaponskeySequenceEdit, 6, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.BasicTab)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.BasicTab)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 2, 1, 1)
        self.WarehouseMaidkeySequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.BasicTab)
        self.WarehouseMaidkeySequenceEdit.setObjectName("WarehouseMaidkeySequenceEdit")
        self.gridLayout.addWidget(self.WarehouseMaidkeySequenceEdit, 4, 3, 1, 1)
        self.ResetViewCheckBox = QtWidgets.QCheckBox(parent=self.BasicTab)
        self.ResetViewCheckBox.setChecked(True)
        self.ResetViewCheckBox.setTristate(False)
        self.ResetViewCheckBox.setObjectName("ResetViewCheckBox")
        self.gridLayout.addWidget(self.ResetViewCheckBox, 1, 1, 1, 1)
        self.SetTentSequenceEdit = QtWidgets.QKeySequenceEdit(parent=self.BasicTab)
        self.SetTentSequenceEdit.setObjectName("SetTentSequenceEdit")
        self.gridLayout.addWidget(self.SetTentSequenceEdit, 5, 3, 1, 1)
        self.TestButton = QtWidgets.QPushButton(parent=self.BasicTab)
        self.TestButton.setObjectName("TestButton")
        self.gridLayout.addWidget(self.TestButton, 10, 3, 1, 1)
        self.EmailAlarmCheckBox = QtWidgets.QCheckBox(parent=self.BasicTab)
        self.EmailAlarmCheckBox.setObjectName("EmailAlarmCheckBox")
        self.gridLayout.addWidget(self.EmailAlarmCheckBox, 13, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.BasicTab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.BasicTab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 1, 1, 1)
        self.StartAtTradingWarehouseButton = QtWidgets.QRadioButton(parent=self.BasicTab)
        self.StartAtTradingWarehouseButton.setChecked(True)
        self.StartAtTradingWarehouseButton.setObjectName("StartAtTradingWarehouseButton")
        self.gridLayout.addWidget(self.StartAtTradingWarehouseButton, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.BasicTab, "")
        self.TimeTab = QtWidgets.QWidget()
        self.TimeTab.setObjectName("TimeTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.TimeTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Boss2CanBeHitCoolTimeEdit = QtWidgets.QLineEdit(parent=self.TimeTab)
        self.Boss2CanBeHitCoolTimeEdit.setObjectName("Boss2CanBeHitCoolTimeEdit")
        self.gridLayout_4.addWidget(self.Boss2CanBeHitCoolTimeEdit, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.TimeTab)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.SkillGroup1KillBoss1CostEdit = QtWidgets.QLineEdit(parent=self.TimeTab)
        self.SkillGroup1KillBoss1CostEdit.setObjectName("SkillGroup1KillBoss1CostEdit")
        self.gridLayout_4.addWidget(self.SkillGroup1KillBoss1CostEdit, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.TimeTab)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)
        self.Boss1CanBeHitCoolTimeEdit = QtWidgets.QLineEdit(parent=self.TimeTab)
        self.Boss1CanBeHitCoolTimeEdit.setObjectName("Boss1CanBeHitCoolTimeEdit")
        self.gridLayout_4.addWidget(self.Boss1CanBeHitCoolTimeEdit, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.TimeTab)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.TimeTab)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 3, 0, 1, 1)
        self.backTradingHouseTimeEdit = QtWidgets.QLineEdit(parent=self.TimeTab)
        self.backTradingHouseTimeEdit.setObjectName("backTradingHouseTimeEdit")
        self.gridLayout_4.addWidget(self.backTradingHouseTimeEdit, 3, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.TimeTab, "")
        self.DataCollectionTab = QtWidgets.QWidget()
        self.DataCollectionTab.setObjectName("DataCollectionTab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.DataCollectionTab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.CollectMagramOrKhalkCheckBox = QtWidgets.QCheckBox(parent=self.DataCollectionTab)
        self.CollectMagramOrKhalkCheckBox.setObjectName("CollectMagramOrKhalkCheckBox")
        self.gridLayout_6.addWidget(self.CollectMagramOrKhalkCheckBox, 3, 0, 1, 1)
        self.CollectTaskOverCheckBox = QtWidgets.QCheckBox(parent=self.DataCollectionTab)
        self.CollectTaskOverCheckBox.setObjectName("CollectTaskOverCheckBox")
        self.gridLayout_6.addWidget(self.CollectTaskOverCheckBox, 0, 0, 1, 1)
        self.CollectUseWarehouseMaidCheckBox = QtWidgets.QCheckBox(parent=self.DataCollectionTab)
        self.CollectUseWarehouseMaidCheckBox.setObjectName("CollectUseWarehouseMaidCheckBox")
        self.gridLayout_6.addWidget(self.CollectUseWarehouseMaidCheckBox, 4, 0, 1, 1)
        self.CollectBagUiCheckBox = QtWidgets.QCheckBox(parent=self.DataCollectionTab)
        self.CollectBagUiCheckBox.setObjectName("CollectBagUiCheckBox")
        self.gridLayout_6.addWidget(self.CollectBagUiCheckBox, 1, 0, 1, 1)
        self.CollectProcessBarCheckBox = QtWidgets.QCheckBox(parent=self.DataCollectionTab)
        self.CollectProcessBarCheckBox.setObjectName("CollectProcessBarCheckBox")
        self.gridLayout_6.addWidget(self.CollectProcessBarCheckBox, 2, 0, 1, 1)
        self.CollectFindNPCCheckBox = QtWidgets.QCheckBox(parent=self.DataCollectionTab)
        self.CollectFindNPCCheckBox.setObjectName("CollectFindNPCCheckBox")
        self.gridLayout_6.addWidget(self.CollectFindNPCCheckBox, 5, 0, 1, 1)
        self.CollectGMCheck = QtWidgets.QCheckBox(parent=self.DataCollectionTab)
        self.CollectGMCheck.setChecked(True)
        self.CollectGMCheck.setObjectName("CollectGMCheck")
        self.gridLayout_6.addWidget(self.CollectGMCheck, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.DataCollectionTab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=OpCtrl)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StartPauseButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.StartPauseButton.setObjectName("StartPauseButton")
        self.horizontalLayout.addWidget(self.StartPauseButton)
        self.EndButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.EndButton.setObjectName("EndButton")
        self.horizontalLayout.addWidget(self.EndButton)
        self.MergeALButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.MergeALButton.setObjectName("MergeALButton")
        self.horizontalLayout.addWidget(self.MergeALButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(OpCtrl)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OpCtrl)

    def retranslateUi(self, OpCtrl):
        _translate = QtCore.QCoreApplication.translate
        OpCtrl.setWindowTitle(_translate("OpCtrl", "Form"))
        self.label_6.setText(_translate("OpCtrl", "帐篷修理 alt +"))
        self.AuditionAlarmButton.setText(_translate("OpCtrl", "试听GM警报"))
        self.UseWarehouseMaidCheckBox.setToolTip(_translate("OpCtrl", "需要至少有4个仓库女仆，存放：記憶的碎片、獵人勛章、以及兩種召喚怪物掉落的雜物"))
        self.UseWarehouseMaidCheckBox.setText(_translate("OpCtrl", "女仆存放杂物"))
        self.label_2.setText(_translate("OpCtrl", "仓库女仆 alt +"))
        self.RecycleTentkeySequenceEdit.setKeySequence(_translate("OpCtrl", "5"))
        self.BackExchangeCheckBox.setToolTip(_translate("OpCtrl", "开启后，角色打完背包的球后会自动回到交易所取球，然后再回到球场继续打球"))
        self.BackExchangeCheckBox.setText(_translate("OpCtrl", "回到交易所"))
        self.RepairWeaponsCheckBox.setToolTip(_translate("OpCtrl", "需要购买珍珠商品帐篷"))
        self.RepairWeaponsCheckBox.setText(_translate("OpCtrl", "帐篷修理装备"))
        self.IntoHuttonCheckBox.setToolTip(_translate("OpCtrl", "BETA功能，确保游戏分辨率为1920 * 1080，需要确认所在线是否可以进入赫顿领域，赛季及新手线不支持"))
        self.IntoHuttonCheckBox.setText(_translate("OpCtrl", "进入赫顿领域"))
        self.EmailEdit.setPlaceholderText(_translate("OpCtrl", "请输入你的邮件地址"))
        self.StartAtCallPlaceButton.setText(_translate("OpCtrl", "从球点开始"))
        self.label.setText(_translate("OpCtrl", "开始前"))
        self.label_11.setText(_translate("OpCtrl", "GM督查相关"))
        self.RepairWeaponskeySequenceEdit.setKeySequence(_translate("OpCtrl", "4"))
        self.label_5.setText(_translate("OpCtrl", "设置帐篷 alt +"))
        self.label_7.setText(_translate("OpCtrl", "回收帐篷 alt +"))
        self.WarehouseMaidkeySequenceEdit.setKeySequence(_translate("OpCtrl", "1"))
        self.ResetViewCheckBox.setText(_translate("OpCtrl", "重置到最大视野"))
        self.SetTentSequenceEdit.setKeySequence(_translate("OpCtrl", "3"))
        self.TestButton.setToolTip(_translate("OpCtrl", "GM报警"))
        self.TestButton.setText(_translate("OpCtrl", "TEST"))
        self.EmailAlarmCheckBox.setText(_translate("OpCtrl", "邮件警报提醒"))
        self.label_3.setText(_translate("OpCtrl", "结束后"))
        self.label_4.setText(_translate("OpCtrl", "其他"))
        self.StartAtTradingWarehouseButton.setText(_translate("OpCtrl", "从交易所开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BasicTab), _translate("OpCtrl", "基础设置"))
        self.Boss2CanBeHitCoolTimeEdit.setText(_translate("OpCtrl", "12"))
        self.label_8.setText(_translate("OpCtrl", "召唤到玛格岚可以被打(s)"))
        self.SkillGroup1KillBoss1CostEdit.setText(_translate("OpCtrl", "1.5"))
        self.label_9.setText(_translate("OpCtrl", "玛格岚死到柯尔特出现(s)"))
        self.Boss1CanBeHitCoolTimeEdit.setText(_translate("OpCtrl", "36.5"))
        self.label_12.setText(_translate("OpCtrl", "技能组1预计击杀耗时(s)"))
        self.label_10.setText(_translate("OpCtrl", "球点至交易所的耗时(s)"))
        self.backTradingHouseTimeEdit.setText(_translate("OpCtrl", "140"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TimeTab), _translate("OpCtrl", "时间设置"))
        self.CollectMagramOrKhalkCheckBox.setText(_translate("OpCtrl", "采集玛格岚或柯尔克截图"))
        self.CollectTaskOverCheckBox.setText(_translate("OpCtrl", "采集任务完成截图"))
        self.CollectUseWarehouseMaidCheckBox.setText(_translate("OpCtrl", "采集仓库女仆清理背包截图"))
        self.CollectBagUiCheckBox.setText(_translate("OpCtrl", "采集收集背包UI截图"))
        self.CollectProcessBarCheckBox.setText(_translate("OpCtrl", "采集进度条截图"))
        self.CollectFindNPCCheckBox.setText(_translate("OpCtrl", "采集寻找NLP的UI截图"))
        self.CollectGMCheck.setText(_translate("OpCtrl", "采集GM督查截图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataCollectionTab), _translate("OpCtrl", "数据采集"))
        self.StartPauseButton.setText(_translate("OpCtrl", "开始 F10"))
        self.EndButton.setText(_translate("OpCtrl", "结束 F11"))
        self.MergeALButton.setText(_translate("OpCtrl", "合成古语 F9"))
