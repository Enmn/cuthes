import zipfile
from io import BytesIO
import os
import shutil
import time
import requests

def close():
    os.system('cls' if os.name == 'nt' else 'clear')



def checker_update():
    version = open(".version", "r").read().strip()
    response = requests.get('https://raw.githubusercontent.com/Enmn/cuthes/main/.version').text.strip()
    new_version = response
    if new_version != version:
        return True
    else:
        return False
    
    

def update():
    if checker_update() == True:
        zip_url = 'https://github.com//Enmn/cuthes/archive/master.zip'
        dir_name = 'cuthes-main'
        close()
        print('There is a new version that will be updated soon...')
        time.sleep(5)
        print("Fetching the update url...")
        time.sleep(1)
        print("Updating... ")
        response = requests.get(zip_url)
        if response.status_code == 200:
            zip_content = response.content
            with zipfile.ZipFile(BytesIO(zip_content)) as zip_file:
                for member in zip_file.namelist():
                    filename = os.path.split(member)
                    if not filename[1]:
                        continue
                    new_filename = os.path.join(
                        filename[0].replace(dir_name, "."),
                        filename[1])
                    filename = new_filename
                    os.makedirs(os.path.dirname(filename), exist_ok=True)
                    source = zip_file.open(member)
                    target = open(new_filename, "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)
            file = open('.version', 'r').read()
            print('Cuthes update completed')
            time.sleep(1)
            print(f'Updated to the new version: {file} !')
            print('\tUpdated, please turn it on again')