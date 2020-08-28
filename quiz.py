import bottle
import model


@bottle.get('/')
def zacetna_stran():
    return bottle.template('zacetna_stran.tpl')


@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')


bottle.run(reloader=True, debug=True)

