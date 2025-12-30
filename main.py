print ("Hello World! I am FileWise your Demogorgon from Stanger Things! I am A CLI tool for students to manage their files.")
from scanner import scan_files
from organizer import classify_file, build_new_name
from preview import show_preview
from undo import log_action
from utils import get_safe_filename
import os
import shutil

def main():
    folder = input("Enter folder path: ").strip()
    subject = input("Enter subject name: ").strip()

    files = scan_files(folder)
    preview_data = []

    for file in files:
        category = classify_file(file["ext"])
        new_name = build_new_name(subject, category, file["name"])
        dest_dir = os.path.join(folder, subject, category)
        safe_name = get_safe_filename(dest_dir, new_name)
        dest_path = os.path.join(dest_dir, safe_name)


        preview_data.append((file["path"], dest_path))

    show_preview(preview_data)

    confirm = input("Apply changes? (y/n): ").lower()
    if confirm != "y":
        print("Operation cancelled.")
        return

    for old, new in preview_data:
        os.makedirs(os.path.dirname(new), exist_ok=True)
        shutil.move(old, new)
        log_action(old, new)

    print("Files organized successfully.")

if __name__ == "__main__":
    main()
