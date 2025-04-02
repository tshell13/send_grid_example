import os

from send_grid import SendGrid

api_key = os.environ.get("API_KEY")

print(api_key)

html_content = """
<html>
  <body>
    <h2>Hello 👋 Vitali</h2>
    <p>This is a <strong>beautiful HTML email</strong> with an image:</p>
    <img src="https://external-preview.redd.it/Q_jQKTk88F6ouuVzLOQmP8wqp-1NuuxVNBf8MNVIAsI.jpg?auto=webp&s=95ef5a9553ef21cd0abac88859fd2e04179cb6bf" alt="Image" width="400" />
    <p>Best,<br>Tim</p>
  </body>
</html>
"""

subject = "From Hell"
from_email = "<>"
to_emails = ["<>", "<>"]

sg = SendGrid(api_key)
sg.send(html_content, subject, from_email, to_emails)