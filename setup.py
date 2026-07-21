from setuptools import find_packages, setup
from typing import List
#typing lib provides special types that describe what kind of data
# your variables, functions, and classes are expected to use.It is like a lable marker

''' like list here say's -This variable should contain a list of integers.
integer_list: List[int] = [1, 2, 3, 4, 5] If it would be list[str]
Then it should contain a list of strings.'''
HYPEN_E_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
    '''
    This function will take variable file_path as argument of string type 
    and return a list of requirements as string type.
    The -> symbol in Python is called the return type annotation.
    It tells readers (and tools like VS Code) what type of value a function is expected to return.
    '''
    requirements = []
    with open(file_path) as file_obj:  
        # The open() function is used to open a file so that Python can work with it.
        #Here with is imp as with (with )the file 
        #will be automatically closed after the block of code is executed.
        #and with out with we  will code like this
        # open(file_path)=file_obj
        # file_obj.close()
        # Also we can use the methods on objects not the varables
        
        requirements = file_obj.readlines()
        #use readlines() method to read all the lines of a file 
        requirements = [req.replace("\n","") for req in requirements]
        #As in requirements.txt file we are writting the lib names on next line 
        #.readlines() method will read it as "li_name\n" so we don't want \n
        #so we replace \n with "" using rwplace() method and we are using list comprehension
        # mean using for loop in one line and  tem_variable req is used to store each line
        # of the file in the list comprehension.
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            #if -e . is present in the requirements list then we remove it from the list
            #by this we can install the the project to package 
            #just by using command install -r requirements.txt instead of using 
            #python setup.py install command to install the project to package.
    return requirements

setup(
    name='DS_Project',
    version='0.0.1',
    author='Digvijay',
    author_email='digvijayppa@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
        