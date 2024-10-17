import schedule

from database_connect import connect_db


def update_movies_table(data_movie_update):
    connection = connect_db()

    if connection:
        cursor = connection.cursor()

        try:
            cursor.fast_executemany = True
            insert_query = "INSERT INTO movies (id, adult, original_title, popularity, video) VALUES (?, ?, ?, ?, ?)"
            data_to_insert = [
                (
                    row["id"],
                    row["adult"],
                    row["original_title"],
                    row["popularity"],
                    row["video"],
                )
                for index, row in data_movie_update.iterrows()
            ]

            cursor.executemany(insert_query, data_to_insert)
            connection.commit()
            print("Données insérées avec succès dans la base de données.")
        except Exception as e:
            print(f"Erreur lors de l'insertion des données : {e}")
        finally:
            connection.close()
    else:
        print("Connexion à la base de données échouée.")

    schedule.every(30).days.do(update_movies_table)
