class Database(object):
    def __init__(self):
        pass

    # Returns an object with (fake) data
    def getQueue(self, start, numberOfLinks):
        with open('./queue.txt', 'r') as fr:
            fakeData = [r.read()]
            return fakeData

    # Always returns True
    def setQueue(self, obj):
        return True
