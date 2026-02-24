# This script moves a selected folder from one drive to another drive while keeping the file path. 
# It is designed for files synced across devices, allowing movement of large or infrequently used files outside the sync.

import os
import shutil
from PyQt6.QtWidgets import QApplication, QFileDialog
import sys

# Function to replicate all files and subdirectories from a folder
def replicate_folder(source_folder, destination_drive):
    # Walk through the folder, including all subdirectories and files
    for dirpath, dirnames, filenames in os.walk(source_folder):
        # For each file, replicate it while maintaining the folder structure
        for filename in filenames:
            source_file = os.path.join(dirpath, filename)
            replicate_file(source_file, destination_drive)

    # Delete the folder after replication
    shutil.rmtree(source_folder)
    print(f"Folder {source_folder} deleted after replication.")

# Function to replicate a single file
def replicate_file(source_file, destination_drive):
    source_drive, relative_path = os.path.splitdrive(source_file)
    destination_path = os.path.join(destination_drive, relative_path.lstrip(os.sep))
    destination_folder = os.path.dirname(destination_path)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    shutil.copy2(source_file, destination_path)
    os.remove(source_file)
    print(f"File copied from {source_file} to {destination_path} and deleted.")

# Function to handle folder picking and replication
def select_and_replicate_folders(destination_drive):
    # Use PyQt6's folder picker dialog
    app = QApplication(sys.argv)
    
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.Directory)
    
    # Set the initial directory to Z: drive
    dialog.setDirectory("Z:/")
    
    if dialog.exec():
        selected_folder = dialog.selectedFiles()[0]
        replicate_folder(selected_folder, destination_drive)

# Example usage
destination_drive = 'E:/'  # Destination drive

# Automatically replicate folders selected through the GUI
select_and_replicate_folders(destination_drive)
