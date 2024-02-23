from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hola' in lowered:
        return 'holaaa!'
    elif 'como estas' in lowered:
        return 'Muy bien, gracias!'
    elif 'adios' in lowered:
        return 'Hasta la proxima!'
    elif 'si' in lowered:
        return 'A bueno, pa saber!'
    elif 'que' in lowered:
        return 'SEXY!'
    elif 'tira un dado' in lowered:
        return f'Tu sacaste: {randint(1, 6)}'
    else:
        return choice(['Yo no te entiendo...',
                       'De que me estas hablando?',
                       'Acaso sabes como se pronuncia eso?'])