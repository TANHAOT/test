from otree.settings import BaseSettings

SESSION_CONFIGS = [
    dict(
        name='public_goods',
        display_name="Public Goods Game (2 Players)",
        num_demo_participants=2,
        app_sequence=['public_goods'],
    ),
]

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

# 默认数据库 SQLite，Render 免费 Postgres 可选
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# oTree secret key
SECRET_KEY = 's3cR3tK3y_XyzAbc1234567890_qwertyuiopASDFGHJKL'
