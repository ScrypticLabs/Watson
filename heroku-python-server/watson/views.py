from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting
from wit import Wit
from translate import Translator
import smtplib
import wolframalpha

WIT_AI_SERVER_TOKEN = "LYBE2RHXMFM5CDI5DORS2QOUZKL5R7AE"
WOLFRAM_ALPHA_ID = "83VQY6-L3EWU2VKAJ"

SENDER_ADDRESS = "abhisoccerplayer@gmail.com"
RECEIVER_ADDRESS = "atillaabc@gmail.com"

client = wolframalpha.Client(WOLFRAM_ALPHA_ID)

def index(request):
	query = request.GET
	if query.get("action") == "singleService":
		reply = witAI(query.get("text"),query.get("city"),query.get("state"),query.get("country"),"")
		return HttpResponse(reply)
	elif query.get("action") == "multiService":
		if query.get("sender") == "5198175265":
			reply = translate(query.get("text"), "french")
			return HttpResponse(reply)
		else:
			reply = translate(query.get("text"), "english")
			return HttpResponse(reply)

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})

def witAI(text, city, state, country, zipCode):
	response = Wit(WIT_AI_SERVER_TOKEN)
	command = dict(response.get_message(text))
	if command['outcomes'][0]['confidence'] >= 0.6:
		if command['outcomes'][0]['intent'] == "translate":
			language = command['outcomes'][0]['entities']['toLanguage'][0]['value'].lower()
			translateContent = command['outcomes'][0]['entities']['trContent'][0]['value'].lower()
			return translate(translateContent, language)
		elif command['outcomes'][0]['intent'] == "email":
			emailContent = command['outcomes'][0]['entities']['content'][0]['value']
			contact = command['outcomes'][0]['entities']['emailContact'][0]['value'].title()
			try:
				emailLanguage = command['outcomes'][0]['entities']['toLanguage'][0]['value'].lower()
				emailContent = translate(emailContent,emailLanguage)
			except:
				pass
			sendemail(from_addr    = SENDER_ADDRESS, 
			          to_addr_list = [RECEIVER_ADDRESS],
			          cc_addr_list = [], 
			          subject      = 'Email from Abhi Gupta via Watson', 
			          message      = emailContent,
			          login        = 'abhisoccerplayer@gmail.com', 
			          password     = 'hackathon')
			return "Your message has been sent to %s, courtesy of Watson." % contact

	else:
		return wolframAlpha(text)

def translate(content, language):
	lang_pack = {"english":"en","russian": "ru","french": "fr","japanese": "ja","italian": "it","spanish": "es","croatian": "hr","arabic": "ar"}
	lang = lang_pack[language]
	translator= Translator(to_lang=lang)
	return translator.translate(content)
 
def sendemail(from_addr, to_addr_list, cc_addr_list, subject, message, login, password, smtpserver='smtp.gmail.com:587'):
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

def wolframAlpha(text):
	res = client.query(text)
	try:
		return next(res.results).text
	except:
		try:
			for counter, pod in enumerate(res.pods):
			    if pod.text != None:
			    	return pod.text
		except:
			return "Sorry, I didn't understand that!"
	return "Sorry, I didn't understand that!"
