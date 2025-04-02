## Setup Instructions

### 1. Install Dependencies
Use Poetry to install the required dependencies:
```bash
poetry install
```
### 2. Configure Environment Variable
Add your API key as an environment variable:
export API_KEY="your-api-key-here"


### 3. Update Email Configuration
Modify the email settings in the code:
```python
from_email = "your-email@example.com"
to_emails = ["recipient1@example.com", "recipient2@example.com"]
```

### 4. Verify Sender
Log into your SendGrid admin panel
Verify your sender identity
Ensure your sending email is authenticated

### 5. Run the Application
Execute the main script:
```bash
python main.py
```
