
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insta_stat_v2.settings')

application = get_asgi_application()
