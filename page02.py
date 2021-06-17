import tkinter as tk
from PIL import Image, ImageTk

class Page02(tk.Frame) :

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

		self.win_label = tk.Label(self.main_frame, text="You Win !!!", font=("MV Boli", 40, "bold"), bg="black", fg="white")
		self.win_label.pack(pady=5)

		frame_w = self.config.side

		image = Image.open(self.config.win_img)
		i_w, i_h = image.size
		ratio = i_w/frame_w
		new_size = (int(i_w/ratio/4),int(i_h/ratio/4))
		image = image.resize(new_size)
		self.logo = ImageTk.PhotoImage(image)

		self.logo = ImageTk.PhotoImage(image)
		self.label_logo = tk.Label(self.main_frame, image=self.logo)
		self.label_logo.pack(pady=5)

		self.next_level_btn = tk.Button(self.main_frame, text="NEXT LEVEL", font=("Arial", 15, "bold"), command=lambda:self.game.next_level_game(), bd=2)
		self.next_level_btn.pack(pady=4)

		self.replay_btn = tk.Button(self.main_frame, text="REPLAY", font=("Arial", 15, "bold"), command=lambda:self.game.replay_game(), bd=2) 
		self.replay_btn.pack(pady=4)

		self.preview_btn = tk.Button(self.main_frame, text="PREVIEW", font=("Arial",15, "bold"), command=lambda:self.game.preview_game(), bd=2) 
		self.preview_btn.pack(pady=4)

		self.main_menu_btn = tk.Button(self.main_frame, text="MAIN MENU", font=("Arial", 15, "bold"), command=lambda:self.game.main_menu_game(), bd=2)
		self.main_menu_btn.pack(pady=4)

		self.quit_game_btn = tk.Button(self.main_frame, text="CLOSE", font=("Arial", 15, "bold"), command=lambda:self.game.close_game(), bd=2)
		self.quit_game_btn.pack(pady=4)

