# move some sensitive information into python variables so that it can be saved into our local code so everyone not able to see our info
# set python environment variables in windows 10 for python
# control panel->system and security->system->Advance system settings->Environment variables->user variables->new->set here u r info

import os  # to access the environment variables import os module i think this is one of use of OS module
# db_user = "raji"
# db_password = "raji_143"

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASS")

print(db_user)
print(db_password)
