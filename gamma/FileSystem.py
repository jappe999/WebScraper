import os, re

def create_dir(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

        return True
    except Exception as e:
        print(e)

    return False

def set_data(url, html):
    stripped_path = re.sub('^(http://|https://)(www\.)?', '', url)
    directory     = 'data/' + stripped_path

    create_dir(directory)

    FILE_NAME = 'index.html'
    with open(directory + '/' + FILE_NAME, 'w+') as f:
        f.write(str(html))
        f.close()
