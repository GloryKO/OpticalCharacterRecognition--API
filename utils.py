import os
import shutil

def get_filepath_from_server(uploaded_file,path='.',save_as='default'):
    file_extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path,save_as + file_extension)

    with open(temp_file,"wb") as buffer:
        shutil.copyfileobj(uploaded_file.file,buffer)
    return temp_file