import time

import win32gui


# win32虽然也可控制键盘，但不如使用PyUserInput的方便。需要注意在windows和mac下接口参数可能有所不同。


def get_current_window():
    return win32gui.GetForegroundWindow()


def set_current_window(hwnd):
    win32gui.SetForegroundWindow(hwnd)


def get_window_title(hwnd):
    return win32gui.GetWindowText(hwnd)


def get_current_window_title():
    return get_window_title(get_current_window())


def find_window_by_title(title):
    try:
        return win32gui.FindWindow(None, title)
    except Exception as ex:
        print('error calling win32gui.FindWindow ' + str(ex))
        return -1


if __name__ == "__main__":
    # 给定一个标题, 查找这个窗口, 如果找到就放到最前
    hwnd = get_current_window()

    window_title = win32gui.GetWindowText(hwnd)
    class_name = win32gui.GetClassName(hwnd)
    window_rect = win32gui.GetWindowRect(hwnd)

    print("窗口标题:", window_title)
    print("窗口类名:", class_name)
    print("窗口位置和大小:", window_rect)

    hwndChildList = []
    win32gui.EnumChildWindows(hwnd, lambda hw, param: param.append(hw), hwndChildList)
    print("hwndChildList: ", hwndChildList)

    # 获得窗口的菜单句柄
    menuHandle = win32gui.GetMenu(hwnd)
    print("获得窗口的菜单句柄 menuHandle: ", menuHandle)

