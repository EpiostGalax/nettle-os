import ctypes
WALLPAPER_PATH = "wallpaperofnettle.png"
ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)
