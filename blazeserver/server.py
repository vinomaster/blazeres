#!/usr/bin/env python

from blaze import *
csv = CSV('../blaze/blaze/examples/data/iris.csv')
hmda = CSV('../blaze/blaze/examples/data/hmda-small.csv')
Data(csv)
Data(hmda)

from blaze.server import Server
server = Server({'iris': csv, 'hmda': csv})
server.run(host='0.0.0.0', port=6363)