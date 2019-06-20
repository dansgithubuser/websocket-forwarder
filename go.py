import os
import sys

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(DIR, 'deps'))

import djangogo

parser = djangogo.make_parser()
args = parser.parse_args()
djangogo.main(args,
    project='proj_websocket_forwarder',
    app='websocket_forwarder',
    db_name='db_websocket_forwarder',
    db_user='u_websocket_forwarder',
    heroku_url='https://websocket-forwarder.herokuapp.com/',
    heroku_repo='https://git.heroku.com/websocket-forwarder.git',
)
