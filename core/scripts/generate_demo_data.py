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
        [1, 'Antes de tu primera entrevista', 2, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vel tellus lorem. Aliquam ut tortor nisl. In pulvinar vitae libero nec condimentum. Proin sem mauris, iaculis nec orci vel, tincidunt faucibus nunc. Suspendisse in commodo est. Donec est augue, varius sed diam ut, convallis tempus metus. Vestibulum elementum condimentum mauris non tempor.'],
        [3, 'En la entrevista', 1, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vel tellus lorem. Aliquam ut tortor nisl. In pulvinar vitae libero nec condimentum. Proin sem mauris, iaculis nec orci vel, tincidunt faucibus nunc. Suspendisse in commodo est. Donec est augue, varius sed diam ut, convallis tempus metus. Vestibulum elementum condimentum mauris non tempor.'],
        [2, 'Tu tambien tienes un valor', 3, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vel tellus lorem. Aliquam ut tortor nisl. In pulvinar vitae libero nec condimentum. Proin sem mauris, iaculis nec orci vel, tincidunt faucibus nunc. Suspendisse in commodo est. Donec est augue, varius sed diam ut, convallis tempus metus. Vestibulum elementum condimentum mauris non tempor.'],
        [4, 'Errores comunes', 2, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vel tellus lorem. Aliquam ut tortor nisl. In pulvinar vitae libero nec condimentum. Proin sem mauris, iaculis nec orci vel, tincidunt faucibus nunc. Suspendisse in commodo est. Donec est augue, varius sed diam ut, convallis tempus metus. Vestibulum elementum condimentum mauris non tempor.'],
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
