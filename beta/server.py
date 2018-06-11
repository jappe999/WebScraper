import socket, json, re, errno, signal, os
from colorama import Fore, Back, Style
from database import Database

class Server:
    def __init__(self, host, port, num_links):
        self.host      = host
        self.port      = port
        self.num_links = num_links
        self.db        = Database('root', 'YOUR_PASSWORD', 'beta')

    @staticmethod
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

    def parse_request(self, request):
        if re.search('(\[.*\])', request):
            post_data = re.search('\[(.*)\]', request).group(1)
            urls      = (re.sub('\s*\'\s*', '', post_data)).split(',')

        return urls

    def set_queue(self, urls):
        if self.db.set_queue(urls):
            print(Fore.GREEN + 'Added', urls, 'to queue.')
            print(Style.RESET_ALL)
        else:
            print(Fore.WHITE + urls)
            print(Fore.RED + '----------Adding links to queue failed!----------')
            print(Style.RESET_ALL)

    def generate_response(self, request):
        response = 'HTTP/1.1 200 OK \n\n'

        if re.search('POST \/get', request):
            response += json.dumps(self.db.get_queue(self.num_links))

        return response

    def handle(self, client_connection):
        request = client_connection.recv(4096)
        request = str(request.decode())

        urls = self.parse_request(request)
        self.set_queue(urls)
        http_response = self.generate_response(request)

        client_connection.sendall(bytes(http_response, 'utf8'))
        client_connection.close()

    def listen(self):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((self.host, self.port))
        listener.listen(1024)

        print(Fore.WHITE + 'Listening on Port', self.port)

        signal.signal(signal.SIGCHLD, Server.grim_reaper)

        self.serve(listener)


    def serve(self, listener):

        while True:
            try:
                client_connection, client_address = listener.accept()
            except IOError as e:
                code, msg = e.args
                # restart 'accept' if it was interrupted
                if code == errno.EINTR:
                    continue
                else:
                    raise

            pid = os.fork()
            if pid == 0:
                listener.close()  # close child copy

                self.handle(client_connection, self.num_links)

                client_connection.close()
                os._exit(0)
            else:
                client_connection.close()  # close parent copy and loop over
