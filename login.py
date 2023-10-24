import tkinter as tk
from tkinter import messagebox
import win32gui, win32con
from PIL import Image, ImageTk

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tela de Login")
        self.master.geometry("300x250")
        self.master.overrideredirect(1)  # Remove a barra de título e bordas
        self.master.attributes("-alpha", 0.9) # Transparência da janela

        # Crie um canvas para criar uma janela arredondada
        self.canvas = tk.Canvas(self.master, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Carregue a imagem de fundo personalizada (background.png)
        self.background_img = Image.open("background.png")
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)

        # Adicione widgets ao canvas
        self.lbl_title = tk.Label(self.canvas, text="Login", font=("Arial", 16))
        self.lbl_title.place(x=120, y=20)

        self.lbl_username = tk.Label(self.canvas, text="Usuário:")
        self.lbl_username.place(x=30, y=70)
        self.entry_username = tk.Entry(self.canvas)
        self.entry_username.place(x=120, y=70, width=150)

        self.lbl_password = tk.Label(self.canvas, text="Senha:")
        self.lbl_password.place(x=30, y=110)
        self.entry_password = tk.Entry(self.canvas, show="*")
        self.entry_password.place(x=120, y=110, width=150)

        self.btn_login = tk.Button(self.canvas, text="Login/Entrar", command=self.check_login)
        self.btn_login.place(x=30, y=160, width=120)

        self.btn_forgot_password = tk.Button(self.canvas, text="Esqueci a senha", command=self.forgot_password)
        self.btn_forgot_password.place(x=160, y=160, width=120)

        self.btn_close = tk.Button(self.canvas, text="Sair/Fechar", command=self.master.destroy)
        self.btn_close.place(x=30, y=200, width=250)

        # Função para mover a janela
        self.canvas.bind("<Button-1>", self.start_move)
        self.canvas.bind("<ButtonRelease-1>", self.stop_move)
        self.canvas.bind("<B1-Motion>", self.do_move)

    def check_login(self):
        if self.entry_username.get() == "admin" and self.entry_password.get() == "admin":
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.master.destroy()
            # main_menu()  # Descomente esta linha quando tiver o módulo mainMenu pronto
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    def forgot_password(self):
        messagebox.showinfo("Informação", "Entre em contato com o administrador para redefinir sua senha.")

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry("+%s+%s" % (x, y))

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)

    # Transição suave da janela
    alpha = 0.0
    while alpha < 1.0:
        root.attributes("-alpha", alpha)
        alpha += 0.01
        root.update_idletasks()
        root.update()

    root.mainloop()
