class View:

    def print_parsed_data(self, data):
        print(data)

    def start_log_analisys(self):
        print("\nStarting Log Analysis\n")

    def finish_log_analisys(self):
        print("Log Anaysis_Ended")

    def print_top_articles(self, pop_articles):
        print("\nThe most popular articles off all time, are:")
        for index, article in enumerate(pop_articles):
            if index == 0:
                continue

            pos = article[0].index('/', article[0].index('/') + 1)
            print('\t"' + article[0][pos + 1:] + '" - {}'
                  .format(article[2]) + " views")

    def show_get_most_popular_author(self, pop_authors):
        print("\nThe most popular authors are:")
        for author in pop_authors:
            print('\t' + "{} - {} views".format(author[0], author[1]))

    def show_days_with_most_error(self, error):
        print('\nDays that had more than 1% erros:')
        for day in error:
            print('\t' + "{} {},{} - {}% errors".format(day[0].strftime("%B"),
                                                        day[0].strftime("%d"),
                                                        day[0].strftime("%Y"),
                                                        day[1]))
            print('\n\n')
