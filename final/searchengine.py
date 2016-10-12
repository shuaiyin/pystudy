from pysqlite2 import dbapi2 as sqlite
class crawler:
	#init a crawler and import the name of db 
	def __init__(self,dbname):
		#if the db is not exist,it will auto create
		self.con = sqlite.connect(dbname)

	def __del__(self):
		self.con.close()
	def dbcommit(self):
		self.con.commit()#submit the transaction 

	#use as get the id of the row,if not exist, add it into db 
	def getentryid(self,table,field,value,createnew=True):
		return None 

	#build index for each url 
	def addtoindex(self,url,soup):
		print 'Indexing %s' % url 

	#fetch words fron html(free of tag )
	def gettextonly(self,soup):
		return None 

	#split sentence into words 
	def seperatewords(self,text):
		return None 

	#if the index of the url has been build ,then return true
	def isindexed(self,url):
		return False

	#add a link to connect two url 
	def addlinkref(self,urlFrom,urlTo,linkText):
		pass

	#do Breadth-First-Search(guang) from a group of url,util the specify deep 
	#at the same time,build indexes for the url  
	def crawl(self,pages,depth=2):
		pass

	#create the table of database 
	def createindextables(self):
		pass

class searcher:
	def __init__(self,dbname):
		self.con = sqlite3.connect(dbname)

	def __del__(self):
		self.con.close()

	def getmatchrows(self,q):
		#construct query string 
		fieldlist = 'w0.urlib'
		tablelist = ''
		clauselist = ''
		wordids = []
		#split word by space 
		words = q.split(' ')
		tablenumer = 0 

		for word in words:
			#get the id of the word 
			sql = "select rowid fron wordlist where word='%s'"
			wordrow = self.con.execute("select rowid from wordlist w")



















































