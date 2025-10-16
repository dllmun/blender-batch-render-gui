import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox


root = tk.Tk()

root.title("BLENDER BATCH RENDER GUI")
root.resizable(False, False)
root.geometry("640x480")


try:
    file = open("current_blender_version_folder.txt")
    _blender_version_directory = file.read()
    file.close()
except:
    file = open("current_blender_version_folder.txt", "x")
    file.close()
    _blender_version_directory = ""

_blender_version_directory_label = tk.Label(root, text="CURRENT BLENDER VERSION FOLDER:\n" + _blender_version_directory)
_blender_version_directory_label.pack(pady=(5, 0))


def _on_blender_version_button_pressed():
    _blender_version_directory = fd.askdirectory(
        title='SELECT BLENDER VERSION FOLDER',
        initialdir='\Program Files\Blender Foundation',
    )
    try:
        file = open("current_blender_version_folder.txt", "w")
        file.write(_blender_version_directory)
        file.close()
    except:
        pass
    
    _blender_version_directory_label.config(text="CURRENT BLENDER VERSION FOLDER:\n" + _blender_version_directory)

_select_blender_version_button = tk.Button(root, text=">>  SELECT BLENDER VERSION FOLDER  <<", command=_on_blender_version_button_pressed)
_select_blender_version_button.pack(pady=(0, 15))


_label = tk.Label(root, text='SELECTED BLEND FILES TO RENDER:')
_label.pack(pady=0, side=tk.TOP, fill=tk.X)

_listbox = tk.Listbox(root, selectmode=tk.EXTENDED)
_listbox.pack(padx=10, pady=(5, 5), expand=True, fill=tk.BOTH)

def select_files():
    _filetypes = (
        ('Blender files ( *.blend )', '*.blend'),
        ('All files ( *.* )', '*.*')
    )

    _filenames = fd.askopenfilenames(
        title='SELECT BLEND FILES TO RENDER',
        filetypes=_filetypes)
    
    return _filenames

def _on_add_blend_files_pressed():
    _blend_files = select_files()
    for blend_file in _blend_files:
        _listbox.insert(_listbox.size(), blend_file)

_add_blend_files_button = tk.Button(root, text="( + )  ADD BLEND FILES", command=_on_add_blend_files_pressed)
_add_blend_files_button.pack(pady=(0, 10), padx=(5, 10), side=tk.RIGHT)


def _on_remove_blend_files_pressed():
    _selection = _listbox.curselection()
    if len(_selection) > 0:
        _listbox.delete(min(_selection))
        _on_remove_blend_files_pressed()

_remove_blend_files_button = tk.Button(root, text="( - )  REMOVE BLEND FILES", command=_on_remove_blend_files_pressed)
_remove_blend_files_button .pack(pady=(0, 10), padx=0, side=tk.RIGHT)


_close_cmd_check_var = tk.IntVar()
def _on_export_bat_file_pressed():
    _export_directory = fd.askdirectory(
        title='SELECT EXPORT LOCATION',
    )
    try:
        file = open(_export_directory + "/blender_batch_render.bat", "w")
        
        file.write('cd "' + _blender_version_directory_label.cget("text").replace("CURRENT BLENDER VERSION FOLDER:\n", "") + '"\n')
        
        for i in range(0, _listbox.size()):
            file.write('blender -b "' + _listbox.get(i) + '" -a\n')
            
        if _close_cmd_check_var.get() == 0:
            file.write("cmd /k")
            
        file.close()
    except:
        messagebox.showerror("Error", "Program failed to export .bat file.")

_export_bat_file_button = tk.Button(root, text="<<  EXPORT BAT FILE", command=_on_export_bat_file_pressed)
_export_bat_file_button.pack(pady=(0, 10), padx=(10, 1), side=tk.LEFT)


_close_cmd_checkbutton = tk.Checkbutton(root, text="Close cmd window when done?", variable=_close_cmd_check_var, onvalue=1, offvalue=0,)
_close_cmd_checkbutton.pack(pady=(0, 10), padx=0, side=tk.LEFT)


root.mainloop()