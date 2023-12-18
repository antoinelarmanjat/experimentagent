# experimentagent
experiment
app.py is a flask application with three endpoints:
/ redirects to index.html
/stamps is a "GET" REST API (should actually be a POST but...) to store a new stamp with name and value
/stamplist (should just be the GET version of /stamps but...) to show the list of all stamps

index.html is the frontend file

setup_database.py is a file to initiate the SQLite3 db
