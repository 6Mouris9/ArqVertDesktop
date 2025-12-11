from PIL import Image
import os


imagem = Image.open()



def make_files_directory():
    name_directory = "Converted_Archives"
    if(not os.path.exists(f"./{name_directory}")):
        os.mkdir(name_directory)
        os.chdir(f"./{name_directory}")
        
        if(not os.path.exists("PDF")):
            os.mkdir("PDF")
        if(not os.path.exists("PNG")):
            os.mkdir("PNG")
        if(not os.path.exists("JPG")):
            os.mkdir("JPG")
    else:
        os.chdir(f"./{name_directory}")
        if(not os.path.exists("PDF")):
            os.mkdir("PDF")
        if(not os.path.exists("PNG")):
            os.mkdir("PNG")
        if(not os.path.exists("JPG")):
            os.mkdir("JPG")


make_files_directory()
