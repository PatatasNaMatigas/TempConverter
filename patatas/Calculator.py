import tkinter as tk
from tkinter import font
import ctypes

class Calculator:

    userInterfaceUtils = None
    mainWindow = None

    def __init__(self):
        print("Calculator Initiated")

    def start(self):
        if self.mainWindow is None:
            self.userInterfaceUtils = UserInterfaceUtils()
            self.userInterfaceUtils.initFont()
            self.mainWindow = MainWindow(calculator)
            print(font.families())
            self.mainWindow.start()

class UserInterfaceUtils:

    def initFont(self):
        FR_PRIVATE = 0x10
        FR_NOT_ENUM = 0x20

        ctypes.windll.gdi32.AddFontResourceExW("res/fonts/Mono.ttf", FR_PRIVATE, 0)

class MainWindow:

    calculator = None
    window = None

    # components
    tempInput = None
    fromUnitInput = None
    toUnitInput = None

    def __init__(self, calculator):
        self.calculator = calculator
        window = tk.Tk()
        window.title("TempConvert Pro Max")
        window.config(
            background = "#A57EFF"
        )
        window.geometry("300x210")
        self.window = window

    def initComponents(self):
        tempInput = tk.Entry(
            self.window,
            bg = self.window["bg"],
            fg = "#FFFFFF",
            font = ("VCR OSD Mono", 9),
            bd = 1,
            highlightthickness = 1,
        )
        tempInput.place(
            x = 30,
            y = 40,
            w = 150,
            h = 20
        )
        self.tempInput = tempInput

    def getWindow(self):
        return self.window

    def start(self):
        self.initComponents()
        self.window.mainloop()

calculator = Calculator()
calculator.start()