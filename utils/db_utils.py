import logging
import sqlite3 as sql

import pymysql

import setting

logger = logging.getLogger(__name__)
CONFIG = setting.get_db_config()


def get_polling_frequency_data():
    connection = None
    query = 'SELECT region_nm, category, specific_time, frequency, created_ts, modified_ts ' \
            'FROM tpas_polling_frequency'
    try:
        connection = pymysql.connect(host=CONFIG['host'],
                                     user=CONFIG['username'],
                                     password=CONFIG['password'],
                                     db=CONFIG['database'])
        cur = connection.cursor()
    except Exception as excp:
        logger.error("Exception Caught! {}".format(excp))
    else:
        try:
            cur.execute(query)
            return cur.fetchall()
        except Exception as excp:
            logger.error("Exception Caught! {}".format(excp))
        finally:
            cur.close()
    finally:
        connection.close()


def get_scheduled_poll_data():
    connection = None
    query = 'SELECT site_id, polling_category, host_ip, host_name, device_type, records, cycle_id, poll_start_time, ' \
            'poll_end_time, total_polling_execution_time, polling_status ' \
            'FROM tpas_scheduled_poller_tracker'
    try:
        connection = pymysql.connect(host=CONFIG['host'],
                                     user=CONFIG['username'],
                                     password=CONFIG['password'],
                                     db=CONFIG['database'])
        cur = connection.cursor()
    except Exception as excp:
        logger.error("Exception Caught! {}".format(excp))
    else:
        try:
            cur.execute(query)
            return cur.fetchall()
        except Exception as excp:
            logger.error("Exception Caught! {}".format(excp))
        finally:
            cur.close()
    finally:
        connection.close()


def get_midsplit_poll_data():
    connection = None
    query = 'SELECT site_id, polling_category, host,host_name, device_type, records, cycle_id, poll_start_time, ' \
            'poll_end_time, total_execution_time, status ' \
            'FROM tpas_midsplit_scheduled_tracker'
    try:
        connection = pymysql.connect(host=CONFIG['host'],
                                     user=CONFIG['username'],
                                     password=CONFIG['password'],
                                     db=CONFIG['database'])
        cur = connection.cursor()
    except Exception as excp:
        logger.error("Exception Caught! {}".format(excp))
    else:
        try:
            cur.execute(query)
            return cur.fetchall()
        except Exception as excp:
            logger.error("Exception Caught! {}".format(excp))
        finally:
            cur.close()
    finally:
        connection.close()


def get_inventory_data():
    connection = None
    query = 'SELECT region_nm, system_nm, site_id, ipv4_addr, device_host_nm, device_type_nm, poll_this_device, ' \
            'isActive, ofdma_enabled, created_ts, modified_ts ' \
            'FROM tpas_device_inventory'
    try:
        connection = pymysql.connect(host=CONFIG['host'],
                                     user=CONFIG['username'],
                                     password=CONFIG['password'],
                                     db=CONFIG['database'])
        cur = connection.cursor()
    except Exception as excp:
        logger.error("Exception Caught! {}".format(excp))
    else:
        try:
            cur.execute(query)
            return cur.fetchall()
        except Exception as excp:
            logger.error("Exception Caught! {}".format(excp))
        finally:
            cur.close()
    finally:
        connection.close()


def connection_2(request):
    try:
        db_conn = sql.connect('static/database/credentials_manager.db')
        cur = db_conn.cursor()
    except Exception as excp:
        logger.error("Exception Caught! {}".format(excp))
    else:
        try:
            cur.execute("SELECT * FROM get_uname_pwd WHERE username={} AND password={}".format(
                "'" + request.form['username'] + "'",
                "'" + request.form['password'] + "'"))
            return cur.fetchone()
        except Exception as excp:
            logger.error("Exception Caught! {}".format(excp))
        finally:
            cur.close()
            db_conn.close()
