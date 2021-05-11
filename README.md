# Word Counter
This application is meant to take in a volume of text through a web form and will then return the number of words in the text that was submitted.

# Steps to Use
The main path through this application is the flask-app.py file, where a minimal Flask application is configured to run.

# Known Issues
	* There is no persistence of data within the application
	* The input field has no upper limit on the amount of text allowed.
	
# Development To-Do
	* Expand on Bootstrap utilization to add more visual interest to the site
	* Add additional validation checks to prevent possible security threats
	* Add a database layer to persist the words entered into the application
	* Transition Flask app into the cloud via Heroku or AWS
	* Shape the submitted word data structure to include more statistics about the text after submission
		* Display the most frequently used words in the submitted text
		* Display occurances of punctuation
		* Determine best way to visualize the data through Pandas
	
