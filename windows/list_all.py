import win32gui


# def callback(hwnd, extra):
#     if win32gui.IsWindowVisible(hwnd):
#         print(f"window text: '{win32gui.GetWindowText(hwnd)}'")
#
# win32gui.EnumWindows(callback, None)

def find_window_by_title(title):
    try:
        return win32gui.FindWindow(None, title)
    except Exception as ex:
        print('error calling win32gui.FindWindow ' + str(ex))
        return -1


def callback(hw_child, extra):
    print(f"window text: '{win32gui.GetWindowText(hw_child)}'")


hwnd = find_window_by_title('微信')
win32gui.EnumChildWindows(hwnd, callback, None)
# hwndChildList = []
# print("hwndChildList: ", hwndChildList)
