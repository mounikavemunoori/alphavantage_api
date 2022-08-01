# First create the virtualenv with python 3 version
virtualenv -p python3 env_name
# Activate the created virtualenv 
source env_name/bin/activate
# then install the requests package
pip install selenium
# install pytest package for running the test cases
pip install pytest
# install the pytest-html package to generate the test reports 
 pip install pytest-html

# I have used below link to generate our own api-key
https://www.alphavantage.co/support/#api-key

# Then copy the generated ap-key and paste in the test_data/alphavantage_data.config
path:-centime_api_automation/test_data
Example
[keys]
api_key_no_value=None
api_key='Here have to paste our own api-key which one we generated above step'

# Then go to the testcases folder
   cd centime_api_automation/test_data/testcases

# Then run the test script with below command
pytest -v test_alpha_vintage.py -s --html=reports/index.html







