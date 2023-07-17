import os
import subprocess
import traceback

def compress_pdf(input_file_path, output_file_path, power=3):
    quality = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
    }

    try:
        subprocess.check_call(['gswin64c.exe', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                                '-dPDFSETTINGS={}'.format(quality[power]),
                                '-dNOPAUSE', '-dBATCH', '-dQUIET', '-sOutputFile={}'.format(output_file_path),
                                input_file_path]
        )
        # If the compression is successful, delete the original file
        os.remove(input_file_path)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while compressing {input_file_path}")
        print(f"Return code: {e.returncode}")
        print(f"Output: {e.output}")
    except Exception as e:
        print(f"An unexpected error occurred while compressing {input_file_path}")
        print(traceback.format_exc())

def walk_and_compress(path='.'):
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if file.endswith('.pdf'):
                file_path = os.path.join(dirpath, file)
                output_file_path = os.path.join(dirpath, os.path.splitext(file)[0] + '_compressed.pdf')
                compress_pdf(file_path, output_file_path)

walk_and_compress()  # Call function with directory path
