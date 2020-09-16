import json
import sys
import os

def begin(path):
	pe = open('PushEvent.json','a',encoding='utf-8')
	ic = open('IssueCommentEven.json','a',encoding='utf-8')
	ie=open('IssuesEvent.json','a',encoding='utf-8')
	pr=open('PullRequestEvent.json','a',encoding='utf-8')
	file = os.listdir(path)#得到文件列表
	for i in file:
		if (os.path.splitext(i)[1] == '.json'):#os.path.splitext(i)返回一个列表，首个元素为文件名。第二个元素为文件类型
			with open(path+"//"+i, 'r', encoding='utf-8') as f:
					for jsonstr in f.readlines(): #根据读到数据的不通将数据写入不同文件
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
#根据命令行参数进行不同的查找
	num=0
	if(name==' ' and repo!=' '):#项目名参数为空时
		with open(event+'.json', 'r', encoding='utf-8') as f:
				for jsonstr in f.readlines(): 
					date = json.loads(jsonstr)
					if(date['repo']['name']==repo):
						num=num+1
	elif(repo==' ' and name !=' '):#用户名名参数为空时
		with open(event+'.json', 'r', encoding='utf-8') as f:
				for jsonstr in f.readlines(): 
					date = json.loads(jsonstr)
					if(date['actor']['login']==name):
						num=num+1
	elif(repo!=' ' and name !=' '):#查询某项目中某用户某类型事件
		with open(event+'.json', 'r', encoding='utf-8') as f:
				for jsonstr in f.readlines(): 
					date = json.loads(jsonstr)
					if(date['actor']['login']==name and date['repo']['name']==repo):
						num=num+1
	#初始化输出0
	
	print(num)

		

if __name__ == '__main__':
	if('-i' in sys.argv):#根据命令行信息为参数赋值
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
	findnum(username,userepo,event)#调用函数findunm

	
