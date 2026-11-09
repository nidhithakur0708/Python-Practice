# Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

#Create Virtual env
# virtualenv env1
# virtualenv env2

# Get inside and import packages
# .\env1\Scripts\activate.bat
# pip install pandas
# pip install pyjoke
#pip freeze >requirements.txt

#Now get out of env1
# .\env1\Scripts\deactivate.bat
# .\env2\Scripts\activate.bat
# pip install -r requirements.txt
# This installs every package in the env1