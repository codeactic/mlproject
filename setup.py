from setuptools import find_packages,setup
from typing import List

HPYEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements which are mentioned in requirements.txt
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HPYEN_E_DOT in requirements:
            requirements.remove(HPYEN_E_DOT)

    return requirements



setup(
name='mlproject',
version='0.0.1',
author='shresth',
author_email='shresthsj90@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
