import pymysql

con = pymysql.connect(host='localhost', user='root', password='0000', db='newschema', charset='utf8')  # 한글처리 (charset = 'utf8')

cur = con.cursor()
dbinput = f"insert into newschema.chatting1(user_id, message) values('affdklfd', 'b')"
idon = f"select * from newschema.chatting1"

cur.execute(dbinput)
cur.execute(idon)

avg = cur.fetchall()
con.commit()

print(avg)