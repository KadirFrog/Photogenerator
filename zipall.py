import zipfile, os

def zipGenerated(folder_to_zip, output_zip_filename):
    with zipfile.ZipFile(output_zip_filename, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk(folder_to_zip):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, folder_to_zip)
                zipf.write(file_path, arcname)
