import os
import logging

from tornado import web, ioloop
from sockjs.tornado import SockJSRouter, SockJSConnection

# Set Django Environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'wsrequest_example.settings'

from wsrequest import WebSocketRequest


logging.getLogger().setLevel(logging.INFO)


class IndexHandler(web.RequestHandler):
    def get(self, url='/'):
        self.render('templates/index.html')


class RESTAPIConnection(SockJSConnection):
    def on_message(self, data):
        logging.info(self.session.conn_info.ip)
        logging.info(self.session.conn_info.headers)
        request = WebSocketRequest(data)
        response = request.get_response()
        self.send({
            'response': {
                'url': request.get_url(),
                'data': response.data
            }
        })


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))

    Router = SockJSRouter(RESTAPIConnection, '/ws/api')

    app = web.Application(
        [(r'/', IndexHandler)] + Router.urls
    )

    app.listen(port)

    logging.info(' [*] Listening on 0.0.0.0:{}'.format(port))

    ioloop.IOLoop.instance().start()
