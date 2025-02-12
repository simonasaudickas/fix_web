import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
engine = create_engine('postgresql://postgres:Svedas1983@localhost:5432/fixjob')

def get_products():
   with engine.connect() as conn:
      prods=pd.DataFrame(conn.execute(text("SELECT * FROM produktai_lt")).fetchall())


