#First data sience project 
1.Never all venv file in repo
2.Create a gitignore file -the file which is made to store the info of files which we don't want to commit 
3.In VS Code, the venv folder appeared green because it was an untracked file/folder.after adding gitigore-"Ignore the venv folder. Pretend it doesn't exist.
4.we add requierments.txt file where we add the name of libilary which we want to install and use in project  also these are the latest version  are installed even if we don't mension and we mension  the version with == operator and adding this file we use command-pip install -requierments.txt.This packages will ne installed in venv 
# Why do we use `setup.py` in a Data Science / Machine Learning Project?
`setup.py` is used to package the project as a Python package. It makes the project organized, reusable, and easier to maintain.
## Why is it needed?
Without `setup.py`, Python may not recognize your project's modules, and you may need to manually modify the Python path using `sys.path`.
With `setup.py`, the project can be installed locally using:
```bash
pip install -e .
```
After installation, Python can directly import modules from the project without modifying the path.
Example:
```python
from src.data_ingestion import DataIngestion
```
instead of:
```python
import sys
sys.path.append("src")
from data_ingestion import DataIngestion
```
## Advantages of using `setup.py`

- Packages the project as a Python package.
- Allows clean and simple imports.
- Eliminates the need to manually modify the Python path.
- Makes the code reusable across multiple projects.
- Helps maintain a standard project structure.
- Makes collaboration easier because other developers can install the project with a single command.
- Editable installation (`pip install -e .`) automatically reflects code changes without reinstalling the package.
## Conclusion
`setup.py` is used to convert a Data Science project into a reusable Python package. It provides a standard project structure, simplifies module imports, and allows the project to be installed in editable mode using `pip install -e .`, making development and collaboration much easier.
##To get more information about setup.py go and search python setup.py and check the first site of python packaging 
### Issue
I face the problem that when i was trying to import fin_packages,setup from setuptools it showed a yellow line below setuptools .i had my venv activated but it was that which i was using in this project also the i didn't select the interpreter
so i use this command to  find exact interpreter path that I should select in VS Code.
command-python -c "import sys; print(sys.executable)"
Step2-crl+shift+p
step3-select interpreter
step4-select enter interpreter path
step5-select find
step6-select path which came oyt of the earier command
