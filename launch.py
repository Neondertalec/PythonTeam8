import enum, os, msvcrt

class Color(enum.Enum):
	end    = '\33[0m'
	gray   = '\33[90m'
	red    = '\33[91m'
	green  = '\33[92m'
	yellow = '\33[93m'
	blue   = '\33[94m'
	violet = '\33[95m'
	beige  = '\33[96m'
	white  = '\33[97m'
	hilight  = '\33[45m'
	def __get__(self, instance, owner):
		return self.value

root_dir = os.path.dirname(__file__)
current_dir = root_dir
dir_folders = []
dir_files = []
selection = 0

def goto_dir(dir):
	global current_dir, dir_folders, dir_files, selection

	current_dir = dir
	dir_folders = []
	dir_files = []
	selection = 0

	if root_dir != current_dir:
		dir_folders.append('..')

	for file in os.listdir(current_dir):
		if file[0] == '.' or os.path.join(root_dir, file) == __file__: continue

		if os.path.isdir(os.path.join(root_dir, file)):
			dir_folders.append(file)
		else:
			dir_files.append(file)

def print_dir():
	os.system('cls||clear')
	print(f"{Color.yellow}{current_dir}{Color.end}")

	i = 0
	files = [*dir_folders, *dir_files]
	folders_len = len(dir_folders)

	for i in range(0, len(files)):
		print(f"{Color.hilight if selection == i else ''}{Color.green if i < folders_len else Color.blue}{files[i]}{Color.end}")

def select_option():
	if selection < len(dir_folders):
		if dir_folders[selection] == '..':
			goto_dir(os.path.dirname(current_dir))
		else:
			goto_dir(os.path.join(current_dir, dir_folders[selection]))
	else:
		os.system('cls||clear')
		try:
			exec(open(os.path.join(current_dir, dir_files[selection - len(dir_folders)])).read())
		except:
			print(f"{Color.red}An error occured!{Color.end}")
		input(f"{Color.red}Press any key to return{Color.end}")
	print_dir()

def slide_option(dir = 1):
	global selection

	selection += dir
	length = len(dir_folders) + len(dir_files)
	if selection < 0:
		selection = length-1
	elif selection >= length:
		selection = 0
		
goto_dir(current_dir)
print_dir()

while True:
	key = msvcrt.getch()
	# print(key)
	if key == b'\x1b':# Esc
		break
	if key == b'\x03':# Ctrl + C
		break

	if key == b'\r':# Enter
		select_option()

	if key == b'\x00':# Special stuff
		key = msvcrt.getch()
		# print("s " + str(key))
		if key == b'H':#arrow up
			slide_option(-1)
			print_dir()
		elif key == b'P':#arrow down
			slide_option(1)
			print_dir()
		# elif key == b'K':#arrow left
		# 	pass
		# elif key == b'M':#arrow rigth
		# 	pass