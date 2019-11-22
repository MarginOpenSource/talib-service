#!/usr/bin/env python

import argparse
import numpy
import rpyc
import talib
from rpyc.utils.server import ThreadedServer


class TaLibService(rpyc.Service):
    TALIB_FUNCTIONS_REGISTERED = False

    def __init__(self):
        TaLibService.__register_talib_functions()

    def on_connect(self, conn):
        print("- new connection {}".format(conn))

    def on_disconnect(self, conn):
        print("- connection closed for {}".format(conn))

    def remote_np(self):
        return numpy

    @staticmethod
    def __register_talib_functions():
        """Registers all ta-lib functions in the TaLibService class"""
        if TaLibService.TALIB_FUNCTIONS_REGISTERED:
            return
        TaLibService.exposed_get_function_groups = talib.get_function_groups
        TaLibService.exposed_get_functions = talib.get_functions
        for func in talib.get_functions():
            setattr(TaLibService, "exposed_" + func, getattr(talib, func))
        TaLibService.TALIB_FUNCTIONS_REGISTERED = True


def parse_args():
    parser = argparse.ArgumentParser(prog='margin-talib-service',
                                     description='Start a service that grants access to TA-Lib for margin strategies.',
                                     epilog='Check out https://github.com/MarginOpenSource/talib-service '
                                            'for more information.')
    parser.add_argument('-p', '--port', help='Specify the port that the service is binding to.', action='store',
                        default=18861, type=int)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    port = args.port
    print("Creating server on port {}".format(port))
    try:
        server = ThreadedServer(TaLibService, port=port,
                                protocol_config={'allow_all_attrs': True, 'allow_pickle': True})
    except OSError:
        print("Chosen port {} on localhost is already in use, please specify a different port.".format(port))
        return 1
    print("Starting TA-Lib service...")
    server.start()


if __name__ == "__main__":
    main()
