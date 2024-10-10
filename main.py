import os
import shutil


def copy_matching_files(annotation_dir, data_dir, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get all text file names without extension
    annotation_files = [os.path.splitext(f)[0] for f in os.listdir(
        annotation_dir) if f.endswith('.txt')]

    # Iterate through image files and copy if there's a matching text file
    for data_file in os.listdir(data_dir):
        if data_file.endswith('.jpg'):
            data_name = os.path.splitext(data_file)[0]
            if data_name in annotation_files:
                src = os.path.join(data_dir, data_file)
                dst = os.path.join(output_dir, data_file)
                shutil.copy2(src, dst)
                print(f"Copied: {data_file}")

    print("File copying complete.")


# Usage
annotations_directory = 'annotations'
data_directory = 'data'
resolved_directory = 'resolved'

copy_matching_files(annotations_directory, data_directory, resolved_directory)
