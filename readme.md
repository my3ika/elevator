#### To run the server, run this command from your terminal of choice:
<p><samp>python3 ./my_server.py


#### To call the APIs, use the following syntax.

##### A person requests an elevator be sent to their current floor
<p><samp>curl -s -X POST 'http://0.0.0.0:8080/floor/5/call'

##### A person requests that they be brought to a floor
<p><samp>curl -s -X POST 'http://0.0.0.0:8080/elevator/goto/5'

##### An elevator car requests all floors that it’s current passengers are servicing (e.g. to light up the buttons that show which floors the car is going to)
<p><samp>curl -s -X GET 'http://0.0.0.0:8080/floor/requested'

##### An elevator car requests the next floor it needs to service
<p><samp>curl -s -X GET 'http://0.0.0.0:8080/floor/next'
