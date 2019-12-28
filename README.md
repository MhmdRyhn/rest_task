# rest_task



## Steps to Setup and Run The Project
:heavy_check_mark: This project has been developed using **Python 3.5** on **Linux** <br>
:heavy_check_mark: It is assumed that **Python >= 3.5** is installed in your system. And you are using debian distribution of **Linux**. Now, follow the below steps:
- [Setup Redis Server](#setup-redis-server)
- [Clone the Repository](#clone-the-repository)
- [Setup Virtual Environment and Install Required Packages](#setup-virtual-environment-and-install-required-packages)
- [Start Django Server](#start-django-server)
- [Send Request Using Postman](#send-request-using-postman)



### Setup Redis Server
**\*\*\*** If **Redis** is already installed in your system, then skip this step, but make sure **Redis is running on your system**.

At first install **Redis** server using following commands:
```
sudo apt-get update
sudo apt-get install redis-server
```
After installation of the **redis server**, make sure the redis server is running. To check status:
```
sudo systemctl status redis
```
If it is not running, then start it using following command:
```
sudo systemctl start redis
```


### Clone the Repository
Make sure you have `git` installed in your syatem. <br><br>
Clone the repository using the following command:
```
git clone https://github.com/MhmdRyhn/rest_task.git
```


### Setup Virtual Environment and Install Required Packages
After cloning the repository, enter into the project directory.
```
cd rest_task/
```
Now, create virtual environment using following command. Make sure `virtualenv` package is installed in the system.
```
virtualenv -p python3 venv
```
If Python version 3.x is the default version in your system, you can use `python` instead of `python3` in the above command. <br><br>
Activate the virtual environment:
```
source venv/bin/activate
```
Install packages using `pip`:
```
pip3 install -r requirements.txt
```
If `pip3` doesn't work, use `pip` instead.



### Start Django Server
Open terminal. Make sure that you are in the project root directory in terminal window/tab. <br><br>
Start the **django server** using the following command.
```
python3 manage.py runserver
```
If Python version 3.x is the default version in your system, you can use `python` instead of `python3` in the above command. <br><br>


### Send Request Using Postman
#### Post Request:
Send a **Post** request using following payload to `http://127.0.0.1:8000/values`

**Payload**
```
{
  "key1": "v1",
  "key2": "v2",
  "key3": "v3"
}
```

**Response:**
```
{
  "status_code": 200,
  "body": {
      "key3": "v3",
      "key2": "v2",
      "key1": "v1"
  }
}
```

#### Get Request:
- Send **Get** request to `http://127.0.0.1:8000/values`. It will return all the key-value stored in Database.
- Send **Get** request to `http://127.0.0.1:8000/values?keys=key1,key2,key3`. It will return the key-value pairs found in the storage. If some key is not found, those keys are shown as *Key not found in storage* in error section of the response.


#### Patch Request
Send **Patch** request to `http://127.0.0.1:8000/values`. It will update the value of the keys found. The keys that are not found in the storage will be shown as *Key not found in storage* in error section of the response.

**Payload**
```
{
  "key1": "v1-1",
  "key2": "v2",
  "key4": "v4-1"
}
```




