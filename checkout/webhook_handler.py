from django import HttpResponse


class StripeWH_Handler:
    '''
    Handle Sytripe webhooks
    '''

    def __init__(self, request):
        self.reqest = request
    
    def handle_event(self, event):
        '''
        Handle a generic/unknown/unexpected webhook event
        '''

        return HttpResponse(
            content=f'Webhooj received: {event["type"]}',
            status=200
        )
