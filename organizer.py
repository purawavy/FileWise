def classify_file(ext):
    if ext == ".pdf":
        return "Lectures"
    elif ext == ".docx":
        return "Assignments"
    elif ext == ".pptx":
        return "Slides"
    elif ext in [".jpg", ".png"]:
        return "Notes"
    else:
        return "Others"

def build_new_name(subject, category, original):
    return f"{subject}_{category}_{original}"
