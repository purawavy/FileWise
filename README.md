# FileWise
Filewise is a smart file organization tool designed specifically for students. It automatically organizes, renames, and structures academic files based on context such as subject, course, exam type, and timeline.
Filewise is a smart file organization tool built specifically for students. It automatically renames and organizes academic files based on context such as subject, file type, and usage, while giving users full control through a clear preview and undo system.

Problem

Students deal with hundreds of poorly named and disorganized files every semester including notes, assignments, slides, and PDFs. Existing file organizers are either too generic, overly technical, or unsafe to trust with important academic files.

The result is wasted time, confusion, and unnecessary stress.

Solution

Filewise introduces context-based file organization tailored for academic workflows. The tool organizes files based on how students actually use them, not just by file type, and always shows a preview before making any changes.

Features

Context-Aware Organization
Organizes files by subject and academic category such as Lectures, Assignments, Slides, and Notes.

Automatic File Renaming
Converts messy filenames into clear, readable formats.

Preview Before Apply
Shows exactly how files will be renamed and moved before execution.

One-Click Undo
Safely revert the last organization action using a history log.

Zero Configuration
No manual rules or scripts required. Works out of the box.

Project Structure
filewise/
│
├── main.py          # Entry point
├── scanner.py       # Scans files in a directory
├── organizer.py    # Renaming and organization logic
├── preview.py      # Displays changes before applying
├── undo.py         # Undo functionality
├── utils.py        # Helper functions
├── logs/
│   └── history.json
└── test_files/      # Sample files for testing

How It Works

User selects a folder containing academic files

Filewise scans and classifies files

A preview of all changes is displayed

User confirms to apply changes

Actions are logged for undo support

Installation
Requirements

Python 3.10 or higher

Git (optional)

Clone the repository
git clone https://github.com/your-username/filewise.git
cd filewise

Run the project
python main.py

Current Status

🚧 MVP in development

CLI-based interface

Student-focused use case

Manual subject input

Future versions will expand context detection and add a GUI.

Roadmap

 Improve context detection

 GUI support

 Advanced undo history

 Professional use cases

Vision

Filewise aims to become the default context-driven file organizer, starting with students and expanding into professional domains while maintaining simplicity, safety, and trust.

License

This project is currently under development. License to be added.
