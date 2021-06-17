import tkinter as tk
from PIL import Image, ImageTk

class Page01(tk.Frame) :

	def __init__(self, parent, Game):

		self.game = Game
		self.config = Game.config

		#CONFIG FRAME
		super().__init__(parent)
		self.configure(bg="black")
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.main_frame = tk.Frame(self, height=self.config.side, width=self.config.side, bg="black")
		self.main_frame.pack(expand=True)

		self.battleship_label = tk.Label(self.main_frame, text="BattleShip", font=("Jokerman", 40), bg="Black", fg="Lavender")
		self.battleship_label.pack(pady=2)

		self.version_label = tk.Label(self.main_frame, text="Team Version", font=("Jokerman", 22), bg="Black", fg="Lavender")
		self.version_label.pack(pady=2)

		frame_w = self.config.side

		image = Image.open(self.config.init_img)
		i_w, i_h = image.size
		ratio = i_w/frame_w
		new_size = (int(i_w/ratio/3),int(i_h/ratio/3))
		image = image.resize(new_size)
		self.logo = ImageTk.PhotoImage(image)

		self.logo = ImageTk.PhotoImage(image)
		self.label_logo = tk.Label(self.main_frame, image=self.logo)
		self.label_logo.pack(pady=10)

		self.username_label = tk.Label(self.main_frame, text="Username : ", font=("Arial", 17, "bold"), bg="black", fg="lavender")
		self.username_label.pack(pady=3)

		self.var_username = tk.StringVar()
		self.input_username = tk.Entry(self.main_frame, font=("Comic Sans MS", 15),  textvariable=self.var_username)
		self.input_username.pack(pady=20)

		self.btn_start = tk.Button(self.main_frame, text="START", font=("Arial", 18, "bold"), command=lambda:self.game.window.auth_login(), bd=2)
		self.btn_start.pack(pady=5)