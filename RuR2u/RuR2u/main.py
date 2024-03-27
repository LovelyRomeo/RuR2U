import os

path = 'RuR2u/WebAppsru/'

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


create_folder(path + '/image')

media_url = os.path.join(path, 'image')



