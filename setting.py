ENV = 'DEV'
USE_TEST_DATA = True


def get_db_config():
    if ENV == 'DEV':
        return {
            'host': '10.64.53.223',
            'username': 'tpas',
            'password': 'letmein',
            'database': 'tpas'
        }
    elif ENV == 'QA':
        return {
            'host': '10.64.53.223',
            'username': 'tpasqa',
            'password': 'tp@qa#123',
            'database': 'tpas_QA'
        }
    elif ENV == 'PROD':
        return {
            'host': '10.64.195.226',
            'username': 'tpasprod',
            'password': 'tp@prod#123',
            'database': 'tpas'
        }
