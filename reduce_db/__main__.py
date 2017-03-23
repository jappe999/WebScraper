from database import Database

database = Database('root', '42069blazeIt', 'beta')

def process(url_id):
	self.execute("DELETE FROM queue WHERE ID='" + str(url_id) + "';")
	self.execute("DELETE FROM keywords WHERE url_id='" + str(url_id) + "';")
	print('Deleted', str(url_id))


def main(n):
	print('Hello World!')
	MAX_THREADS = 20
	threads = []
	try:
	    while True:
	        # Check for dead threads
	        for thread in threads:
	            if not thread.isAlive():
	                threads.remove(thread)

	        if not len(threads) >= MAX_THREADS: # Elsewise there would spam a great number threads
	            for row in database.getData(n):
	                t = Thread(target=process, args=(row[0],))
	                t.daemon = True
	                t.start()
	                threads.append(t)
	# Failsafe for dataloss
	except KeyboardInterrupt as e:
	    print(Fore.YELLOW + "keyboardInterrupt:")
	    print("Trying to peacefully shut down...")
	    print(Style.RESET_ALL)
	    while True:
	        for thread in threads:
	            if not thread.isAlive():
	                threads.remove(thread)
	        if len(threads) < 1:
				database.close()
	            break

if __name__ == '__main__':
	main(10)
