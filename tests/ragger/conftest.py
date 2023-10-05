from ragger.conftest import configuration

###########################
### CONFIGURATION START ###
###########################

configuration.OPTIONAL.APP_DIR="target/nanosplus/release/"

#########################
### CONFIGURATION END ###
#########################

# Pull all features from the base ragger conftest using the overridden configuration
pytest_plugins = ("ragger.conftest.base_conftest", )