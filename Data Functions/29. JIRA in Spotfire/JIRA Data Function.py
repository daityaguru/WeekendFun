print(time) #to make sure data function gets triggered by constantly changing input parameters {DateTimeNow()}
# import the installed Jira library
from jira import JIRA
# Import the required libraries
import requests
import pandas as pd

jiraOptions = {'server': "https://daityaguru.atlassian.net"} #Replace with your instance of JIRA

# Get a JIRA client instance, pass, Authentication parameters and the Server name.
# uname = your emailID & passwd = token you receive after registration
jira = JIRA(options=jiraOptions, basic_auth=(
	uname, passwd))
#uname and passwd are passed as input parameters

listAllIssues=[]
for singleIssue in jira.search_issues(jql_str='project = FUN'):
    listAllIssues.append([singleIssue.key, singleIssue.fields.summary,singleIssue.fields.reporter.displayName,singleIssue.fields.description])
    print('{}: {}:{}'.format(singleIssue.key, singleIssue.fields.summary,singleIssue.fields.reporter.displayName,singleIssue.fields.description))

dfIssues = pd.DataFrame(listAllIssues, columns=["Key","Summary","Reporter","Description"])

# Reframing the columns to get proper sequence in output.
columnTiles = ["Key", "Summary", "Reporter","Description"]
dfIssues = dfIssues.reindex(columns=columnTiles)
#print(dfIssues) # To debug, if required
