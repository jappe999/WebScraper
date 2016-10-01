from os import system

pipInstalls = ['bs4', 'requests']

def main():
        try:
            items = ' '.join(pipInstalls)
            try:
                command = 'python -m pip install {}'.format(items)
                system(command)
            except:
                pass

            try:
                command = 'python3 -m pip install {}'.format(items)
                system(command)
            except:
                pass

            try:
                command = 'py -m pip install {}'.format(items)
                system(command)
            except:
                pass

            try:
                command = 'sudo python3 -m pip install {}'.format(items)
                system(command)
            except:
                pass

            print('Successfully initialized the Scraper.')
        except Exception as e:
            print('Error:', e)



if __name__ == '__main__':
    main()
