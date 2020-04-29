import os
#Utility funtion to check if ENV_VAR key is defined and not Default
def is_default(key):
	try:
		env_var = os.environ.get(key)
		return env_var == "DefaultString" or env_var == -1 or env_var == "-1"  or env_var == None or env_var == "False"

	except:
		return True
# This is a list of valid fully-qualified domain names (FQDNs) for this server.
# The server will not permit write access to the server via any other
# hostnames. The first FQDN in the list will be treated as the preferred name.
#
# Example: ALLOWED_HOSTS = ['peering.example.com', 'peering.internal.local']
ALLOWED_HOSTS = ["*"]
if not is_default("ALLOWED_HOSTS"):
	ALLOWED_HOSTS =  os.environ.get("ALLOWED_HOSTS").split(',')

# Must be unique to each setup (CHANGE IT!).
if is_default("SECRET_KEY"):
	raise ValueError("SECRET_KEY could not be "+str(os.environ.get("SECRET_KEY")))
else:
	SECRET_KEY =  os.environ.get("SECRET_KEY")

# Base URL path if accessing Peering Manager within a directory.
BASE_PATH = ""
if not is_default("BASE_PATH"):
	BASE_PATH =  os.environ.get("BASE_PATH")

# Time zone to use for date.
TIME_ZONE = "Europe/Paris"
if not is_default("TIME_ZONE"):
	TIME_ZONE = os.environ.get("TIME_ZONE")

# Autonomous System number
MY_ASN = 64512
if not is_default("MY_ASN"):
	MY_ASN = os.environ.get("MY_ASN")
# PostgreSQL database configuration
DATABASE = {
    "NAME": "peering_manager",  # Database name
    "USER": "devbox",  # PostgreSQL username
    "PASSWORD": "devbox",  # PostgreSQL password
    "HOST": "localhost",  # Database server
    "PORT": "",  # Database port (leave blank for default)
}
if not is_default("DATABASE_NAME"):
	DATABASE['NAME'] = os.environ.get("DATABASE_NAME")
if not is_default("DATABASE_USER"):
        DATABASE['USER'] = os.environ.get("DATABASE_USER")
if not is_default("DATABASE_PASSWORD"):
        DATABASE['PASSWORD'] = os.environ.get("DATABASE_PASSWORD")
if not is_default("DATABASE_HOST"):
        DATABASE['HOST'] = os.environ.get("DATABASE_HOST")
if not is_default("DATABASE_PORT"):
        DATABASE['PORT'] = os.environ.get("DATABASE_PORT")

#Enable Verbose debug
if not is_default("DEBUG"):
        DEBUG = bool(os.environ.get("DEBUG"))
#The number of days to retain logged changes
if not is_default("CHANGELOG_RETENTION"):
        CHANGELOG_RETENTION = int(os.environ.get("CHANGELOG_RETENTION"))

#Setting this to True will permit only authenticated users to access Peering Manager. By default, anonymous users are permitted to access Peering Manager as read-only.
if not is_default("LOGIN_REQUIRED"):
        LOGIN_REQUIRED = bool(os.environ.get("LOGIN_REQUIRED"))
#Email setting
if not is_default("EMAIL_SERVER") and not is_default("EMAIL_PORT")  and not is_default("EMAIL_USERNAME") and not is_default("EMAIL_PASSWORD") and not is_default("EMAIL_TIMEOUT") and not is_default("EMAIL_FROM_ADDRESS") and not is_default("EMAIL_SUBJECT_PREFIX"):
	EMAIL = {
		"SERVER": os.environ.get("EMAIL_SERVER"),
		"PORT":  int(os.environ.get("EMAIL_PORT")),
		"USERNAME":  os.environ.get("EMAIL_USERNAME"),
		"PASSSWORD":  os.environ.get("EMAIL_PASSWORD"),
		"TIMEOUT":  int(os.environ.get("EMAIL_TIMEOUT")),
		"FROM_ADDRESS":  os.environ.get("FROM_ADDRESS"), 
		"SUBJECT_PREFIX": os.environ.get("SUBJECT_PREFIX"),
	}
#These settings are being used to authenticate to PeeringDB.
if not is_default("PEERINGDB_USERNAME"):
       PEERINGDB_USERNAME = os.environ.get("PEERINGDB_USERNAME")
if not is_default("PEERINGDB_PASSWORD"):
       PEERINGDB_PASSWORD = os.environ.get("PEERINGDB_PASSWORD")
#Peering Manager will use these credentials when authenticating to remote devices via the NAPALM library, if installed
if not is_default("NAPALM_USERNAME"):
       NAPALM_USERNAME = os.environ.get("NAPALM_USERNAME")
if not is_default("NAPALM_PASSWORD"):
       NAPALM_PASSWORD = os.environ.get("NAPALM_PASSWORD")

#A dictionary of optional arguments to pass to NAPALM when instantiating a network driver
if not is_default("NAPALM_ARGS"):
       NAPALM_ARGS = os.environ.get("NAPALM_ARGS").split(',')

#The amount of time (in seconds) to wait for NAPALM to connect to a device.
if not is_default("NAPALM_TIMEOUT"):
       NAPALM_TIMEOUT = int(os.environ.get("NAPALM_TIMEOUT"))

#Determine how many objects to display per page within each list of objects.
if not is_default("PAGINATE_COUNT"):
       PAGINATE_COUNT = int(os.environ.get("PAGINATE_COUNT"))
#The host that will be used by BGPQ3 to look for IRR objects.
if not is_default("BGPQ3_HOST"):
       BGPQ3_HOST = os.environ.get("BGPQ3_HOST")
#A list of comma separated sources from which we will accept IRR objects.
if not is_default("BGPQ3_SOURCES"):
       BGPQ3_SOURCES = os.environ.get("BGPQ3_SOURCES")
#A dictionary with two keys: ipv6 and ipv4. Each value must be a list of strings to pass to BGPQ3. No spaces are allowed inside strings. If a string has a space in it, it should be split into two distinct strings.
if not is_default("BGPQ3_ARGS"):
       BGPQ3_ARGS = os.environ.get("BGPQ3_ARGS")
#The NetBox API URL to which the queries must be sent to.
if not is_default("NETBOX_API"):
       NETBOX_API = os.environ.get("NETBOX_API")
#The API token registered in the NetBox instance to be used in queries.
if not is_default("NETBOX_API_TOKEN"):
       NETBOX_API_TOKEN = os.environ.get("NETBOX_API_TOKEN")
#The roles that devices must have in the NetBox instance that will be queried.
if not is_default("NETBOX_DEVICE_ROLES"):
       NETBOX_DEVICE_ROLES = os.environ.get("NETBOX_DEVICE_ROLES").split(',')
