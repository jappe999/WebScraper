from threading import Thread
from database import Database

def process(row):
	url_id = row[0]
	database = Database('root', '42069blazeIt', 'beta')
	try:
		database.execute("DELETE FROM queue WHERE ID='" + str(url_id) + "';")
		database.execute("DELETE FROM keywords WHERE url_id='" + str(url_id) + "';")
		print('Deleted', str(url_id))
	except:
		print('Error deleting', str(url_id))


def main(n):
	print('Hello World!')
	MAX_THREADS = 20
	threads = []
	database = Database('root', '42069blazeIt', 'beta')
	try:
		while True:
			# Check for dead threads
			for thread in threads:
				if not thread.isAlive():
					threads.remove(thread)

			if not len(threads) >= MAX_THREADS: # Elsewise there would spam a great number threads
				for row in database.getData(n):
					t = Thread(target=process, args=(row,))
					t.daemon = True
					t.start()
					threads.append(t)

	# Failsafe for dataloss
	except KeyboardInterrupt as e:
		print("keyboardInterrupt:")
		print("Trying to peacefully shut down...")
		while True:
			for thread in threads:
				if not thread.isAlive():
					threads.remove(thread)
				if len(threads) < 1:
					database.close()
					break

if __name__ == '__main__':
	main(10)
