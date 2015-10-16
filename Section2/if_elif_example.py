#!/usr/bin/env python3

def check_name(name, age):
    if name == 'Bob':
        return('Hi Bob')
    elif age < 12:
        return('You are not Alice, kiddo.')
    elif age > 3000:
        return('Unlike you, Alice is not immortal.')
    else:
        return('Hi Alice')

if __name__ == "__main__":
    print(check_name('billy', 10))