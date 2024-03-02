#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv("data.xlsx - Sheet1.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.describe()


# In[6]:


import matplotlib.pyplot as plt


# In[7]:


import seaborn as sns


# **Univariate Analysis**

# In[8]:


numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns


# In[9]:


for col in numerical_columns:
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 3, 1)
    sns.histplot(df[col], kde=True)
    plt.title(f'Histogram of {col}')
    
    plt.subplot(1, 3, 2)
    sns.boxplot(y=df[col])
    plt.title(f'Boxplot of {col}')
    
    plt.subplot(1, 3, 3)
    sns.kdeplot(df[col], cumulative=True)
    plt.title(f'CDF of {col}')
    
    plt.tight_layout()
    plt.show()


# In[10]:


categorical_columns = df.select_dtypes(include=['object']).columns


# In[11]:


for col in categorical_columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(df[col])
    plt.title(f'Countplot of {col}')
    plt.xticks(rotation=45)
    plt.show()


# ****From these visualisations****<br>
# *Most of the salaries are between 100000 and 1000000.<br>
# *Most of the persons have around 90%.(left skewed distribution)<br>
# *most number of persons are graduate 12th in between 2007 and 2010<br>
# *The histogram plot of 12percentage is slightly leftskewed(very slight).most ofthe person have 70%on their 12th.<br>
# *most of the students are from tier 2 colleges.<br>
# *most of the students 70-80 CGPA on their college and they graduated in around 2000s.<be>

# **Bivariate Analysis**

# In[12]:


sns.pairplot(df[numerical_columns])
plt.show()

# Box plots for numerical and categorical columns
for num_col in numerical_columns:
    for cat_col in categorical_columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[cat_col], y=df[num_col])
        plt.title(f'Boxplot of {num_col} by {cat_col}')
        plt.xticks(rotation=45)
        plt.show()


# ****From These visualisations****<br>
# *Most of the students are joined in a company on 7-01-2014 and most ofthem are currently working on that company.<br>
# *Most of them are software engineer and most persons are work in Bangalore and the large number of trainees are male.<br>
# *The prsons have b-tech or B.E background<br>
# *most peoples are from electronics and communication engineering<br>
# *Most students are completed their graduation in Uttar Pradesh
# 

# **Research Questions**

# **1. Test the claim regarding salary expectations for fresh computer science engineering graduates**

# In[13]:


cse_graduates = df[df['Specialization'] == 'Computer Science Engineering']


# In[14]:


claimed_salary_range = (250000, 300000)
is_claimed = cse_graduates['Salary'].between(*claimed_salary_range).any()
print(f"Claimed Salary Range (INR): {claimed_salary_range}")
print(f"Does any Computer Science Engineering graduate fall within this range?: {'Yes' if is_claimed else 'No'}")


# **2. Explore the relationship between gender and specialization**

# In[15]:


# Countplot of Specialization by Gender
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Specialization', hue='Gender')
plt.title('Countplot of Specialization by Gender')
plt.xticks(rotation=45)
plt.show()


# In[16]:


# Count of Specialization by Gender
specialization_counts = df.groupby(['Specialization', 'Gender']).size().unstack(fill_value=0)
print("Count of Specialization by Gender:")
print(specialization_counts)


# **Conclusion**

# In conclusion, the exploratory data analysis (EDA) of the Aspiring Minds Employment Outcome 2015 (AMEO) dataset provided valuable insights into the employment outcomes of engineering graduates. Here are the key findings:
# 
# ****Salary Distribution****: The distribution of salaries among engineering graduates varied widely, with some graduates earning significantly higher salaries than others. Further analysis revealed factors such as specialization, college tier, and academic performance may influence salary levels.
# 
# ****Gender Disparit****: There appeared to be a gender disparity in employment outcomes, with males dominating certain specializations and job roles. Understanding and addressing this gender gap is essential for promoting diversity and inclusivity in the engineering workforce.
# 
# ****Skill Scores****: The dataset included standardized scores from various skill areas such as cognitive skills, technical skills, and personality traits. These scores could be further analyzed to understand their impact on employment outcomes and career trajectories.
# 
# ****Relationships Between Variables****: Bivariate analysis revealed interesting relationships between different variables. For example, there seemed to be correlations between academic performance (e.g., GPA, percentage scores) and job roles or salary levels.
# 
# The dataset was released by Aspiring Minds from the Aspiring Mind Employment Outcome 2015 (AMEO). The study is primarily limited only to students with engineering disciplines.So most of the students have b.tech background.Few students are completed their degree in tier-1 colleges.Most of the Students have 70-80% on their 12th and degree.Eventhough Most of them are earn high salary as other 90% above marked students.Females and males have no difference in getting their specialization.They do their Specialisation based on their passion.

# In[ ]:




