import os
from threading import Thread

import toml
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtCore import pyqtSignal
from ui.ui_app import Ui_MainWindow
from system_hotkey import SystemHotkey

from app.app_thread import GMAlarmThread
from app.init_resource import global_var
from control.GMCheckDialog import GMCheckDialog


class App(QMainWindow, Ui_MainWindow):
    sig_hotkey = pyqtSignal(str)
    sig_gm_check = pyqtSignal(str)

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)

        self.sig_hotkey.connect(self.handleHotKeyEvent)
        self.sig_gm_check.connect(self.showGMCheckDialog)

        self.hk_start_pause = SystemHotkey()
        self.hk_stop = SystemHotkey()
        self.hk_test = SystemHotkey()

        self.hk_start_pause.register(('f10',), callback=lambda x: self.sendHotKeySig('f10'))
        self.hk_stop.register(('f11',), callback=lambda x: self.sendHotKeySig('f11'))
        self.hk_test.register(('f9',), callback=lambda x: self.sendHotKeySig('f9'))

        self.actionSaveConfig.triggered.connect(self.save_config)

    def sendHotKeySig(self, i_str):
        self.sig_hotkey.emit(i_str)

    def handleHotKeyEvent(self, i_str):
        if i_str == 'f10':
            # 开始 / 暂停
            self.OpCtrl.clicked_for_start_pause_button()
        if i_str == 'f11':
            # 停止
            self.OpCtrl.clicked_for_end_button()
        if i_str == 'f9':
            # 仅合球
            self.OpCtrl.clicked_for_al_button()

    def showGMCheckDialog(self, i_str):
        # 启动警报音的播放线程
        alarm_thread = GMAlarmThread()
        t = Thread(target=alarm_thread.run, args=())
        t.start()
        global_var["threads"].append((t, alarm_thread))

        # 展示弹窗信息
        dialog = GMCheckDialog(self)
        dialog.show()

    def save_config(self):
        """保存配置逻辑"""
        available, rst, reason = self.OpCtrl.collect()
        if available:
            toml_content = toml.dumps(rst)

            fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                                                    caption="配置文件",
                                                                    directory=os.path.join(os.getcwd(), "config"),  # 起始路径
                                                                    filter="Toml Files (*.toml);;All Files (*)",
                                                                    initialFilter="Toml Files (*.toml)")
            if fileName_choose == "":
                # 取消选择
                return

            with open(fileName_choose, 'w', encoding="utf-8") as fp:
                fp.write(toml_content)
