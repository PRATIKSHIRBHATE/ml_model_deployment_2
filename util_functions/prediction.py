import numpy as np
import pickle
# import boto3


"""
# Incase the model is stored on AWS
def get_model():
    bucket= boto3.resource('s3').Bucket('pratikshirbhate')
    bucket.download_file('ml_models/model.pkl','/tmp/model.pkl')
    model= pickle.load(open('/tmp/test_model.pkl')
    return model
"""
model = pickle.load(open('ml_models/model.pkl', 'rb'))

def predict_salary(input_list):
    '''
    This function takes list of numeric values which are input features for the model
    '''
    features = [np.float(x) for x in input_list]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = round(prediction[0])
    # print('Fixed Per Month Employee Salary should be Rs {} /-'.format(output))

    return output
