import tkinter as tk
from tkinter import ttk

class ModernWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # 设置窗口样式
        self.style = ttk.Style(self)
        self.style.configure('TButton', foreground='#ABCDEF', background='#ABCDEF', borderwidth=0, relief='flat')
        self.style.configure('TLabel')
        self.configure(bg="#edf3dd")
        self.title('Free VPN')

        # 创建并布局控件
        self.label = ttk.Label(self, text='点击下列按钮以获得订阅')
        self.label.pack(pady=20)
        
        self.button_vmess = ttk.Button(self, text='vmess', command=self.vmess)
        self.button_vmess.pack(pady=10)

        self.button_socketrocket = ttk.Button(self, text='socketrocket', command=self.socketrocket)
        self.button_socketrocket.pack(pady=10)
        
    def vmess(self):
        self.label.configure(text='vmess按钮已点击！')
        
    def socketrocket(self):
        self.label.configure(text='socketrocket按钮已点击！')

window = ModernWindow()
window.mainloop()