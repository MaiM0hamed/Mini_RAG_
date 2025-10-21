from enum import Enum

class ResponseSignal(Enum):
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"

from src.controllers.DataController import DataController
from src.controllers.ProjectController import ProjectController

class RequestSignal(Enum):
    CREATE = "CREATE"
    READ = "READ"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
