import bottle
import model


@bottle.get('/')
def zacetna_stran():
    return bottle.template('zacetna_stran.tpl')


bottle.run(reloader=True, debug=True)