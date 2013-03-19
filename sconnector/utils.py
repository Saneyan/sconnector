import json

def getobj (fn, coding = 'utf-8'):
  f = open(fn, 'r')

  # Convrt JSON into Python objects
  try:
    obj = json.load(f, coding)
  except ValueError, ve:
    raise ConfigError("An error occured when loading a configuration file. Check the permission and syntax.")

  f.close()
  return obj


def getdefault (obj, pre = None):
  if 'default' in obj:
    default = obj['default']
  else:
    default = {}

  if not 'settings' in default:
    default['settings'] = {}

  if pre != None:
    return update(pre, default)

  return default


def update (des, src):
  for key in src:
    if key == 'settings':
      des['settings'].update(src['settings'])
    else:
      des[key] = src[key]

  return des
