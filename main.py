import tkinter as tk
import sys

from tkinter import messagebox

import time as Time

from config import Config
from page01 import Page01
from player import Player 
from game_stat import Game_Stat
from board import Board
from ship import Ship
from page02 import Page02


class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game # battleship
		self.config = Game.config

		super().__init__()
		self.title(self.config.title)
		self.geometry(self.config.screen)

		self.create_container()

		self.pages = {}

		self.create_page02()
		self.create_board()
		self.create_page01()

		
	def change_page(self, page) :
		page = self.pages[page]
		page.tkraise()

	def auth_login(self) :
		username = self.pages['page01'].var_username.get()

		empty = ""

		if username == empty :
			info = messagebox.showinfo("Username Confirmation", "Please input USERNAME")
		else :
			self.change_page('board')

	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_page02(self) :
		self.pages["page02"] = Page02(self.container, self.game)
	
	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)

	def create_page01(self) :
		self.pages["page01"] = Page01(self.container, self.game)

class Battleship:

	def __init__(self):
		self.config = Config()
		self.player = Player()		
		self.game_stat = Game_Stat()
		self.window = Window(self)
		self.ship = Ship(self)

	def check_location(self) :
		ship = self.ship.location 
		player = self.player.location
		if ship == player :
			return True
		return False

	def window_button_clicked(self, pos_x, pos_y):
		#print(pos_x, pos_y)
		self.player.current_location(pos_x, pos_y)
		win = self.check_location()
		self.window.pages['board'].change_image_btn(pos_x, pos_y, win)
		if win :
			Time.sleep(1)
			self.window.change_page("page02")

	def run(self):
		self.window.mainloop()

	def main_menu_game(self) :
		self.game_stat.level = 1
		self.config.row = 5
		self.config.column = 5

		self.ship.setup_Location()
		self.window.create_board()
		self.window.change_page("page01")

	def next_level_game(self) :
		self.game_stat.level += 1
		self.config.row += 1
		self.config.column += 1

		self.ship.setup_Location()
		self.window.create_board()
		self.window.change_page("board")

	def preview_game(self) :
		self.window.change_page("board")

	def replay_game(self) :
		self.ship.setup_Location()
		self.window.create_board()
		self.window.change_page("board")

	def close_game(self) :
		sys.exit()

if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()