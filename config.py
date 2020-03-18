from uuid import UUID
from os import environ

host = '0.0.0.0'
port = 80
debug = True

pg_user = environ.get('POSTGRES_USER') or 'postgres'
pg_pass = environ.get('POSTGRES_PASSWORD') or ''
PG_URI = f'postgres://{pg_user}:{pg_pass}@pg'


APP_SECRET = UUID('8036587d-11ea-4c59-af9b-9da52eded1bc').bytes

NGX_IMAGE_PATH = '/var/ngx_img/{}'
NGX_IMAGE_URL = '/ngx_img/{}'
CUT_SIZES = [
    (256, 256),
    (512, 512),
    (1024, 1024),
    (2048, 2048),
]
DELETE_FILE_ON_DELETE = False

NOT_FOUND_IMAGE_CONTENT_TYPE = 'image/jpeg'
with open('not-found.jpg', 'rb') as f:
    NOT_FOUND_IMAGE = f.read()
