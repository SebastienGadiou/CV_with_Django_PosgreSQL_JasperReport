import os
from platform import python_version
from pyreportjasper import PyReportJasper
import psycopg2


def all():


    def del_previousrecords():
            connection = psycopg2.connect(host='localhost', database='MYCV', user='xxxxxxxxx', password='xxxxxxxx')
            cur = connection.cursor()
            cur.execute(
                'DELETE FROM public."createCV_allaboutme" WHERE id <> (SELECT max(id) FROM public."createCV_allaboutme")')
            connection.commit()
    del_previousrecords()



    def CVcreation():
       REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), r'C:\put the path here\template')
       input_file = os.path.join(REPORTS_DIR, 'CV.jrxml')
       output_file = os.path.join(REPORTS_DIR, 'CV')
       conn = {
         'driver': 'postgres',
         'username': 'xxxxxxx',
         'password': 'xxxxxxxx',
         'host': 'localhost',
         'database': 'MYCV',
         'schema': 'public',
         'port': '5432',
         'jdbc_driver' :'org.postgresql.Driver',
         'jdbc_dir':'C:\\put the path here \\postgresql-42.7.1.jar',
       }


       pyreportjasper = PyReportJasper()
       pyreportjasper.config(
         input_file,
         output_file,
         db_connection=conn,
         output_formats=['pdf','html'],
         parameters={'python_version': python_version()},
         locale='en_US')
       pyreportjasper.process_report()


    CVcreation()

all()
