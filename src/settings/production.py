from .base import *

DEBUG = False

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'URL':  'postgres://ctmscmew:LqfJ2EQsBuNciYv9yH9GM_Vb-jQKzxov@satao.db.elephantsql.com/ctmscmew',
        'NAME': 'ctmscmew',
        'USER': 'ctmscmew',
        'PASSWORD': 'LqfJ2EQsBuNciYv9yH9GM_Vb-jQKzxov',
        'HOST': 'satao.db.elephantsql.com',
       
    }
}