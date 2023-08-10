Atlassian Jira Backup Robot
==============
### What does this robot do?

The main purpose of this process is to create backups of Siili Solutions internal Atlassian product site - Jira, in order to prevent data loss in case of system errors and similar events. A software robot generates the backups, downloads them, and transfers these packages to Siili's local directory, from where they can be restored to Atlassian more quickly when needed. 

First the robot retrieves information of the webpages to be opened in Stage0. In the first round (Stage1), the robot signs in to web page, creates a zip-compressed file from the company's Jira environment and closes the webpage. In the second round (Stage2), it signs in again, downloads and stores the file in the company's local directory. The progression of the robot is presented in detail in the thesis, https://urn.fi/URN:NBN:fi:amk-2023060521436, starting from section 4.3.

### Project structure


    .
    ├── libraries               # For implementing keywords that interact with target systems
    │   ├── ExcelLibrary.py
    │   ├── JiraLibrary.py
    │   ├── LibraryBase.py
    │   └── utils.py
    ├── pipelines               # Declarative-style Jenkins pipelines
    │   ├── Jenkinsfile
    │   └── process.groovy
    ├── resources    
    │   ├── locators.py                 # Configuration and other resources
    │   ├── settings.py
    │   ├── settings_helpers.py
    │   └── templates.py
    ├── scripts                 # Batch/shell cripts for running setup, tests and the process
    │   └── start.(cmd|sh)
    ├── stages                  # Robot workflow split into stages
    │   ├── Stage0.py
    │   ├── Stage1.py    
    │   └── Stage2.py
    ├── tasks                   # Robot Framework workflows
    │   └── main.robot
    ├── tests                   # Unit tests
    │   └── test_utils.py
    ├── venv
    ├── .env        
    ├── .gitignore
    ├── playwright-log.txt
    ├── requirements.txt
    ├── requirements-dev.txt
    ├── requirements-tests.txt
    ├── run.py
    ├── setup.cfg
    ├── setup.py
    ├── URLs.xlsx
    └── README.md

### Instructuons to connect to Slack

To generate and send a message to a Slack channel using Python, you need to use the Slack API. 
The easiest way to interact with the Slack API is to use the slack-sdk library. Here's a step-by-step guide on how to do this:

Install the slack-sdk library: pip install slack-sdk
Create a Slack App and get your API token:
Go to https://api.slack.com/apps and sign in to your Slack account.
Click on "Create New App" and give it a name and select your desired workspace.
Navigate to the "OAuth & Permissions" page under the "Features" section.
Add the "chat:write" scope under the "Bot Token Scopes" section.
Install your app to your workspace by clicking the "Install App" button in the "Install App" section.
Copy the "Bot User OAuth Token" (starts with xoxb-) and save it for later use.
Write Python code to send a message to Slack.
Run the script.
Keep in mind that the first time you run the script, you may need to invite the bot to the channel by typing @bot-name 
(replace with your bot's actual name) and then selecting "Invite to channel".
