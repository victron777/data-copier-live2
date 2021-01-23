import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': 'localhost',
            'DB_NAME': 'sourceDB',
            'DB_USER': os.environ.get('DB_USER'),
            'DB_PASS': os.environ.get('DB_PASS')
        },
        'TARGET_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': 'localhost',
            'DB_NAME': 'targetDB',
            'DB_USER': os.environ.get('DB_USER'),
            'DB_PASS': os.environ.get('DB_PASS')
        }
    }

}

