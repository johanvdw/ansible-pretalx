from .settings import *

INSTALLED_APPS += ["pghistory", "pgtrigger"]

MIDDLEWARE += ["pghistory.middleware.HistoryMiddleware"]

import pghistory

PGHISTORY_OBJ_FIELD = pghistory.ObjForeignKey(
    related_name="log_events", related_query_name="log_events"
)

#LOGGING = {
#    'version': 1,
#    'handlers': {
#        'console': {
#            'level': 'DEBUG',
#            'class': 'logging.StreamHandler',
#        },
#    },
#    'loggers': {
#        'django.db.backends': {
#            'handlers': ['console'],
#            'level': 'DEBUG',
#            'propagate': False,
#        },
#    },
#}

import mimetypes
mimetypes.add_type("text/css", ".css", True)
