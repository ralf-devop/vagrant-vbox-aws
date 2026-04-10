import socket
import cowsay

cowsay.cow("Hello, I am on '"+ socket.gethostname() +"'!")
