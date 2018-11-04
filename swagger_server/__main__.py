#!/usr/bin/env python3

import connexion
import os

from swagger_server import encoder


def main():
    if os.environ.get('GOOGLE_API_KEY') == None:
        print("The environment variable \"GOOGLE_API_KEY\" is not set.\nPlease set your API key and try again")
        exit()

    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Geocoder'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
