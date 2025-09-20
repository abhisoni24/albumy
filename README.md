# Albumy

*Capture and share every wonderful moment.*

![Screenshot](https://helloflask.com/screenshots/albumy.png)

## Installation

clone:
```
$ git clone https://github.com/abhisoni24/albumy.git
$ cd albumy
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```
generate fake data then run:
```
$ flask forge #this generates fake data
$ flask run
* Running on http://127.0.0.1:5000/
```
Test account:
* email: `admin@helloflask.com`
* password: `helloflask`


Optionally, I haved added a script to import some cool pictures from the repository of "yavuzceliker". The script is called getRandomImage.py and saved the random pictures in the uploads folder by the existing named and thus overrides the bland one-color background images.

## Setup API for Objection Detection in Pictures and Tag Generation
Setting up an Azure Computer Vision Resource as a Student Account
1.	Go to Azure for Students and sign up with your school email: https://azure.microsoft.com/en-us/free/students
2.	Once signed up, go to the Azure Portal.
3.	Click “Create a resource” and search for “Computer Vision”.
4.	Click “Create”, fill in the required details, and create a new resource group if needed.
5.	If you are using the student account, the default policy allows the creation of resources in specific regions only. For UIC Students, this is the list of allowed regions:
West US 2, East US 2, West US 3, North Central US, Canada Central
6.	After deployment, go to your Computer Vision resource.
7.	In the left sidebar, click “Keys and Endpoint”.
8.	Copy one of the keys and the endpoint URL.
9. Lastly, paste the respective items in .flaskenv file that you should create by removing the ".example" from the ".flaskenv.example" file.
10. Re-run the flask server and you should be good to go.

Alternately, you can use any local instances of a vision model or any other vision model APIs. All you need are the authentication keys and the endpoint. The setup configuration will be slightly different for them, but very trivial. Any LLM model can help you make the changes.

## Demo of ML Functions

1. If you open a picture in a full window, and it doesn't have alt text and/or tags already, then before loading the reosurces the application calls the Azure visoin API and processes those info for you, and finally loads the page with everything.
2. The search also utilizes the tags in the picture as the ML-emabled search feature.


## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
