import os
import urllib
from wit import Wit
import json
import goslate
import wolframalpha
import smtplib
import urllib2
import urllib
import httplib
from xml.etree import ElementTree as etree
import sys

WIT_AI_SERVER_TOKEN = "LYBE2RHXMFM5CDI5DORS2QOUZKL5R7AE"

response = os.system("curl \
      -H 'Authorization: Bearer LYBE2RHXMFM5CDI5DORS2QOUZKL5R7AE' \
      'https://api.wit.ai/message?v=20141022&q=where%20is%20the%20nearest%20McDonalds'")

request = json.loads(json.load(response))
print(request)

params = {}
params['access_token'] = 'LYBE2RHXMFM5CDI5DORS2QOUZKL5R7AE'
params['text'] = "where+is+the+nearest+McDonalds"
params = urllib.urlencode(params)
f = urllib.urlopen("https://api.wit.ai/message?v=20141022&q=", params)
print f.read()


def witAI(text, city, state, country, zipCode):
	response = Wit(WIT_AI_SERVER_TOKEN)
	return dict(response.get_message(text))

analysis = witAI("","","","","")
print(analysis['msg_id'])
print(analysis['_text'])
print(analysis['outcomes'][0]['intent'])
print(analysis['outcomes'][0]['confidence'])


gs = goslate.Goslate()
lang_pack = {"russian": "ru","french": "fr","japanese": "ja","italian": "it","spanish": "es","croatian": "hr","arabic": "ar"}
lang = lang_pack["french"]
print(gs.translate("hello how are you", "italian"))
try:
	print(gs.translate("hello how are you", "fr"))
except:
	print("Sorry, that language is not currently supported.")

 
class wolfram(object):
    def __init__(self, appid):
        self.appid = appid
        self.base_url = 'http://api.wolframalpha.com/v2/query?'
        self.headers = {'User-Agent':None}
 
    def _get_xml(self, ip):
        url_params = {'input':ip, 'appid':self.appid}
        data = urllib.urlencode(url_params)
        req = urllib2.Request(self.base_url, data, self.headers)
        xml = urllib2.urlopen(req).read()
        return xml
 
    def _xmlparser(self, xml):
        data_dics = {}
        tree = etree.fromstring(xml)
        #retrieving every tag with label 'plaintext'
        for e in tree.findall('pod'):
            for item in [ef for ef in list(e) if ef.tag=='subpod']:
                for it in [i for i in list(item) if i.tag=='plaintext']:
                    if it.tag=='plaintext':
                        data_dics[e.get('title')] = it.text
        return data_dics
 
    def search(self, ip):
        xml = self._get_xml(ip)
        result_dics = self._xmlparser(xml)
        print(result_dics['Result'])
 


 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

sendemail(from_addr    = 'abhisoccerplayer@gmail.com', 
          to_addr_list = ['atillaabc@gmail.com'],
          cc_addr_list = [], 
          subject      = 'Howdy', 
          message      = 'Howdy from a python function', 
          login        = 'abhisoccerplayer@gmail.com', 
          password     = 'hackathon')


client = wolframalpha.Client("83VQY6-L3EWU2VKAJ")
text = input()

while True:
	res = client.query(text)
	for counter, pod in enumerate(res.pods):
		if pod.text != None:
			print(pod.text)
	text = input()

if __name__ == "__main__":
    appid = "83VQY6-L3EWU2VKAJ"
    query = "how do you say hello how are you in french"
    w = wolfram(appid)
    w.search(query)


