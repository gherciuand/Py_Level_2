import psycopg2


def executeSQL(sql):
    with psycopg2.connect("host=localhost dbname=To_Do user=postgres password=123") as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            if 'SELECT' in sql:
                return cur.fetchall()
