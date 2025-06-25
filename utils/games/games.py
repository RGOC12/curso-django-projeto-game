from random import randint

from faker import Faker




fake = Faker('pt_BR')
# print(signature(fake.random_number))

def rand_ratio():
    return randint(840, 900), randint(473, 573)

def make_games():
    return {
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
              'url': 'https://via.assets.so/game.png?id=1&q=95&w=360&h=360&fit=fill',
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_games())