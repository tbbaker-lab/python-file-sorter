from pathlib import path
import shutil

fol = path("test_files")

file_types = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "audio": [".mp3", ".wav", ".aac"],
    "videos": [".mp4", ".avi", ".mkv"],
    "archives": [".zip", ".rar", ".tar", ".gz"],
    "others": []
}

for file in fol.iterdir():
    if file.is_dir():
        continue

extension = file.suffix.lower()

folder_name = file_types.get(extension, "others")

new_folder = fol / folder_name
new_folder.mkdir(exist_ok=True)

shutil.move(str(file), str(new_folder / file.name))

print(f"Moved {file.name} to {folder_name}")