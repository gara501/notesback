from os import path
import os
import pymysql.cursors
import yaml

basepath = 'queries'

def openConnection():
  # Connect to the database
  
  condict = yaml.load(open('dbcon.yaml'), Loader=yaml.FullLoader)
  
  if condict['current'] == 'dev':
    conn = condict['dev']
  else:
    conn = condict['prod']

  connection = pymysql.connect(host=conn['host'],
                              user=conn['user'],
                              password=conn['password'],
                              db=conn["database"],
                              charset='utf8',
                              use_unicode=True,
                              port=conn['port'],
                              cursorclass=pymysql.cursors.DictCursor)
  return connection

def select(query):
  conn = openConnection()
  try:
    conn.commit()
    with conn.cursor() as cursor:
        sqlQuery = loadQueryFromFile(query)
        cursor.execute(sqlQuery)
        result = cursor.fetchall()
        return result
  finally:
      conn.close()

def insert(params):
  conn = openConnection()
  try:
    conn.commit()
    with conn.cursor() as cursor:
        sqlQuery = loadQueryFromFile(query)
        insertParams = getInsertData()
        cursor.execute(sqlQuery, insertParams)
        cursor.commit()
        return True
  finally:
      conn.close()

def loadQueryFromFile(queryName):
  file = getQueryFile(queryName)
  try:
   with open(file) as f: 
    print("Loading SQL file, please wait...")
    ret = f.read()
    return ret
  except IOError as e:
   print("Error: %s not found." % file)


def getQueryFile(queryName):
  queryFileName = queryName + '.sql';
  file = os.path.join(basepath, queryFileName)
  return file
