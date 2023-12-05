import os

def rename_files(source_folder, prefix):
    """Rename all files in the source folder with a prefix and a 6-digit count."""
    count = 1
    total = len(os.listdir(source_folder))
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            # Construct new file name
            extension = os.path.splitext(filename)[1]
            new_filename = f"{prefix}{str(count).zfill(6)}{extension}"
            new_file_path = os.path.join(source_folder, new_filename)

            # Rename the file
            os.rename(file_path, new_file_path)
            count += 1
            print(f"Renamed {new_file_path}")

# Example usage
source_folder = '/Users/cho/Downloads/Fire/4. Renamed/nonfire'
prefix = 'NONFIRE_'
rename_files(source_folder, prefix)
