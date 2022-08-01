from configparser import  ConfigParser
import sys
import os
def read_config_data(filename=None, section=None, key=None):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    config_file_path = os.path.join(SCRIPT_DIR, '..', 'test_data', filename)
    parser = ConfigParser()
    parser.read(config_file_path)
    if section is not None and key is not None:
        return parser.get(section, key)
    # return None

# read_config_data('alphavantage_data.config')
