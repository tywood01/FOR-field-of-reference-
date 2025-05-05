"""
    kam/script.py
    
    -Authors: Tytus Woodburn
    -Emails: tytus.woodburn@student.cune.edu
    -Date: 05-05-2025
"""
import os

# Define the directory containing the images
appimages_dir = "/home/twoodburn/finalproject/kam/static/images/appimages/ios"

# Base path for static files
static_base_path = "/static/images/appimages/ios/"

# Get all filenames in the directory
try:
    filenames = os.listdir(appimages_dir)
    files_to_cache = [
        f"{static_base_path}{filename}"
        for filename in filenames
        if os.path.isfile(os.path.join(appimages_dir, filename))
    ]

    # Print the filesToCache array for use in serviceworker.js
    print("const filesToCache = [")
    for file in files_to_cache:
        print(f"    '{file}',")
    print("];")
except FileNotFoundError:
    print(f"Directory not found: {appimages_dir}")
except Exception as e:
    print(f"An error occurred: {e}")
