class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_log_analysis(self):
        self.view.start_log_analisys()

    def get_popular_articles(self):
        pop_articles = self.model.parse_top_articles()
        self.view.print_top_articles(pop_articles)

    def get_popular_authors(self):
        pop_authors = self.model.get_most_popular_author()
        self.view.show_get_most_popular_author(pop_authors)

    def get_days_of_errors(self):
        error_days = self.model.get_day_with_errors()
        self.view.show_days_with_most_error(error_days)
