# Rename images in bulk
import os
# Mention image folder full path

folder_path = "D:/Python/Senior/number"

files = os.listdir(folder_path)

# Rename images with serial number. Keeping the format (png, jpeg, jpg, etc.) same

for index, file in enumerate(files):

    os.rename(os.path.join(folder_path, file), os.path.join(folder_path, ''.join([str(index), '.', file.split('.')[-1]])))