#!/usr/bin/env python2.7

from parse_database import modelparser
from parse_database import parsercontroller
from parse_database import viewparser


def start():
    controller = parsercontroller.Controller(model, view)
    controller.start_log_analysis()
    controller.get_popular_articles()
    controller.get_popular_authors()
    controller.get_days_of_errors()


if __name__ == '__main__':
    view = viewparser.View()
    model = modelparser.Model()
    start()

