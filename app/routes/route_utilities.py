from flask import abort,make_response
from ..db import db

def validate_model(cls,model_id):
    try:
        model_id = int(model_id)
    except: 
        response = {"message": f"{model_id} is not valid"}
        abort(make_response(response, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        response = {"message": f"{model_id} is not found"}
        abort(make_response(response, 404))
    
    return model
