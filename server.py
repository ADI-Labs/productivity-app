#!/usr/bin/env python3

"""
Productivity Webserver

To run locally:

    python server.py

Go to http://localhost:8080 in your browser.
"""

import click


@click.command()
@click.option('--debug', is_flag=True)
@click.option('--threaded', is_flag=True)
@click.argument('HOST', default='0.0.0.0')
@click.argument('PORT', default=8080, type=int)
def serve(debug, threaded, host, port):
    """
    Run the server using:

        python server.py

    Show the help text using:

        python server.py --help

    """
    from app import app
    app.run(host=host, port=port, debug=debug, threaded=threaded)

if __name__ == '__main__':
    serve()
