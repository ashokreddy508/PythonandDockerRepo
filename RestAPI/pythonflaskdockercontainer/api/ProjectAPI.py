from flask_restful import Resource
import logging as logger
import os
from dotenv import load_dotenv
load_dotenv()
class ProjectAPI(Resource):
    def get(self):
        logger.debug("Inside the post method of Task")
        #load_dotenv()
        projectDetails = {
                "version" : "1.0.0",
                "owner" : "Ashok",
                "service_name" : "myapplication",
                "service_port" : os.getenv('service_port'),
                "log_level" : os.getenv('log_level')
                }
        return projectDetails,200
