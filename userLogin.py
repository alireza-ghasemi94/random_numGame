import mysql.connector
from cryptography.fernet import Fernet

class users:
  def __init__(self):
    self.user = 'ali'
    self.password_database = 'Qaz@1234'
    self.database = 'game'
    self.host = 'localhost'
    self.conn = self._get_connection()
    self.cursor = self.conn.cursor()
#################################3
  def _get_connection(self):
    return mysql.connector.connect(
      host=self.host,
      user=self.user,
      password=self.password_database,
      database=self.database
    )


  #### register

  def reg(self,name,password):
    enpass = self.encryptpass(password)
    print(len(str(enpass)))
    print(enpass)#### TODO fix encrypt 'b'
    # sql = "insert into users(id,name,score,level,passwords) values (1,'{0}',0,1,'{1}');".format(name,enpass)
    # self.cursor.execute(sql)
    # self.conn.commit()



  def login(self,username,password):
    users = self.selectusers()
    listuser = {}
    for item in users:
      if username == item[1] and password == item[4]:
        print('ok')
        id = str(item[0])
        name = str(item[1])
        scoreuser = str(item[2])
        leveluser = str(item[3])
        # listuser.append(id,name,scoreuser,leveluser)
        listuser.update({'name':name,'score':scoreuser,'level':leveluser})
        return listuser
      else:
        print("failed")

  ### show data
  def selectusers(self):
    sql = "select * from users;"
    self.cursor.execute(sql)
    myresult = self.cursor.fetchall()
    return myresult
    # for item in myresult:
    #   print(f'name =>{item[0]} password => {item[1]}')
    #   print('------')

  def showuserdata(self,username,password):
    data = self.login(username,password)
    return data

  # def savedata(self,name,newscore,newlevel):
  #   sql = "update users set score = '{0}' ,level = '{1}' where name = '{2}';".format(newscore,newlevel,name)
  #   self.cursor.execute(sql)
  #   self.conn.commit()

  def savedata(self,**kwargs):
    sql = "update users set score = '{0}' ,level = '{1}' where name = '{2}';".format(kwargs['newscore'],kwargs['newlevel'],kwargs['name'])
    self.cursor.execute(sql)
    self.conn.commit()


  def encryptpass(self,passwords):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(passwords.encode())
    return encMessage

  def decryptpass(self,passwords,key):
    pass

  def keypass(self):
    pass


u = users()
u.reg('test','p10')
# u.savedata(newscore=10,newlevel=2,name='ali')
# # # u.reg('alireza','4cfcbfd56')
# #
# # # u.selectusers()
# # print(u.showuserdata('alireza','456'))
# # # u.savedata('ali',12,2)
# u.reg('ali','aaa')