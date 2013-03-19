def getdoc ():
  return '''
 = Secure Connector v0.01
 = Saneyuki Tadokoro @ gfunction Computer Science Laboratory

useage: sconnect [command] [options]

Command:
  checkconf  : Check a configuration file.
  copy       : Use secure copy.
  forwarding : Use SSH port forwarding.
  help       : Display heredoc.
  remote     : Remote host.

Options (forwarding, stop, remote, copy):
  -h, --host                 : Connect to the host
  -i, --identity-file        : Select an identity file
  -p, --ssh-destination-port : Specify SSH port
  -t, --target               : Select target data

Options (forwarding):
  -d, --destination          : Specify destination for IP or DNS name
  -n, --no-shell             : Do not run remote shell
  -o, --source-port          : Use the source port
  -r, --destination-port     : Use the destination port
  -s, --source               : Specify source for IP or DNS name
  -x, --exit                 : Stop using SSH port forwarding

Options (copy):
  -s, --source               : Specify local directory as a source
  -S, --remote-source        : Specify remote directory as a source
  -d, --destination          : Specify local directory as a destination
  -D, --remote-destinaion    : Specify remote directory as a destination
'''
