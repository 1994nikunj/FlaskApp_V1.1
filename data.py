import datetime

# ----------------------------------------------------------------------------------------------------------------------
# POLLING FREQUENCY
# TABLE: tpas_polling_frequency
QUERT_1A = 'SHOW COLUMNS FROM tpas_polling_frequency'
tpas_polling_frequency_info = (
    ('frequency_id', 'int(11)', 'NO', 'PRI', None, 'auto_increment'),
    ('region_nm', 'char(20)', 'NO', '', None, ''),
    ('category', 'char(20)', 'NO', '', None, ''),
    ('modified_ts', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'on update CURRENT_TIMESTAMP'),
    ('created_ts', 'datetime', 'NO', '', None, ''),
    ('specific_time', 'char(5)', 'NO', '', None, ''),
    ('frequency', 'char(4)', 'NO', '', None, '')
)
QUERT_1B = 'SELECT region_nm,category,specific_time,frequency,created_ts,modified_ts FROM tpas_polling_frequency'
tpas_polling_frequency_raw = (
    ('Atlanta', 'CUTIL', 'n/a', '15', datetime.datetime(2020, 5, 18, 21, 34, 43), datetime.datetime(2020, 6, 19, 11, 22, 28)),
    ('Atlanta', 'CMT', 'n/a', '30', datetime.datetime(2020, 5, 18, 21, 48, 4), datetime.datetime(2020, 6, 15, 1, 2, 10)),
    ('Atlanta', 'DOCSIS', 'n/a', '60', datetime.datetime(2020, 5, 18, 21, 48, 19), datetime.datetime(2020, 8, 11, 12, 41, 19)),
    ('Atlanta', 'INTERFACE', 'n/a', '15', datetime.datetime(2020, 5, 18, 21, 49, 33), datetime.datetime(2020, 6, 17, 20, 35, 8)),
    ('Atlanta', 'MINV', 'n/a', '5', datetime.datetime(2020, 5, 18, 21, 49, 47), datetime.datetime(2020, 7, 24, 22, 5, 40)),
    ('Atlanta', 'OFDMA', 'n/a', '120', datetime.datetime(2020, 5, 18, 21, 50), datetime.datetime(2020, 7, 9, 4, 44, 42)),
    ('Atlanta', 'RPHY', 'n/a', '60', datetime.datetime(2020, 5, 18, 21, 50, 15), datetime.datetime(2020, 8, 19, 14, 53, 23)),
    ('Atlanta', 'AGG', 'n/a', '120', datetime.datetime(2020, 6, 8, 10, 12), datetime.datetime(2020, 9, 9, 15, 42, 37)),
    ('Atlanta', 'Janine', '14:45', 'n/a', datetime.datetime(2020, 6, 17, 14, 32, 33), datetime.datetime(2020, 6, 17, 14, 38, 42)),
    ('Atlanta', 'HUB-R', 'n/a', '120', datetime.datetime(2020, 6, 26, 14, 58, 9), datetime.datetime(2020, 8, 9, 9, 43, 7)),
    ('Atlanta', 'MODEM-FLAP', 'n/a', '15', datetime.datetime(2020, 7, 2, 1, 32, 10), datetime.datetime(2020, 7, 2, 1, 32, 10)),
    ('Atlanta', 'OCML', 'n/a', '120', datetime.datetime(2020, 7, 10, 6, 36, 6), datetime.datetime(2020, 8, 7, 7, 36, 22)),
    ('Atlanta', 'STATIC-IP', '05:00', 'n/a', datetime.datetime(2020, 7, 15, 7, 47, 45), datetime.datetime(2020, 7, 15, 7, 47, 45)),
    ('San Diego', 'AGG', 'n/a', '30', datetime.datetime(2020, 8, 17, 16, 38, 33), datetime.datetime(2020, 8, 17, 16, 40, 30))
)

# ----------------------------------------------------------------------------------------------------------------------
# MIDSPLIT TRACKER DATA
# TABLE: tpas_midsplit_scheduled_tracker
QUERT_2A = 'SHOW COLUMNS FROM tpas_midsplit_scheduled_tracker'
tpas_midsplit_scheduled_tracker_info = (
    ('start_id', 'int(11)', 'NO', 'PRI', None, 'auto_increment'),
    ('host', 'varchar(100)', 'YES', '', None, ''),
    ('host_name', 'varchar(50)', 'YES', '', None, ''),
    ('site_id', 'varchar(10)', 'YES', '', None, ''),
    ('cycle_id', 'varchar(50)', 'YES', '', None, ''),
    ('polling_category', 'varchar(20)', 'YES', '', None, ''),
    ('device_type', 'varchar(50)', 'YES', '', None, ''),
    ('records', 'varchar(50)', 'YES', '', None, ''),
    ('firmware', 'varchar(50)', 'YES', '', None, ''),
    ('poll_start_time', 'varchar(50)', 'YES', '', None, ''),
    ('poll_end_time', 'varchar(50)', 'YES', '', None, ''),
    ('total_execution_time', 'varchar(50)', 'YES', '', None, ''),
    ('status', 'varchar(50)', 'YES', '', None, '')
)
QUERT_2B = 'SELECT site_id,polling_category,host,host_name,device_type,records,cycle_id,poll_start_time,poll_end_time,total_execution_time,status FROM tpas_midsplit_scheduled_tracker'
tpas_midsplit_scheduled_tracker_raw = (
    ('001', 'OFDMA', '174.68.240.127', 'PSP6CMTK01', 'CCAP', 'part3-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:04', '0.0', 'SUCCESS'),
    ('001', 'OFDMA', '174.68.255.214', 'PSP6CMTK02', 'CCAP', 'part4-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:04', '0.0', 'SUCCESS'),
    ('001', 'OFDMA', '174.68.255.209', 'AEP6CAPC01', 'CCAP', 'part1-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:03', '2020-04-08 03:00:05', '2.0', 'SUCCESS'),
    ('001', 'INTERFACE', '174.68.240.127', 'PSP6CMTK01', 'CCAP', 'part3-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:05', '1.0', 'SUCCESS'),
    ('001', 'INTERFACE', '174.68.255.214', 'PSP6CMTK02', 'CCAP', 'part4-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:06', '2.0', 'SUCCESS'),
    ('001', 'OFDMA', '174.68.255.211', 'AEP6RPCC03', 'RPHY CCAP', 'part7-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:08', '4.0', 'SUCCESS'),
    ('001', 'OFDMA', '174.68.255.213', 'AEP6RPCC05', 'RPHY CCAP', 'part8-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:08', '2020-04-08 03:00:12', '4.0', 'SUCCESS'),
    ('001', 'INTERFACE', '174.68.255.209', 'AEP6CAPC01', 'CCAP', 'part1-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:12', '8.0', 'SUCCESS'),
    ('001', 'OFDMA', '100.122.78.10', 'HOLTCAPC01', 'CCAP', 'part5-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:03', '2020-04-08 03:00:14', '11.0', 'SUCCESS'),
    ('001', 'INTERFACE', '100.122.78.10', 'HOLTCAPC01', 'CCAP', 'part5-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:15', '11.0', 'SUCCESS')
)

# ----------------------------------------------------------------------------------------------------------------------
# SCHEDULED POLL DATA
# tpas_scheduled_poller_tracker
QUERY_4A = 'SHOW COLUMNS FROM tpas_scheduled_poller_tracker'
tpas_scheduled_poller_tracker_info = (
    ('start_id', 'int(11)', 'NO', 'PRI', None, 'auto_increment'),
    ('host_ip', 'varchar(100)', 'YES', '', None, ''),
    ('host_name', 'varchar(50)', 'YES', '', None, ''),
    ('site_id', 'varchar(5)', 'YES', '', None, ''),
    ('cycle_id', 'varchar(50)', 'YES', '', None, ''),
    ('polling_category', 'varchar(15)', 'YES', '', None, ''),
    ('device_type', 'varchar(100)', 'YES', '', None, ''),
    ('records', 'varchar(15)', 'YES', '', None, ''),
    ('firmware', 'varchar(50)', 'YES', '', None, ''),
    ('poll_start_time', 'varchar(50)', 'YES', '', None, ''),
    ('poll_end_time', 'varchar(50)', 'YES', '', None, ''),
    ('total_polling_execution_time', 'varchar(50)', 'YES', '', None, ''),
    ('polling_status', 'varchar(10)', 'YES', '', None, ''),
    ('oids', 'varchar(20)', 'YES', '', 'oid-value', ''),
    ('index', 'varchar(10)', 'YES', '', '0', '')
)
QUERY_4B = 'SELECT site_id,polling_category,host_ip,host_name,device_type,records,cycle_id,poll_start_time,poll_end_time,total_polling_execution_time,polling_status FROM tpas_scheduled_poller_tracker'
tpas_scheduled_poller_tracker_raw = (
    ('001', 'CUTIL', '174.68.255.214', 'PSP6CMTK02', 'CCAP', 'part4-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:14', '10.0', 'Success'),
    ('001', 'CUTIL', '174.68.255.209', 'AEP6CAPC01', 'CCAP', 'part1-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:15', '11.0', 'Success'),
    ('001', 'CUTIL', '174.68.255.211', 'AEP6RPCC03', 'RPHY CCAP', 'part7-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:26', '22.0', 'Success'),
    ('001', 'CUTIL', '174.68.255.213', 'AEP6RPCC05', 'RPHY CCAP', 'part8-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:27', '23.0', 'Success'),
    ('001', 'CUTIL', '174.68.255.201', 'AEP6CMTK05', 'CCAP', 'part2-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:32', '28.0', 'Success'),
    ('001', 'CUTIL', '100.122.78.10', 'HOLTCAPC01', 'CCAP', 'part5-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:32', '28.0', 'Success'),
    ('001', 'CUTIL', '100.122.78.11', 'HOLTCAPC02', 'CCAP', 'part6-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:04', '2020-04-08 03:00:36', '32.0', 'Success'),
    ('001', 'CUTIL', '174.68.240.127', 'PSP6CMTK01', 'CCAP', 'part3-8', 'Apr-08-2020 03:00 AM', '2020-04-08 03:00:32', '2020-04-08 03:00:39', '7.0', 'Success'),
    ('001', 'CUTIL', '174.68.240.127', 'PSP6CMTK01', 'CCAP', 'part3-8', 'Apr-08-2020 03:15 AM', '2020-04-08 03:15:03', '2020-04-08 03:15:11', '8.0', 'Success'),
    ('001', 'CUTIL', '174.68.255.209', 'AEP6CAPC01', 'CCAP', 'part1-8', 'Apr-08-2020 03:15 AM', '2020-04-08 03:15:03', '2020-04-08 03:15:13', '10.0', 'Success')
)

# ----------------------------------------------------------------------------------------------------------------------
# DEVICE INVENTORY
# TABLE: tpas_device_inventory
QUERT_3A = 'SHOW COLUMNS FROM tpas_device_inventory'
tpas_device_inventory_info = (
    ('region_nm', 'varchar(100)', 'NO', '', None, ''),
    ('system_nm', 'varchar(100)', 'NO', '', None, ''),
    ('ipv4_addr', 'varchar(20)', 'NO', '', None, ''),
    ('ipv6_addr', 'varchar(100)', 'NO', '', None, ''),
    ('device_host_nm', 'varchar(100)', 'NO', '', None, ''),
    ('device_type_nm', 'varchar(25)', 'NO', '', None, ''),
    ('site_id', 'char(3)', 'NO', '', None, ''),
    ('poll_this_device', 'char(1)', 'NO', '', 'F', ''),
    ('created_ts', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', 'on update CURRENT_TIMESTAMP'),
    ('sysdesc', 'varchar(200)', 'YES', '', None, ''),
    ('model', 'varchar(200)', 'YES', '', None, ''),
    ('firmware', 'varchar(100)', 'YES', '', None, ''),
    ('vendor', 'varchar(200)', 'YES', '', None, ''),
    ('isActive', 'tinyint(1)', 'YES', '', '1', ''),
    ('communityString', 'varchar(200)', 'YES', '', None, ''),
    ('modified_ts', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', ''),
    ('modified_by', 'varchar(200)', 'YES', '', None, ''),
    ('ofdma_enabled', 'tinyint(1)', 'YES', '', None, ''),
    ('impromptu_poll', 'varchar(100)', 'YES', '', None, '')
)
QUERT_3B = 'SELECT region_nm,system_nm,site_id,ipv4_addr,device_host_nm,device_type_nm,poll_this_device,isActive,ofdma_enabled,created_ts,modified_ts FROM tpas_device_inventory'
tpas_device_inventory_raw = (
    ('Atlanta', 'Macon', '001', '10.0.251.234', 'EngOCML', 'OCML', 'T', 1, None, datetime.datetime(2020, 7, 10, 6, 19, 15), datetime.datetime(2019, 7, 1, 17, 42, 8)),
    ('Kansas', 'Kansas', '580', '100.120.189.1', 'GRBECAPC01', 'CCAP', 'F', 1, None, datetime.datetime(2018, 9, 7, 13, 24, 38), datetime.datetime(2019, 7, 1, 17, 42, 8)),
    ('Kansas', 'Kansas', '580', '100.120.189.10', 'WICHCAPC05', 'CCAP', 'F', 1, None, datetime.datetime(2019, 6, 26, 12, 40, 54), datetime.datetime(2019, 7, 1, 17, 42, 8)),
    ('Kansas', 'Kansas', '580', '100.120.189.11', 'WICHCAPC06', 'CCAP', 'F', 1, None, datetime.datetime(2018, 9, 7, 13, 24, 38), datetime.datetime(2019, 7, 1, 17, 42, 8)),
    ('Kansas', 'Kansas', '580', '100.120.189.12', 'WICHCAPC07', 'CCAP', 'F', 1, None, datetime.datetime(2018, 9, 7, 13, 24, 38), datetime.datetime(2019, 7, 1, 17, 42, 8)),
    ('Kansas', 'Kansas', '580', '100.120.189.13', 'WICHCAPC08', 'CCAP', 'F', 1, None, datetime.datetime(2018, 9, 7, 13, 24, 38), datetime.datetime(2019, 7, 1, 17, 42, 8)),
    ('Kansas', 'Kansas', '580', '100.120.189.14', 'WICHCAPC09', 'CCAP', 'F', 1, None, datetime.datetime(2018, 9, 7, 13, 24, 38), datetime.datetime(2019, 7, 1, 17, 42, 8)),
    ('Kansas', 'Kansas', '580', '100.120.189.15', 'WICHCAPC10', 'CCAP', 'F', 1, None, datetime.datetime(2018, 9, 7, 13, 24, 38), datetime.datetime(2019, 7, 1, 17, 42, 8)),
    ('Kansas', 'Kansas', '580', '100.120.189.16', 'WICHCAPC11', 'CCAP', 'F', 1, None, datetime.datetime(2018, 9, 7, 13, 24, 38), datetime.datetime(2019, 7, 1, 17, 42, 8)),
    ('Kansas', 'Kansas', '580', '100.120.189.17', 'WICHCAPC12', 'CCAP', 'F', 1, None, datetime.datetime(2018, 9, 7, 13, 24, 38), datetime.datetime(2019, 7, 1, 17, 42, 8))
)
