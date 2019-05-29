import psycopg2

DATABASE = "news"


class Model:

    def fake_parse_database(self):
        return "Not Really Parsed Data"

    def parse_top_articles(self):
        conn = psycopg2.connect(database=DATABASE)
        cursor = conn.cursor()
        cursor.execute("select path, status, count(*) as num from log where "
                       "status = '200 OK'"
                       " group by path, status order by num desc;")
        articles = cursor.fetchall()
        conn.close()
        return articles

    def get_most_popular_author(self):
        conn = psycopg2.connect(database=DATABASE)

        cursor = conn.cursor()
        cursor.execute(
            " SELECT name, count(*) as num FROM authors INNER JOIN articles ON"
            " (authors.id ="
            " articles.author)"
            "JOIN log ON"
            "(replace(log.path, '/article/','')) = slug GROUP BY "
            "name ORDER BY num DESC;")
        articles = cursor.fetchall()
        conn.close()
        return articles

    def get_day_with_errors(self):
        conn = psycopg2.connect(database=DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM
            (SELECT all_day_request.day,
            ROUND((CAST(bad_day_request.bad_request AS NUMERIC) /
            CAST(all_day_request.all_requests AS NUMERIC) * 100 ), 2)
            AS error_per FROM
            (SELECT date(time) AS day, COUNT(*) AS all_requests from log
            GROUP BY day)
            all_day_request
            JOIN
            (SELECT date(time) AS day, COUNT(*) AS bad_request from log
            WHERE status LIKE
            '%404%' GROUP BY day)  bad_day_request
            ON all_day_request.day = bad_day_request.day) AS product
            WHERE error_per >= 1.0;
            """)
        error = cursor.fetchall()
        conn.close()
        return error
