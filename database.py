import sqlalchemy
from sqlalchemy import create_engine, text
engine = create_engine("mysql+pymysql://root:Stromer@2003@localhost/testdb?charset=utf8mb4",
                       connect_args={
                           "ssl":{
                               
                           }
                       })
with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())