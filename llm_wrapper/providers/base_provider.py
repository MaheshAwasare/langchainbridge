from abc import ABC, abstractmethod

class BaseProvider(ABC):
    def __init__(self, api_key=None):
        self.api_key = api_key

    @abstractmethod
    def invoke(self, input_data):
        pass
