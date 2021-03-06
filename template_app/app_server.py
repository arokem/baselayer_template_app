import tornado.web

from baselayer.app import models, model_util
from baselayer.app.app_server import (handlers as baselayer_handlers,
                                      settings as baselayer_settings)
from baselayer.app.config import load_config


from .handlers.example_computation import ExampleComputationHandler


def make_app(cfg, baselayer_handlers, baselayer_settings):
    """Create and return a `tornado.web.Application` object with specified
    handlers and settings.

    Parameters
    ----------
    cfg : Config
        Loaded configuration.  Can be specified with '--config'
        (multiple uses allowed).
    baselayer_handlers : list
        Tornado handlers needed for baselayer to function.
    baselayer_settings : cfg
        Settings needed for baselayer to function.

    """
    if cfg['cookie_secret'] == 'abc01234':
        print('!' * 80)
        print('  Your server is insecure. Please update the secret string ')
        print('  in the configuration file!')
        print('!' * 80)

    handlers = baselayer_handlers + [
    #    (r'/some_url(/.*)?', MyTornadoHandler),
        (r'/example_compute', ExampleComputationHandler)
    ]

    settings = baselayer_settings
    settings.update({})  # Specify any additional Tornado settings here

    app = tornado.web.Application(handlers, **settings)
    models.init_db(**cfg['database'])
    model_util.create_tables()
    app.cfg = cfg

    return app
