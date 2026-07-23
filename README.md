# First data sience project

# 1st
'Never add venv file in repo'
# 2nd
Create a '.gitignore' file -the file which is made to store the info of files which we don't want to commit 
# 3rd
In VS Code, the venv folder appeared green because it was an untracked file/folder.after adding gitigore-"Ignore the venv folder. Pretend it doesn't exist.
# 4th
we add requierments.txt file where we add the name of libilary which we want to install and use in project  also these are the latest version  are installed even if we don't mension and we mension  the version with == operator and adding this file we use command-pip install -requierments.txt.This packages will ne installed in venv 

### Issue
I face the problem that when i was trying to import fin_packages,setup from setuptools it showed a yellow line below setuptools .i had my venv activated but it was that which i was using in this project also the i didn't select the interpreter
so i use this command to  find exact interpreter path that I should select in VS Code.
command-python -c "import sys; print(sys.executable)"
Step2-crl+shift+p
step3-select interpreter
step4-select enter interpreter path
step5-select find
step6-select path which came oyt of the earier command

## 5th 
Create struture of project with automated code in template.py or using cookiecutter

