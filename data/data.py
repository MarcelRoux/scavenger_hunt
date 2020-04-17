import random
import string

keys = []

def shuffle_hints(hints):
    return random.sample(hints, len(hints))

def reset_keys():
    global keys
    
    keys = []

def get_key(N=3):
    key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    print(f'key: {key}')
    if(key not in keys):
        return key
    
    else:
        print(f'duplicate key: {key}')
        return get_key(N)

def get_data():
    return {
        "16L": {
            'egg_number': 1,
            'egg_type': 'egg',
            'room': 'kitchen',
            'location': 'chappies pack.',
            'hints': [
                'https://www.youtube.com/watch?v=sZsJyCyGBSI',
                'https://youtu.be/ve-HWks_eug?t=46', # Red herring.
                'This might be a red herring.' # Red herring.
                ]
        },
        "OTC": {
            'egg_number': 2,
            'egg_type': 'egg',
            'room': 'rear room',
            'location': 'make up station.',
            'hints': [
                'https://www.youtube.com/watch?v=oEx5Jh9MZ2Q',
                'https://youtu.be/1FQydx-s-5E?t=63', # Red herring.
                'https://youtu.be/GmYVfyqzu4Y?t=174' # Red herring
                ]
        },
        "N18": {
            'egg_number': 3,
            'egg_type': 'egg',
            'room': 'kitchen',
            'location': 'back of extractor hood, right side.',
            'hints': [
                'https://www.youtube.com/watch?v=C61sN8pKPGY',
                'https://youtu.be/ve-HWks_eug?t=177', # Red herring.
                'https://youtu.be/GmYVfyqzu4Y?t=102' # Red herring
                ]
        },
        "UO2": {
            'egg_number': 4,   
            'egg_type': 'egg',
            'room': 'kitchen',
            'location': 'Coffee machine hopper',
            'hints': [
                'https://youtu.be/1FQydx-s-5E?t=33',
                'https://youtu.be/ve-HWks_eug?t=46', # Red herring.
                'https://youtu.be/GmYVfyqzu4Y?t=57' # Red herring
                ]
        }
    }

def test_keys_uniqueness():
    print(f'keys start:\n{keys}')

    for i in range(10):
        keys.append(get_key(3))
    
    print(f'keys end:\n{keys}')

def main():

    reset_keys()

    # test_keys_uniqueness()
    print(get_data())



if __name__ == "__main__":
    main()