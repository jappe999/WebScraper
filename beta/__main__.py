import socket, json, re, errno, signal, os
from database import Database
from colorama import init, Fore, Back, Style

def grim_reaper(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,          # Wait for any child process
                 os.WNOHANG  # Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return

        if pid == 0:  # no more zombies
            return

def handle(client_connection, numberOfLinks):
    request = client_connection.recv(4096)
    request = request.decode()
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

    database = Database('root', '42069blazeIt', 'beta')
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

def main(host, port, numberOfLinks):
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((host, port))
    listen_socket.listen(1024)
    print(Fore.WHITE + "Serving on Port", port)

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msg = e.args
            # restart 'accept' if it was interrupted
            if code == errno.EINTR:
                continue
            else:
                raise

        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle(client_connection, numberOfLinks)
            client_connection.close()
            os._exit(0)
        else:  # parent
            client_connection.close()  # close parent copy and loop over

    print(queue)
    print (len(queue))

if __name__ == "__main__":
    init()
    main("", 420, 10)
