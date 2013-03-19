class ParameterError (Exception):
  def __init__ (self, message, argv = []):
    self.message = message
    self.argv = argv
    self.length = len(argv)


class ConfigError (Exception):
  def __init__ (self, message):
    self.message = message
