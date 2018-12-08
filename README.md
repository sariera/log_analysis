# Logs Analysis Project

> Ali Sariera

## Project Description

This project is a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool answers the following questions:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## How To Run:

### PreRequisites:
- Python2
- Vagrant
- VirtualBox

### Setup
1. Install Vagrant And VirtualBox
2. Clone this repository

### To Run

Launch Vagrant VM by running 'vagrant up', you can the log in with 'vagrant ssh'

To load the data, use the command 'psql -d news -f newsdata.sql' to connect a database and run the necessary SQL statements.

The database includes three tables:
- Authors table
- Articles table
- Log table

To execute the program, run 'python data.py' from the command line.