# This script moves a selected file from one drive to another drive while keeping the file path. 
# It was meant for files that are synced on devices, allowing movement of large or infrequently used files outside the sync.

import os
import shutil
from PyQt5.QtWidgets import QApplication, QFileDialog
import sys

# Function to replicate a single file to the new drive, keeping folder structure
def replicate_file(source_file, destination_drive):
    # Get the relative path of the file from the source drive
    source_drive, relative_path = os.path.splitdrive(source_file)
    
    # Construct the destination path by replacing the drive letter
    destination_path = os.path.join(destination_drive, relative_path.lstrip(os.sep))
    
    # Extract the folder structure of the destination path
    destination_folder = os.path.dirname(destination_path)
    
    # Create the folder structure in the destination if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Copy the file from source to destination
    shutil.copy2(source_file, destination_path)
    
    print(f"File copied from {source_file} to {destination_path}")
    
    # Delete the original file after copying
    os.remove(source_file)
    print(f"File {source_file} deleted after replication.")

# Function to handle file picking and replication
def select_and_replicate_files(destination_drive):
    # Use PyQt5's file picker dialog for selecting files
    app = QApplication(sys.argv)
    
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.ExistingFiles)
    
    # Set the initial directory to Z: drive
    dialog.setDirectory("Z:/")
    
    if dialog.exec_():
        selected_files = dialog.selectedFiles()
        
        for file in selected_files:
            replicate_file(file, destination_drive)

# Example usage
destination_drive = 'E:/'  # Destination drive

# Automatically replicate files selected through the GUI
select_and_replicate_files(destination_drive)
