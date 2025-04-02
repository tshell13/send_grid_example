from sendgrid import SendGridAPIClient, Mail


class SendGrid:
    def __init__(self, api_key: str, ):
        self.__api_key = api_key
        self._sg = SendGridAPIClient(self.__api_key)


    def send(self, message: str, subject: str = None, from_email: str = None, to_emails: list[str] = None):
        message = Mail(
            from_email=from_email,
            to_emails=to_emails,
            subject=subject,
            html_content=message
        )


        try:

            response = self._sg.send(message)
            print(f'Status Code: {response.status_code}')
        except Exception as e:
            print(f'Error: {e}')