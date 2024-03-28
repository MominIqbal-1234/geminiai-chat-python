from GeminiAIChat.process import GET


class API:
    def __init__(self,api=None) -> None:
        self.api = api
        

    def prompt(self,prompt:str) -> None: ...
        
    def response(self) -> str: ...