# Log Alaysis - Udacity
### Full Stack Web Developer ND

_______________________________________________________________________________________________________________________

## About 
This is a Udacity Nanodegree project required for the Ful Stack NanoDegree program.  It parses a large Postgres database 
using python language.

It parses the database to answer the following questions using a single request query.
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time.
3. On which days did more than 1% of the requests lead to errors?

## Prerequisites
* Python 2.7 [https://www.python.org/downloads/release/python-2715/]
* Vagrant [https://www.vagrantup.com/]
* Oracle VM VirtualBox [https://www.virtualbox.org/]

This project implements the MVC pattern, it is built using python 2.7 and uses the library psycopg2.

## How to run

* Download zip file or clone the project using [https://github.com/rcarbal/Log-Analysis.git].
* Use Vagrant VM to run your virtual environment `vagrant up`.
* Once your virtual environment is up use `vagrant ssh`.
* Add the repo to the /vagrant directory in your environment.

#### Setup the database
* Download database from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
* add the files from above link to your project root.
* Use the following commands to setup database files.
    * `psql -d news -f newsdata.sql`
* To see the available tables ise the following command:
    * `\dt`
* Available tables:
    * Author, Articles, Log tables.


## Run Script
Use the following command on root to run the script.
* `python main.py`