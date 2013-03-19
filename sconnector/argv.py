import re
import sys
from exception import ParameterError


def getcmd ():
  argv = sys.argv[1:]

  if len(argv) <= 0:
    raise ParameterError('No parameter assinged', argv)

  return argv[0]


def getargv (cmd):
  iargv = sys.argv[1:]

  if len(iargv) <= 1:
    raise ParameterError('Two or more parameters are required to execute', iargv)

  argv = iargv[1:]
  i = 0
  param = { 'argv': iargv }

  while True:
    val = argv[i]

    if cmd == 'forwarding':
      if re.match(r"-n|--no-shell", val):
        param['noshell'] = argv[i + 1]
      elif re.match(r"-s|--source", val):
        param['source'] = argv[i + 1]
      elif re.match(r"-o|--source-port", val):
        param['source_port'] = argv[i + 1]
      elif re.match(r"-d|--destination", val):
        param['destination'] = argv[i + 1]
      elif re.match(r"-r|--destination-port", val):
        param['destination_port'] = argv[i + 1]
      elif re.match(r"-x|--exit", val):
        param['stop'] = True
    elif cmd == 'copy':
      if re.match(r"-s|--source", val):
        param['source'] = argv[i + 1]
      elif re.match(r"-S|--remote-source", val):
        param['remote_source'] = argv[i + 1]
      elif re.match(r"-d|--destination", val):
        param['destination'] = argv[i + 1]
      elif re.match(r"-D|--remote-destination", val):
        param['remote_destination'] = argv[i + 1]

    if re.match(r"-t|--target", val):
      param['target'] = argv[i + 1]
    elif re.match(r"-p|--ssh-destination-port", val):
      param['ssh_destination_port'] = argv[i + 1]
    elif re.match(r"-i|--identity-file", val):
      param['pem_file'] = argv[i + 1]
    elif re.match(r"-h|--host", val):
      param['host'] = argv[i + 1]

    i += 2

    if len(argv) <= i:
      break;

  return param
