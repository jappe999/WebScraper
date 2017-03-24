from threading import Thread
from database import Database

def process(row):
	url_id   = row[0]
	indexed  = row[1]
	database = Database('root', '42069blazeIt', 'beta')
	try:
		if database.execute("DELETE FROM queue WHERE ID='" + str(url_id) + "';"):
			print('Deleted ID', str(url_id), 'from Queue...')
		else:
			return

		if indexed == 1:
			if database.execute("DELETE FROM keywords WHERE url_id='" + str(url_id) + "';"):
				print('Deleted url_id', str(url_id), 'from Keywords...')
			else:
				return
	except:
		print('Error deleting', str(url_id))
	finally:
		database.close()


def main(n):
	threads     = []
	MAX_THREADS = 20
	database    = Database('root', '42069blazeIt', 'beta')
	print('Hello World!')
	try:
		while True:
			# Check for dead threads
			for thread in threads:
				if not thread.isAlive():
					threads.remove(thread)

			if len(threads) < MAX_THREADS:
				for row in database.getData(n):
					t = Thread(target=process, args=(row,))
					t.deamon = True
					t.start()
					threads.append(t)

	# Failsafe for dataloss
	except KeyboardInterrupt as e:
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
