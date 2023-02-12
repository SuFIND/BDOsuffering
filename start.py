import os
import time
import threading
import multiprocessing

import qdarkstyle

from PyQt6 import QtWidgets
from app.app import App
from utils.log_utils import Logger
from app.init_resource import init_config, init_resource, global_var
from app.app_thread import MsgHandleThread
from app.del_resource import release_resource


def main():
    import sys

    # 初始化日志模块
    Logger.info("app start ...")

    # 初始化配置模块
    config_path = os.environ.get("CFG_PATH", os.path.join(os.getcwd(), "config", "my_config.toml"))
    config = init_config(config_path)

    # 初始化必要资源
    init_resource(config)

    app = QtWidgets.QApplication(sys.argv)
    main_app = App()
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt6'))

    # 启动一个消息处理线程，处理子进程与主进程的消息
    msg_thread = MsgHandleThread()
    t = threading.Thread(target=msg_thread.run, args=(main_app,), daemon=True)
    t.start()

    global_var["threads"].append((t, msg_thread))

    main_app.show()

    exist_code = app.exec()
    release_resource(config)

    sys.exit(exist_code)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
