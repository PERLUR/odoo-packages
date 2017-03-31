#!/usr/bin/python
import csv
from lxml import etree as ET

"""
This script converts Accounts Template CSV file into XML file for use within OpenERP.
"""
__author__ = "Marek Stopka"
__copyright__ = "Copyright 2012, STOPKA Consulting s.r.o."
__credits__ = "Marek Stopka"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Marek Stopka"
__email__ = "marek.stopka@perlur.cz"
__status__ = "Production"

f = open('account.account.template.csv', 'rb')

def UnicodeDictReader(utf8_data, **kwargs):
  csv_reader = csv.DictReader(utf8_data, **kwargs)
  for row in csv_reader:
    yield dict([(key, unicode(value, 'utf-8')) for key, value in row.iteritems()])

cvs_file = UnicodeDictReader(f, delimiter=',', quotechar='"')

openerp = ET.Element('openerp')
data = ET.SubElement(openerp, 'data', noupdate="1")
for row in cvs_file:
  record = ET.SubElement(data, 'record', id=row['id'], model="account.account.template")
  field_code = ET.SubElement(record, 'field', name="code")
  field_code.text = row['code']

  field_name = ET.SubElement(record, 'field', name="name")
  field_name.text = row['name']

  if len(row['parent_id:id']) > 0:
    field_parent_id = ET.SubElement(record, 'field', name="parent_id", ref=row['parent_id:id'])

  field_type = ET.SubElement(record, 'field', name="type")
  field_type.text = row['type']

  field_user_type = ET.SubElement(record, 'field', name="user_type", ref=row['user_type:id'])

print ET.tostring(openerp, encoding='utf-8', pretty_print=True, xml_declaration=True)
