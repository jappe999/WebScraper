import socket, json, re
from database import Database
from colorama import init, Fore, Back, Style

def main(host, port, numberOfLinks):
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((host, port))
    listen_socket.listen(1)
    print(Fore.WHITE + "Serving on Port", port)
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(4096)
        postData = ""
        urls = []
        #print(request)
        if re.search("(\[.*\])", str(request)):
            postData = re.search("\[(.*)\]", str(request)).group(1)
            #print(postData)
            urltemp = postData.split(',')
            urlsnew = []
            for url in urltemp:
                #print(url)
                url = re.sub("\s*\"\s*", "", url)
                urls.append(url)
        else:
            postData = "No POST-data received"

        database = Database('root', '1q2w3e4r!@#$', 'beta')
        if database.setQueue(urls):
            print(Fore.GREEN + "Added", urls, "to queue.")
            print(Style.RESET_ALL)
        else:
            print(Fore.WHITE + urls)
            print(Fore.RED + "----------Adding links to queue failed!----------")
            print(Style.RESET_ALL)
        http_response = "HTTP/1.1 200 OK \n\n"
        if re.search('POST \/get', str(request)):
            http_response += json.dumps(database.getQueue(numberOfLinks))
        database.close()
        client_connection.sendall(bytes(http_response, 'utf8'))
        client_connection.close()

    print(queue)
    print (len(queue))

if __name__ == "__main__":
    init()
    main("", 420, 10)
