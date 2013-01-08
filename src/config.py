import os
import yaml

__all__ = [
    'host',
    'port',
    'resources'
]

config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
config = yaml.load(open(os.path.join(config_path, 'config.yml'), 'r').read())

host = config.get('host', '127.0.0.1')
port = config.get('port', '3000')
resources = config.get('resources', [])
