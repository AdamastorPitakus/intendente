import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tela de Login")
        self.master.geometry("600x600")  
        self.master.overrideredirect(1)  
        self.master.attributes("-alpha", 0.9)

        self.background_img = Image.open("background.png")
        self.background_img = self.background_img.filter(ImageFilter.GaussianBlur(1))
        self.background_img = self.resize_image(self.background_img, 600, 600)
        self.background_photo = ImageTk.PhotoImage(self.background_img)

        self.canvas = tk.Canvas(self.master, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)

        self.login_frame = tk.Frame(self.canvas, bd=1, relief=tk.SOLID, bg='#f5f5f5')  # Using a light color for the frame
        self.login_frame.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.4, anchor='center')

        #tudo centralizado na tela
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

                # configura o peso das colunas e linhas
        self.login_frame.grid_columnconfigure(0, weight=1)
        self.login_frame.grid_columnconfigure(1, weight=2)  # Dando um peso maior para a coluna 1
        self.login_frame.grid_rowconfigure(0, weight=1)
        self.login_frame.grid_rowconfigure(1, weight=1)
        self.login_frame.grid_rowconfigure(2, weight=1)
        self.login_frame.grid_rowconfigure(3, weight=1)
        self.login_frame.grid_rowconfigure(4, weight=1)

        self.lbl_title = tk.Label(self.login_frame, text="Login", font=("Arial", 16), bg='#f5f5f5')
        self.lbl_title.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        self.lbl_username = tk.Label(self.login_frame, text="Usuário:", bg='#f5f5f5')
        self.lbl_username.grid(row=1, column=0, sticky=tk.W, padx=(10, 5))
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=1, column=1, padx=(5, 10), sticky=tk.EW)

        self.lbl_password = tk.Label(self.login_frame, text="Senha:", bg='#f5f5f5')
        self.lbl_password.grid(row=2, column=0, sticky=tk.W, padx=(10, 5))
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=2, column=1, padx=(5, 10), sticky=tk.EW)

        self.btn_login = tk.Button(self.login_frame, text="Login/Entrar", command=self.check_login)
        self.btn_login.grid(row=3, column=0, padx=10, pady=(20, 10), sticky=tk.W)

        self.btn_forgot_password = tk.Button(self.login_frame, text="Esqueci a senha", command=self.forgot_password)
        self.btn_forgot_password.grid(row=3, column=1, padx=10, pady=(20, 10), sticky=tk.E)

        desired_width_ratio = 0.3 # 70% of the screen width
        login_frame_width_ratio = 0.6 # 60% of the login frame width
        canvas_width = 600 # The width of the canvas
        default_button_width = 100 # The default width of the buttons

        ipadx_value = (desired_width_ratio * login_frame_width_ratio * canvas_width - default_button_width) / 2

        self.btn_close = tk.Button(self.login_frame, text="Sair/Fechar", command=self.master.destroy)
        self.btn_close.grid(row=4, column=0, columnspan=2, pady=20, sticky=tk.EW, ipadx=ipadx_value)

        self.canvas.bind("<Button-1>", self.start_move)
        self.canvas.bind("<ButtonRelease-1>", self.stop_move)
        self.canvas.bind("<B1-Motion>", self.do_move)

    def check_login(self):
        if self.entry_username.get() == "admin" and self.entry_password.get() == "admin":
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.master.destroy()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    def forgot_password(self):
        messagebox.showinfo("Informação", "Entre em contato com o administrador para redefinir sua senha.")

    def resize_image(self, image, width, height):
        return image.resize((width, height))

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

    alpha = 0.0
    while alpha < 1.0:
        root.attributes("-alpha", alpha)
        alpha += 0.01
        root.update_idletasks()
        root.update()

    root.mainloop()
