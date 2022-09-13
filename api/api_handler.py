from flask_restful import Api, Resource, reqparse

class api_handler(Resource):
    
  def get(self):
    return {
      'resultStatus': 'SUCCESS',
      'message': "Hello Api Handler"
      }
    
