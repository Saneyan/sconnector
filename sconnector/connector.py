import subprocess

class Connector:

  @staticmethod
  def forwarding (config):

    print "\n * SSH port forwarding mode"

    args = ['ssh']

    settings = config['settings']

    if 'noshell' in settings and settings['noshell'] == True:
      print " * Do not execute remote command"
      args.extend([
        '-f',
        '-N',
        '-M',
        '-S', '/tmp/%(source)s:%(source_port)s.ctl' % config
      ])

    if 'publickey' in settings and settings['publickey'] == True:
      args.extend(['-i', config['pem_file']])

    args.extend([
      '-p', config['ssh_destination_port'],
      '-L', '%(source)s:%(source_port)s:%(destination)s:%(destination_port)s' % config,
      '%(username)s@%(host)s' % config
    ])

    print " * Connecting to %(username)s@%(host)s through port %(ssh_destination_port)s" % config
    print " * Tunneling to %(destination)s:%(destination_port)s from %(source)s:%(source_port)s\n" % config

    p = subprocess.Popen(args)
    p.wait()

    if p.returncode == 0 and settings['noshell'] == True:
      print "\n * Now this sub process has been running in the background"


  @staticmethod
  def stop (config):

    print "\n * Stopping SSH port forwarding..."

    args = [
      'ssh',
      '-S', '/tmp/%(source)s:%(source_port)s.ctl' % config,
      '-O', 'exit', '%(source)s' % config
    ]

    p = subprocess.Popen(args)
    p.wait()


  @staticmethod
  def remote (config):

    print " * SSH remote mode"

    args = ['ssh']

    settings = config['settings']

    if 'publickey' in settings and settings['publickey'] == True:
      args.extend(['-i', config['pem_file']])

    args.extend([
      '-p', config['ssh_destination_port'],
      '%(username)s@%(host)s' % config
    ])

    print " * Connecting to %(username)s@%(host)s through port %(ssh_destination_port)s\n" % config

    p = subprocess.Popen(args)
    p.wait()


  @staticmethod
  def copy (config, src = None, rsrc = None, des = None, rdes = None):

    print " * Copy mode"

    args = ['scp']

    settings = config['settings']

    if 'publickey' in settings and settings['publickey'] == True:
      args.extend(['-i', config['pem_file']])

    args.extend(['-P', config['ssh_destination_port']])

    if rsrc != None:
      args.extend(['%(username)s@%(host)s:' % config + rsrc])
    elif src != None:
      args.extend([src])

    if rdes != None:
      args.extend(['%(username)s@%(host)s:' % config + rdes])
    elif des != None:
      args.extend([des])

    print " * Connecting to %(username)s@%(host)s through port %(ssh_destination_port)s\n" % config

    p = subprocess.Popen(args)
    p.wait()
