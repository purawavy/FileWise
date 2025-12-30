from pathlib import Path

def scan_files(folder):
    files = []
    for item in Path(folder).iterdir():
        if item.is_file():
            files.append({
                "name": item.name,
                "ext": item.suffix.lower(),
                "path": str(item)
            })
    return files
