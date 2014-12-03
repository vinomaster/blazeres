#!/usr/bin/env python

from blaze import CSV, Table
csv = CSV('hmda_lar-2012.csv')  # Open the CSV file
t = Table(csv)                  # Interact with CSV file using interactive Table object

columns = ['action_taken_name', 'agency_abbr', 'applicant_ethnicity_name',
           'applicant_race_name_1', 'applicant_sex_name', 'county_name',
           'loan_purpose_name', 'state_abbr']

t = t[columns]

t2 = t[t.state_abbr == 'NY']

from blaze import into, by
from pandas import DataFrame
# Group on action_taken_name, count each group
print into(DataFrame, t2.action_taken_name.count_values())

from blaze import SQL
sql = SQL('sqlite:///hmda.db', 'data', schema=t.schema) # A SQLite database
into(sql, t)  # Migrate data

sqlTable = Table(sql)

from blaze import create_index
create_index(sql, 'state_abbr', name='state_abbr_index')

t2 = sqlTable[sqlTable.state_abbr == 'NY']

print into(DataFrame, t2.action_taken_name.count_values())
