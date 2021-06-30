#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv


# In[3]:


csvpath = os.path.join('Resources','election_data.csv')
csvpath


# In[4]:


# Set Variables for loop & calculations
total_votes_cast = 0 
candidates = []
khan = 0 
correy = 0 
li = 0 
otooley = 0


# In[5]:


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Skip the first line 
    csv_header = next(csvreader)
    
    # Loop through all the rows, count months, and total profits & losses 
    for row in csvreader: 
        total_votes_cast += 1
        if row[2] not in candidates: 
            candidates.append(row[2])
        if "Khan" in row[2]:
            khan += 1
        if "Correy" in row[2]:
            correy += 1
        if "Li" in row[2]:
            li += 1
        if "O'Tooley" in row[2]:
            otooley += 1


# In[6]:


# Percentage calculations
khan_percentage = "{:.0%}".format(khan/total_votes_cast)
correy_percentage = "{:.0%}".format(correy/total_votes_cast)
li_percentage = "{:.0%}".format(li/total_votes_cast)
otooley_percentage = "{:.0%}".format(otooley/total_votes_cast)


# In[7]:


print("Election Results")
print("----------------")
print(f"Total votes: {total_votes_cast}")
print("----------------")
print(f"Khan: {khan} ({khan_percentage})")
print(f"Correy: {correy} ({correy_percentage})")
print(f"Li: {li} ({li_percentage})")
print(f"O'Tooley: {otooley} ({otooley_percentage})")
print("----------------")
print("Winner: Khan")
print("----------------")


# In[8]:


outfile = open ("pypoll_output.txt", "w")


# In[9]:


outfile.write("Election Results\n")
outfile.write ("------------------------\n")
outfile.write ("Total votes: " + str(total_votes_cast) + "\n")
outfile.write ("Khan: " + str(khan) + " " + str(khan_percentage) + "\n")
outfile.write ("Correy: " + str(correy) + " " + str(correy_percentage) + "\n")
outfile.write ("Li: " + str(li) + " " + str(li_percentage) + "\n")
outfile.write ("O'Tooley: " + str(otooley) + " " + str(otooley_percentage) + "\n")
outfile.close()


# In[ ]:




