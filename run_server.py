from Server import app
from twisted.internet import reactor
from twisted.web.proxy import ReverseProxyResource
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource


if __name__ == "__main__":
    #host="192.168.163.1", port=80,
    #app.run(debug=True)

    def run_twisted_wsgi():
        from twisted.internet import reactor
        from twisted.web.server import Site
        from twisted.web.wsgi import WSGIResource

        resource = WSGIResource(reactor, reactor.getThreadPool(), app)
        site = Site(resource)
        reactor.listenTCP(5000, site)
        reactor.run(**reactor_args)


    if app.debug:
        # Disable twisted signal handlers in development only.
        reactor_args['installSignalHandlers'] = 0
        # Turn on auto reload.
        import werkzeug.serving

        run_twisted_wsgi = werkzeug.serving.run_with_reloader(run_twisted_wsgi)

    run_twisted_wsgi()