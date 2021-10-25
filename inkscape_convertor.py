import subprocess
import os
inkscapePath = r"C:\Program Files\Inkscape\bin\inkscape.exe"

def convert(file_path, target_format):
    path_without_extension = os.path.splitext(file_path)[0]
    target_path = path_without_extension + "." + target_format
    #https://stackoverflow.com/questions/35367550/convert-svg-pdf-to-emf
    subprocess.run([inkscapePath, file_path, '--export-filename', target_path])
    return target_path
    
if __name__ == "__main__":
    convert(r"F:\test\vector_barcode\out.svg","emf")