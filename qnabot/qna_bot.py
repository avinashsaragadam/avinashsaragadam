from botbuilder.core import TurnContext,ActivityHandler,MessageFactory
from botbuilder.ai.qna import QnAMaker,QnAMakerEndpoint


class QnaBot(ActivityHandler):
    def __init__(self):
       qna_endpoint = QnAMakerEndpoint("80f0134d-ce55-47e8-93ee-31b894687e1f","fd39c0bd-befd-49db-85c7-28cce3290744","https://avinashqna.azurewebsites.net/qnamaker")
       self.qna_maker = QnAMaker(qna_endpoint)

    async def on_message_activity(self,turn_context:TurnContext):
      response = await self.qna_maker.get_answers(turn_context)
      if response and len(response) > 0:
         await turn_context.send_activity(MessageFactory.text(response[0].answer))