def includeme(config):
    from raven.base import Client    
    from raven.utils.wsgi import get_current_url, get_headers, \
      get_environ

    settings = config.registry.settings
    client_config = {}
    for key in settings:
        if key.startswith('raven.'):
            client_config[key[6:]] = settings[key]
    client = Client(**client_config)
    config.registry.raven = client
    client.get_current_url = get_current_url
    client.get_headers = get_headers
    client.get_environ = get_environ
