import re
import os
from utils import getobj
from exception import ParameterError, ConfigError

class Checker:
  @staticmethod
  def checkcmd (cmd):
    if not re.match(r"^forwarding$|^remote$|^copy$|^checkconf$|^help$", cmd):
      raise ParameterError('First parameter must be "forwarding", "remote", "checkconf" or "help"')


  @staticmethod
  def checkargv (cmd, argv):
    if not 'target' in argv:
      raise ParameterError('Target data must be selected', argv['argv'])

    return True


  @staticmethod
  def checkconf (cmd, obj):
    if not 'username' in obj:
      raise ConfigError('There is not property "username"')

    if not 'host' in obj:
      raise ConfigError('There is not property "host"')

    if not 'ssh_destination_port' in obj:
      raise ConfigError('There is not property "ssh_destination_port"')

    if cmd == 'forwarding':
      if not 'source' in obj:
        raise Config('There is not property "source"')

      if not 'source_port' in obj:
        raise Config('There is not property "source_port"')

      if not 'destination' in obj:
        raise Config('There is not property "destination"')

      if not 'destination_port' in obj:
        raise Config('There is not property "destination_port"')

    return True


  @staticmethod
  def checkexistence (path):
    if os.path.exists(path) == False:
      raise ConfigError('No configuration file. Check the file path or create configuration file')

    return True


  @classmethod
  def checkfile (self, path):
    print " * Checking a configuration file\n"

    obj = getobj(path)

    if not 'remote' in obj:
      print "Caution: There is not 'remote' property in a configuration file. This means that you cannot use remote mode."

    if not 'forwarding' in obj:
      print "Caution: There is not 'forwarding' property in a configuration file. This means that you cannot use forwarding mode."

    if not 'copy' in obj:
      print "Caution: There is not 'copy' property in a configuration file. This means that you cannot use copy mode."

    return True
