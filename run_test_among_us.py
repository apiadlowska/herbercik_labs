from among_us_full import AmongUsFullGame

try:
    game = AmongUsFullGame()
    print('Instantiated:', game.name, 'RAM:', game.ram_required)
except Exception as e:
    print('ERROR:', type(e).__name__, e)