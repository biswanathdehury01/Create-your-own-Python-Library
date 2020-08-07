Creating a library

This is a simple calculator that takes 2 inputs as either add, sub, mul or div them.


Steps Involved:

1. Create a folder Calculator
2. Have a __init__.py file inside Calulator and your logic.
3. have a README.txt file with your description.
4. Then have CHANGELOG.txt
5. MANIFEST.in file. Here you will be having the OSI, MIT license from below link

https://opensource.org/licenses/MIT

6. then setup.py and change the parameters as per yours
7. Go to Command Prompt in the folder you have all

NOTE: now create a account in 

8. Run below command:

pip install setuptools twine

9. Next do ls and see all the files in it.

10. Next run below command, which will create a dist folder in you current folder

python setup.py sdist

11. Next run below command,

twine upload --repository-url https://upload.pipy.org/legacy/ dist/*

12. Then we will get a link, in pipy account.