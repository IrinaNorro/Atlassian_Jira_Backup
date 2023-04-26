Robot Template
==============

### Project structure

The project should adhere to the below folder structure. Folders should only contain files of the denoted type(s), following the naming conventions.

    .
    ├── libraries               # For implementing keywords that interact with target systems
    │   ├── SystemALibrary.py
    │   ├── SystemBLibrary.py
    │   └── utils.py
    |
    ├── resources               # Configuration and other resources
    │   ├── settings.py
    │   ├── settings_helpers.py
    │   └── locators.py
    ├── scripts                 # Batch/shell cripts for running setup, tests and the process
    │   └── start.(cmd|sh)
    ├── stages                  # Robot workflow split into stages
    │   ├── Stage0.py
    │   └── StageN.py
    ├── tasks                   # Robot Framework workflows
    │   └── main.robot
    ├── tests                   # Unit tests
    │   └── test.py
    ├── .gitignore
    ├── .pylintrc
    ├── .rflintargs
    ├── requirements.txt
    ├── requirements-dev.txt
    ├── requirements-tests.txt
    ├── run.py
    ├── setup.cfg
    ├── setup.py
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
