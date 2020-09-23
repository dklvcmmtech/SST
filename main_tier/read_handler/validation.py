from datetime import datetime, timezone


VALID_ARGS = ['pod','sDateTime','eDateTime']
TODAY = datetime.now(timezone.utc)
eDateTime = TODAY
sDateTime = eDateTime - datetime(24)
retDict = {}
SDATETIME = 'sDateTime'
EDATETIME = 'eDateTime'
FAILURE_STATUS = 'Failure'
def readValidation(args):
    if  SDATETIME not in VALID_ARGS or EDATETIME not in VALID_ARGS:
        return FAILURE_STATUS,""
    