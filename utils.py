import os

def get_safe_filename(folder, filename):
    """
    Prevents overwriting files by appending numbers if needed.
    """
    name, ext = os.path.splitext(filename)
    counter = 1
    safe_name = filename

    while os.path.exists(os.path.join(folder, safe_name)):
        safe_name = f"{name}_{counter}{ext}"
        counter += 1

    return safe_name
