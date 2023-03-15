from setuptools import find_packages,setup
from typing import List

hypen_e = '-e .'



def get_requrirements(file_path:str)->List[str]:
    
    requriemnts = []
    with open(file_path) as file_obj:
        requriemnts = file_obj.readlines()
        requriemnts = [req.replace("\n", " ") for req in requriemnts]
        
        if hypen_e in requriemnts:
            requriemnts.remove(hypen_e)
    return requriemnts

setup(
    name = 'ML_Project',
    version='0.0.1',
    author = 'nan',
    author_email= 'nan',
    packages=find_packages(),
    install_requires = get_requrirements('requirement.txt')
)