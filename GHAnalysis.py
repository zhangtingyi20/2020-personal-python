import json
import sys
import os

def begin(path):
	pe = open('PushEvent.json','a',encoding='utf-8')
	ic = open('IssueCommentEven.json','a',encoding='utf-8')
	ie=open('IssuesEvent.json','a',encoding='utf-8')
	pr=open('PullRequestEvent.json','a',encoding='utf-8')
	file = os.listdir(path)
	for i in file:
		if (os.path.splitext(i)[1] == '.json'):
			with open(path+"//"+i, 'r', encoding='utf-8') as f:
					for jsonstr in f.readlines(): 
						date = json.loads(jsonstr)
						if(date['type']=='PushEvent'):
							pe.write(json.dumps(date))
							pe.write('\n')
						elif(date['type']=='IssueCommentEvent'):
							ic.write(json.dumps(date))
							ic.write('\n')
						elif(date['type']=='IssuesEvent'):
							ie.write(json.dumps(date))
							ie.write('\n')
						elif(date['type']=='PullRequestEvent'):
							pr.write(json.dumps(date))
							pr.write('\n')
	pe.close()
	ic.close()
	ie.close()
	pr.close()

	
def findnum(name,repo,event):
	num=0
	if(name==' ' and repo!=' '):
		with open(event+'.json', 'r', encoding='utf-8') as f:
				for jsonstr in f.readlines(): 
					date = json.loads(jsonstr)
					if(date['repo']['name']==repo):
						num=num+1
	elif(repo==' ' and name !=' '):
		with open(event+'.json', 'r', encoding='utf-8') as f:
				for jsonstr in f.readlines(): 
					date = json.loads(jsonstr)
					if(date['actor']['login']==name):
						num=num+1
	elif(repo!=' ' and name !=' '):
		with open(event+'.json', 'r', encoding='utf-8') as f:
				for jsonstr in f.readlines(): 
					date = json.loads(jsonstr)
					if(date['actor']['login']==name and date['repo']['name']==repo):
						num=num+1
	elif(repo==' ' and name ==' '):
		return
	print(num)

		

if __name__ == '__main__':
	if('-i' in sys.argv):
		begin(sys.argv[sys.argv.index('-i')+1])
	elif('--init' in sys.argv):
		begin(sys.argv[sys.argv.index('--init')+1])

	if('-u' in sys.argv):
		username=sys.argv[sys.argv.index('-u')+1]
	elif('--user' in sys.argv):
		username=sys.argv[sys.argv.index('--user')+1]
	else:
		username=' '
	if('-r' in sys.argv):
		userepo=sys.argv[sys.argv.index('-r')+1]
	elif('--repo' in sys.argv):
		userepo=sys.argv[sys.argv.index('--repo')+1]
	else:
		userepo=' '
	if('-e' in sys.argv):
		event=sys.argv[sys.argv.index('-e')+1]
	elif('--event' in sys.argv):
		username=sys.argv[sys.argv.index('--event')+1]
	else:
		event=' '
	findnum(username,userepo,event)
	

	
