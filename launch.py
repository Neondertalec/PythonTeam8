import enum, os, msvcrt, sys

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
display_skip_count = len(os.path.dirname(root_dir)) + 1
current_dir = root_dir
dir_folders = []
dir_files = []
selection = [0]

def goto_dir(dir):
	global current_dir, dir_folders, dir_files, selection

	current_dir = dir
	dir_folders = []
	dir_files = []

	if root_dir != current_dir:
		dir_folders.append('..')

	for file in os.listdir(current_dir):
		if file[0] == '.' or os.path.join(root_dir, file) == __file__: continue

		if os.path.isdir(os.path.join(root_dir, file)):
			dir_folders.append(file)
		else:
			dir_files.append(file)

def print_dir():
	print("\033[?25l\033[2J\033[H", end="")

	files = [*dir_folders, *dir_files]
	folders_len = len(dir_folders)

	hover_action = "open folder" if selection[-1] < len(dir_folders) else "run python task"
	strss = []
	strss.append(f"{Color.violet}[{selection[-1]+1}/{len(files)}] {Color.yellow}[Path: {current_dir[display_skip_count:]}] {Color.gray}[{hover_action}]{Color.end}")

	for i in range(0, len(files)):
		strss.append(f"{Color.hilight if selection[-1] == i else ''}{Color.green if i < folders_len else Color.blue}{files[i]}{Color.end}")

	print("\n".join(strss))

def select_option():
	if selection[-1] < len(dir_folders):
		if dir_folders[selection[-1]] == '..':
			goto_dir(os.path.dirname(current_dir))
			selection.pop()
		else:
			goto_dir(os.path.join(current_dir, dir_folders[selection[-1]]))
			selection.append(0)
	else:
		os.system('cls||clear')
		print("\033[?25h")
		try:
			os.system(sys.executable + ' ' + os.path.join(current_dir, dir_files[selection[-1] - len(dir_folders)]))
			# exec(open(os.path.join(current_dir, dir_files[selection[-1] - len(dir_folders)])).read())
		except:
			print(f"{Color.red}An error occured!{Color.end}")
		input(f"{Color.red}Press any key to return{Color.end}")
		os.system('cls||clear')

	print_dir()

def slide_option(dir = 1):
	global selection

	selection[-1] += dir
	length = len(dir_folders) + len(dir_files)
	if selection[-1] < 0:
		selection[-1] = length-1
	elif selection[-1] >= length:
		selection[-1] = 0
		
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