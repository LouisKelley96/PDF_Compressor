# PDF_Compressor
Compress PDfs must install ghost script first:

https://www.ghostscript.com/releases/gsdnld.html


pdf_comp.py
This script will compress all PDF files in the current directory. It will create a new directory named pdf_compressed where it will store the compressed files. The original files will remain unchanged.

pdf_comp_all.py
This script will traverse all subdirectories starting from the current directory, find all PDF files, and compress them. The compressed file will be named filename_compressed.pdf and will be placed in the same directory as the original file. The original file will not be affected.

compress_remove.py
This script also traverses all subdirectories starting from the current directory, and it compresses all PDF files it finds. However, unlike pdf_comp_all.py, it will remove the original file after compression is successful. The compressed file will be named filename_compressed.pdf and will be placed in the same directory as the original file.

Please note that due to the nature of compress_remove.py, it's strongly recommended to create a backup of your PDF files before using it, as it removes the original files after compression.
