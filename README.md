python-RestClient
=================
# RestClient
RestClient is an open source script that depends on requests library (http://docs.python-requests.org/en/latest/)
it was developed in 2012 and updated in 2014 by @Khalid Al-hussayen 
the script was used for my owen projects so it is limited to my use any one is welcome to update and fix the script.

## How to use 
You first need to install requests library
```sh
pip install requests
```
Then you can use the script 
## example
```py
from restClient import RestClient
res = RestClient()
res.host = '127.0.0.1:8080/'
res.resourse = 'resource' # the url will be 127.0.0.1:8080/resource
```
Then you can apply basic http methods like GET,POST etc...
if you want to use GET :
```py
res.get()
#if you want to put extrat url to the resourcr
res.get(append_url='/append')
#if you want to use basic auth
res.username = 'username'
res.password = 'password'
res.get(is_auth=True)
#if you want the responce 
res.responce.text
#if you want responce as json 
res.responce.json()
#status code
res.responce.status_code
```
to use post
```py
body = {'key':'value','key':'value'}
res.post(params=body,is_auth=True)
```
responce is an requests responce object for more information how to use responce see http://docs.python-requests.org/en/latest/user/quickstart/#response-content
