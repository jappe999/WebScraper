from fileSystem import *
from database import Database

db = Database('root', '1q2w3e4r!@#$', 'beta')
while True:
    try:
        queue = db.getQueue(20)
        if queue:
            print(queue)
            for q in queue:
                print('\n')
                for u in q:
                    print(u)
                    try:
                        c = getContents(u)
                        if not c is False:
                            m = getMeta(u)
                            setData(m, u, 'Meta')
                            setData(c, u, 'Content')
                    except Exception as e:
                        print(e)
                        continue
        else:
            break
    except:
        break
db.close()
