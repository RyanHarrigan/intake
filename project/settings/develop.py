import dj_database_url
from project.settings.environment import *

USE_DEBUG_TOOLBAR = False
DEBUG = False
ALLOWED_HOSTS = ['*']

# looks for 'DATABASE_URL' environmental variable
DATABASES = {
    'default': dj_database_url.config(),
    'purged': dj_database_url.config(),
}
CLIPS_DATABASE_ALIAS = 'purged'
# settings for file uploads
AWS_ACCESS_KEY_ID = os.environ.get('DEV_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('DEV_AWS_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('DEV_AWS_STORAGE_BUCKET_NAME')
AWS_MEDIA_BUCKET = os.environ.get('DEV_AWS_MEDIA_BUCKET')
LIVE_COUNTY_CHOICES = False

# use mailgun's REST API to validate email addresses
ALLOW_REQUESTS_TO_MAILGUN = True
