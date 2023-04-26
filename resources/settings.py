"""
Configuration objects.
"""
import datetime
import importlib
import os
import platform

from resources.settings_helpers import (
    get_vars_from_config,
    import_variables_from_class,
    import_variables_from_module,
)
## try except
try:
    # create .env file at root to load the environment variables specified in ``ROBOT_DYNAMIC_VARIABLES``
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
except ModuleNotFoundError:
    pass

ROBOT_DYNAMIC_VARIABLES = (
    # Fill me with environment variable names that are mandatory for robot to operate
    "DB_CRED_USR",
    "DB_CRED_PSW",
    "JIRA_CRED_USR",
    "JIRA_CRED_PSW",
    "SLACK_BOT_TOKEN",
    "CONFLU_CRED_USR",
    "CONFLU_CRED_PSW",

)

DIRNAME = os.path.dirname(os.path.abspath(__file__))
PACKAGE_ROOT = os.path.abspath(os.path.join(DIRNAME, os.pardir))
PLATFORM = platform.system()
TODAY = datetime.datetime.now()


def get_variables(env):
    if env.lower() == "prod":
        robot_vars = get_vars_from_config(ProdConfig)
    elif env.lower() == "test":
        robot_vars = get_vars_from_config(TestConfig)
    else:
        robot_vars = get_vars_from_config(DevConfig)
    for k in ROBOT_DYNAMIC_VARIABLES:    
        robot_vars.update({k: os.environ.get(k)})
    return robot_vars


class Config:
    browser = "gc"
    templates = import_variables_from_module("resources.templates")

    db_server = "mongodb+srv://demorobot-dbxun.mongodb.net"
    db_port = 27017
    db_auth_source = "admin"
    db_name = "demorobot"
    download_path = os.path.join(PACKAGE_ROOT, "backups")


class DevConfig(Config):
    _env = "dev"

    db_server = "localhost"


class TestConfig(Config):
    _env = "test"


class ProdConfig(Config):
    _env = "prod"
