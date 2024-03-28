from GeminiAIChat.process import GET

class API:
    def __init__(self,api=None) -> None:
        if api == None:
            raise ValueError("read doc get free api key \n  -> https://github.com/MominIqbal-1234/geminiai-chat-python")
        self.api = api
        self.getRes = GET(self.api)

    def prompt(self,prompt):
        self.getRes.sendResponse(prompt)
        
    def response(self):
        return self.getRes.retrieveShortResponse()

    def detailsResponse(self):
        return self.getRes.retrieveDetailResponse()
