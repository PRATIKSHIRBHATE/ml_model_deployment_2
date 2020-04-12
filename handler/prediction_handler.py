import json

from util_functions.prediction import predict_salary

def get_salary(event, context):
	"""
	"""
	input_features = event["body"]

	response = {
        "statusCode": 200,
        "body": predict_salary(input_features)
    }
	return response