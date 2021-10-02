
def execute():
    from cards.models import Card, Module

    print("[!] Se eliminara la base de datos y se volvera a crear con data predefinida.")
    validacion = input("Continuar = 1 | Cancelar = 2: ")
    
    if validacion != "1":
        print("[*] Se ha cancelado el script.")
        return

    Module.objects.all().delete()
    Card.objects.all().delete()

    module_names = [1, 2, 3, 4, 5, 6]

    cards = [
        [1, 'Kaizen', 2, 'Pero ¿en qué consiste la estrategia Kaizen de mejora constante? «¡Hoy mejor que ayer, mañana mejor que hoy!» es el lema de este principio milenario. En otras palabras: las cosas siempre se pueden—y deben— hacer mejor. Por tanto, ni un solo día debería pasar sin llevar a cabo una cierta mejora.'],
        [3, 'Introducción Artes Secretas', 1, 'No imaginas la de veces que metacharon de pirado. Por aquel entonces me hubiese conformado con que alguien me concediese que en la seducción existían pautas. Me habría contentado con que me dijesen: «Sí, Mario, yo también creo que el amor y la atracción son fenómenos que pueden estudiarse». Pero jamás ocurrió. Eran otros tiempos.'],
        [2, 'LA META: ACTIVARSUPUNTO GG', 3, 'El león se queda hipnotizado contemplando a una gacela. Los pájaros se sienten impulsados a cantar por las mañanas. Las hormigas construyen hormigueros sin deliberarlo. Ya ti, que estás leyendo esto, se te dilatan las pupilas cuando te cruzas con ese pivonazo.'],
        [4, 'Su hombre GANADOR', 2, 'Así que allá va la primera pregunta: ¿te consideras un Ganador? Puede que ya lo seas y solo necesites enterarte. Quizá aún no hayas llegado ahí, pero con un poco de dedicación y constancia vas a adquirir la capacidad de «hacer como si lo fueras hasta que lo seas» de verdad.'],
    ]
    
    if Module.objects.filter(module_type=1) != True:
        
        for module_name in module_names:

            new_module = Module.objects.create()

            new_module.module_type = module_name

            new_module.save()

        print("[+] Modulos creados...")

    
    for card in cards:
        
        module = Module.objects.filter(module_type=card[0]).first()
        new_card = Card.objects.create(card_module=module)
        
        new_card.title = card[1]
        new_card.rarity = card[2]
        new_card.description = card[3]
        
        new_card.save()

    print("[+] Tarjetas creadas...")
    print("[*] DONE !")
