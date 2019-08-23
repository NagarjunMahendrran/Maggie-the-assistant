import sys
from jira import JIRA

import sys, Tkinter

print("BUGID: "+sys.argv[1])
jira_options={'server': 'https://jira.technicolor.com'}
jira = JIRA(options=jira_options,basic_auth=('wipro_nagarjunm', 'X6BH9bJgHxLY'))
issue = jira.issue(sys.argv[1])
print("-------------------------------------------------------------------------")
print("|  Status      :"+ str(issue.fields.status))
print("|  Assinee     :"+ str(issue.fields.assignee.displayName))
print("|  Issue Type  :"+ str(issue.fields.issuetype.name))
print("|  Reporter    :"+ str(issue.fields.reporter.displayName))
print("-------------------------------------------------------------------------")


 
