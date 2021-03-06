import bottle
import model

rezultat = 0
vrednost = 0


@bottle.get('/')
def zacetna_stran():
    return bottle.template('zacetna_stran.tpl')


@bottle.get('/matematika1/')
def matematika1():
    global rezultat
    return bottle.template('matematika1.tpl', rezultat = rezultat)



@bottle.get('/matematika2/')
def matematika2():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('matematika2.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/matematika3/')
def matematika3():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('matematika3.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/matematika4/')
def matematika4():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('matematika4.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/matematika5/')
def matematika5():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('matematika5.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/zgodovina1/')
def zgodovina1():
    global rezultat
    return bottle.template('zgodovina1.tpl', rezultat = rezultat)


@bottle.get('/zgodovina2/')
def zgodovina2():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('zgodovina2.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/zgodovina3/')
def zgodovina3():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('zgodovina3.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/zgodovina4/')
def zgodovina4():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('zgodovina4.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/zgodovina5/')
def zgodovina5():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('zgodovina5.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/geografija1/')
def geografija1():
    global rezultat
    return bottle.template('geografija1.tpl', rezultat = rezultat)


@bottle.get('/geografija2/')
def geografija2():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('geografija2.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/geografija3/')
def geografija3():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('geografija3.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/geografija4/')
def geografija4():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('geografija4.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/geografija5/')
def geografija5():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('geografija5.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)
    

@bottle.get('/sport1/')
def sport1():
    global rezultat
    return bottle.template('sport1.tpl', rezultat = rezultat)


@bottle.get('/sport2/')
def sport2():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('sport2.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/sport3/')
def sport3():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('sport3.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/sport4/')
def sport4():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('sport4.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/sport5/')
def sport5():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('sport5.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/konec/')
def konec():
    global rezultat
    vrednost = bottle.request.query['vrednost']
    rezultat += model.stevec(vrednost)
    skupna_vrednost = model.prav_narobe(vrednost)
    return bottle.template('koncna_stran.tpl', rezultat = rezultat, skupna_vrednost = skupna_vrednost)


@bottle.get('/')
def zacetek():
    global rezultat
    rezultat = 0
    return bottle.template('zacetna_stran.tpl')


@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')


bottle.run(reloader=True, debug=True)

