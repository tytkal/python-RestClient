__author__ = 'khalid'
import urllib2 , hmac , base64
from hashlib import sha1
import hmac , requests
import json
from bson import json_util
class RestClient:
    User_Agent = 'ubuntu'
    host = 'http://127.0.0.1:8080/'
    Content_Type = 'Aplication/json'
    Date = ''
    headers = {}
    data = []
    status_code = ''
    url = ''

    def put_header(self,key,value):
        self.headers[key]=value

    def resourse(self,append):
        self.host += append

    def signature(self):
        stringTosign = self.Content_Length+self.User_Agent+self.host+self.Content_Type+self.Accept_Encoding+self.Date
        signature = hmac.new(self.secret_token,stringTosign.replace(" ", ""),sha1)
        signature = base64.b64encode(signature.digest())
        return signature

    def get(self,resource):
        resp = requests.get(self.host+resource,headers=self.headers)
        self.save_data(resp)

    def post(self,data,resource):
        resp = requests.post(self.host+resource,data=json.dumps(data),headers=self.headers)
        self.save_data(resp)

    def put(self,data,resource):
        resp = requests.put(self.host+resource,data=json.dumps(data),headers=self.headers)
        self.save_data(resp)

    def delete(self,resource,parms=None):
        resp = requests.delete(self.host+resource,params=parms,headers=self.headers)
        print resp.url
        self.save_data(resp)

    def save_data(self,resp):
        self.data = json.loads(resp.text)
        self.status_code = resp.status_code
        self.url = resp.url

#req.add_header('Authorization','General 12331123:'+signature)
'''req = RestClient()
body = {'username':'khalid','email':'tytkal@gmail.com','fullname':'khalid abdulrahman alhussayen-','phone':'0506411119'}

req.post(body,'user')
print req.status_code
print req.data
#parms = {'user_id':'525a5d6d562d5727e640b209'}
#req.delete('user/525a5d6d562d5727e640b209/')
#res.add_header('Authorization','USER-Auth acssessKey:base64(SHA1(secretkey,stringtosign),Username:base64(SHA1(password,stringtosign)')
#req.delete('user/tytkal/')
#print req.status_code'''
