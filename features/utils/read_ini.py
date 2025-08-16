import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def get_ini_data(block, key):
    try:
        return config[block][key]
    except KeyError as e:
        raise KeyError(f"Missing section/key: {e}")

print(get_ini_data('AppData','url'))





