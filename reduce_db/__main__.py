from threading import Thread
from database import Database

database = Database('root', '42069blazeIt', 'beta')

def process(row):
	url_id = row[0]
	try:
		database.execute("DELETE FROM queue WHERE ID='" + str(url_id) + "';")
		database.execute("DELETE FROM keywords WHERE url_id='" + str(url_id) + "';")
		print('Deleted', str(url_id))
	except:
		print('Error deleting', str(url_id))


def main(n):
	print('Hello World!')
	try:
		while True:
			for row in database.getData(n):
				process(row)

	# Failsafe for dataloss
	except KeyboardInterrupt as e:
		database.close()

if __name__ == '__main__':
	main(10)
