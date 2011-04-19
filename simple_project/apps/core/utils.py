"""
Generate a random password.
Code from http://code.activestate.com/recipes/59873-random-password-generation/
"""
def gen_passwd(length=8, chars=string.letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])