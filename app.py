from flask import Flask, request, jsonify, render_template
import requests
import json
import sqlite3
app = Flask(__name__)

@app.route('/')
def homepage():
    # Render the index.html page
    return render_template('index.html')

@app.route('/stamplist', methods=['GET'])
def stamplist():
  # Connect to the database
  conn = get_db_connection()
  cur = conn.cursor()
  # Query to fetch all stamps from the database
  cur.execute('SELECT * FROM stamps')
  # Fetch all results
  stamps = cur.fetchall()
  # Convert the results into a list of dicts
  stamps_list = [dict(stamp) for stamp in stamps]
  # Close the connection
  conn.close()
  # Return the results as JSON
  return jsonify(stamps_list)

def get_db_connection():
  conn = sqlite3.connect('stamps.db')
  conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
  return conn

@app.route('/stamps', methods=['GET'])
def stamps():
    # Get parameters from the request
    stampname = request.args.get('stampname')
    stampvalue = request.args.get('stampvalue')

    response={"StampName":stampname,"StampValue":stampvalue}

    # Insert into the database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO stamps (stampname, stampvalue) VALUES (?, ?)',
                (stampname, stampvalue))
    conn.commit()
    conn.close()
  
    # Return the response back to the client
    return jsonify(str(response))
  
def flask_app():
    return app


if __name__ == "__main__":
    app.run('0.0.0.0', port=5555,debug=True)

