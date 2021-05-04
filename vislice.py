import bottle
import model

vislice = model.Vislice()

@bottle.get('/')
def zacetna_stran():
    return bottle.template('views/index.tpl')

@bottle.post('/igra/')
def nova_igra():
    id = vislice.nova_igra()
    return bottle.redirect(f'/igra/{id}/')

@bottle.get('/igra/<id:int>/')
def pokazi_igro(id):
    igra, stanje = vislice.igre[int(id)]
    return bottle.template('views/igra.tpl', igra=igra, stanje=stanje)

@bottle.post('/igra/<id:int>/')
def ugibaj(id):
   crka = bottle.request.forms.get('crka')
   vislice.ugibaj(id, crka)
   bottle.redirect(f'/igra/{id}/')

bottle.run(reloader=True, debug=True)