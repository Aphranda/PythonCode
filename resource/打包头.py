import sys,os
#注意就是下面的 if 语句
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

# import others
"""
pyinstaller --hidden-import=queue -w -F

或

pyinstaller.exe  -w -F --hidden-import=queue main.py

QApplication.processEvents() 界面刷新
"""
