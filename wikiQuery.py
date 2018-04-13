import os,requests,json
from StringIO import StringIO

if os.name == "nt": os.system("cls")
else:	os.system("clear")

print "\t\t\tWikipediaSearchQuery by Zakariaa Hamid :v"
print "\nfile path : "+os.getcwd()+"/"+__file__
print "UID : "+str(os.getuid())
print "GID : "+str(os.getgid())
print "PID : "+str(os.getpid())
print "\n"

try:
	while 1:
		searchQuery = str(raw_input("enter a search query : "))
		print "\n"
		wikiLink = "https://en.wikipedia.org/w/api.php?format=json&action=query&generator=search&gsrnamespace=0&gsrlimit=10&prop=pageimages|extracts&pilimit=max&exintro&explaintext&exsentences=1&exlimit=max&gsrsearch="+searchQuery
		wikiId = "https://en.wikipedia.org/?curid="
		jsonReq = requests.get(wikiLink).content
		io = StringIO(jsonReq)
		jsonLoad = json.load(io)
		for a in jsonLoad["query"]["pages"]:

			urlId = jsonLoad["query"]["pages"][a]["pageid"]
			urlIdOpen = requests.get(wikiId+str(urlId))
			urlIdOpen = urlIdOpen.url
			title = jsonLoad["query"]["pages"][a]["title"]
			print "\t\t" + title

			urltitle = "_".join(title.split(" "))
			urlIdOpen = "https://en.wikipedia.org/wiki/"+urltitle
			print "\t\t"+urlIdOpen

			print "\t\t"+jsonLoad["query"]["pages"][a]["extract"]
			print "\n"

except KeyboardInterrupt, e:
	print e
	print "GOOD BYE DUDE :) "
except:
	print "something went wrong :("
	print "please re execute the program"
