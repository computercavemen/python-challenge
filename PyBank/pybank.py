#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


csvpath = os.path.join('Resources', 'budget_data.csv')
csvpath


# In[3]:


# Set Variables for loop & calculations
total_months = 0 
profits_losses = 0
previous_value = 0

# Establish a list to hold the changes between rows
unique_changes = []
months = []


# In[4]:


# Open & read the file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Skip the first line 
    csv_header = next(csvreader)
    
    # Loop through all the rows, count months, and total profits & losses 
    for row in csvreader: 
        total_months += 1
        profits_losses = profits_losses + int(row[1])
        months.append(row[0])
        
        # Set a condition for the first row without a previous total
        if row[0] == "Jan-2010":
            previous_value = (int(row[1]))

        # Otherwise substract the current value in column 2 from the previous value and add it to our list 
        else:  
            unique_changes.append(int(row[1]) - previous_value) 

        previous_value = (int(row[1]))

    print(unique_changes)

    # Total all the changes 
    sum_unique_changes = sum(unique_changes)

    # Average the changes 
    average_change = round(sum_unique_changes/(total_months - 1), 2)
    
    # Find greatest increase and decrease 
    max_increase = max(unique_changes)
    max_increase_index = unique_changes.index(max_increase)+1
    max_decrease = min(unique_changes)
    max_decrease_index = unique_changes.index(max_decrease)+1


# In[5]:


print("Financial Analysis\n")
print("--------------------\n")

print(f"Total Months: {total_months}")
print(f"Total: {profits_losses}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {months[max_increase_index]} ${max_increase}")
print(f"Greatest Decrease in Profits: {months[max_decrease_index]} ${max_decrease}")


# In[6]:


outfile = open ("pybank_output.txt", "w")


# In[7]:


outfile.write("Financial Analysis\n")
outfile.write("----------------\n")
outfile.write("Total Months:" + str(total_months)+"\n")
outfile.write("Average Change:" + str(average_change)+"\n")
outfile.write("Greatest Increase in Profits:" + (months[max_increase_index]) + " " + str(max_increase)+"\n")
outfile.write("Greatest Decrease in Profits:" + (months[max_decrease_index]) + str(max_decrease)+"\n")
outfile.close()


# In[ ]:




