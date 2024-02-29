# coding=utf-8
import logging

from flask import Flask, jsonify, make_response, request, render_template
from flask_cors import CORS, cross_origin
import os

from entities.entity import Session, engine, Base
from entities.rating import Rating, RatingSchema

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_ALLOW_HEADERS'] = "Content-Type"
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
logging.getLogger('flask_cors').level = logging.DEBUG


generate database schema
Base.metadata.create_all(engine)


@app.route('/')
def home():
    return render_template('index.html')

@cross_origin()
@app.route('/rating')
def get_ratings():
    session = Session()
    rating_objects = session.query(Rating).all()

    schema = RatingSchema(many = True)
    ratings = schema.dump(rating_objects)

    session.close()
    return jsonify(ratings)


@cross_origin()
@app.route('/rating', methods=['PUT'])
def put_rating():
    posted_rating = RatingSchema()\
        .load(request.get_json())
    
    print(posted_rating)
    rating = Rating(**posted_rating)

    session = Session()
    session.merge(rating)
    session.commit()

    new_rating = RatingSchema().dump(rating)
    session.close()
    return jsonify(new_rating), 201

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
