import os
import subprocess

def compress_pdf(input_file_path, output_file_path, power=3):
    quality = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
    }

    subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                     '-dPDFSETTINGS={}'.format(quality[power]),
                     '-dNOPAUSE', '-dQUIET', '-dBATCH',
                     '-sOutputFile={}'.format(output_file_path),
                     '{}'.format(input_file_path)]
    )

# input_dir = current directory
input_dir = '.'

# Ensure output directory exists
output_dir = os.path.join(input_dir, 'pdf_compressed')
os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    if file.endswith('.pdf'):
        compress_pdf(os.path.join(input_dir, file), os.path.join(output_dir, file))
