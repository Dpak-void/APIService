import connexion
from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir='./')

# Route to request data
@app.route('/api/getdata')
def index():
    data=[{
	    "name": "Harry Potter and the Order of the Phoenix",
	    "img": "https://bit.ly/2IcnSwz",
	    "summary": "Harry Potter and Dumbledore's warning about the return of Lord Voldemort is not heeded by the wizard authorities who, in turn, look to undermine Dumbledore's authority at Hogwarts and discredit Harry."
        }, {
	    "name": "The Lord of the Rings: The Fellowship of the Ring",
	    "img": "https://bit.ly/2tC1Lcg",
	    "summary": "A young hobbit, Frodo, who has found the One Ring that belongs to the Dark Lord Sauron, begins his journey with eight companions to Mount Doom, the only place where it can be destroyed."
        }, {
	    "name": "Avengers: Endgame",
	    "img": "https://bit.ly/2Pzczlb",
	    "summary": "Adrift in space with no food or water, Tony Stark sends a message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the remaining Avengers -- Thor, Black Widow, Captain America and Bruce Banner -- must figure out a way to bring back their vanquished allies for an epic showdown with Thanos -- the evil demigod who decimated the planet and the universe."
        }]
    return jsonify(data)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003, debug=True)