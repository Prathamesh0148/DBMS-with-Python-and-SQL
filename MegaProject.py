#!/usr/bin/env python
# coding: utf-8

# In[192]:


get_ipython().system('pip install pypyodbc')


# In[193]:


import pyodbc as odbc
import numpy as np
import pandas as pd 
import sqlite3
import matplotlib.pyplot as plt



# In[194]:


Connection_string = (

        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=DESKTOP-HB0ANNM\SQLEXPRESS;'
        r'DATABASE=WorldUniversity;'
        r'Trusted_Connection=yes;'
        

)
Conn = odbc.connect(Connection_string)
print(Conn)


# In[ ]:





# In[195]:


from sqlalchemy.engine import URL
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": Connection_string})

from sqlalchemy import create_engine
engine = create_engine(connection_url)




# In[196]:


import sqlalchemy as sa

with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT TOP 10  * FROM Worldu"), conn)
    print(df)


# In[197]:


#1)Retrieve all columns for universities in the USA.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("Select * from Worldu"), conn)
    print(df)


# In[198]:


#2)Find the top 10 universities with the highest scores in 2012.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT top 10 * FROM Worldu where year=2012 ORDER BY score DESC  "), conn)
    print(df)



# In[199]:


#3)List universities in the United Kingdom with a score above 80 in 2013.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT institution from worldu where country='United Kingdom' and score>80 and year=2013 "), conn)
    print(df)


# In[200]:


#4)Count the number of universities in each country.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT country, count (institution) from worldu group by country "), conn)
    print(df)


# In[201]:


#5)	Calculate the average score for universities in each country in 2014.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT country, AVG (score) from worldu where year=2014 group by country "), conn)
    print(df)


# In[202]:


#6)	Find universities with a quality_of_education score greater than 20.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT institution from Worldu where quality_of_education>20 "), conn)
    print(df)


# In[203]:


#7)	Retrieve universities with a score between 70 and 80.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT institution from Worldu where score between 70 and 80 "), conn)
    print(df)


# In[204]:


#8)	List the top 5 universities with the highest alumni employment scores in 2012.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT  top 5 institution from Worldu where year=2012 Order by alumni_employment "), conn)
    print(df)


# In[205]:


#9)	Find the university with the highest quality_of_faculty in 2013.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT top 1 institution from Worldu where year=2013 order by quality_of_faculty DESC "), conn)
    print(df)


# In[206]:


#10)	Count the number of universities that have a national_rank less than 5.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT count (*) as institution from Worldu where national_rank < 5"), conn)
    print(df)


# In[207]:


#11)	Retrieve universities with a quality_of_education rank equal to 1.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT top 1 institution from Worldu  order by quality_of_education  DESC"), conn)
    print(df)


# In[208]:


#12)	List the top 10 universities with the highest citations in 2014.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT top 10 institution from Worldu where year=2014 order by citations DESC"), conn)
    print(df)


# In[209]:


#13)	Calculate the average influence score for universities in the USA.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT AVG(influence) as avg_influence FROM Worldu  WHERE country = 'USA'"), conn)
    print(df)


# In[210]:


#14)	Find universities with a broad_impact rank less than or equal to 50.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT institution, country, broad_impact from Worldu where broad_impact <= 50"), conn)
    print(df)


# In[211]:


#15)	Retrieve universities in Japan with a score greater than 60 in 2012.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT institution from Worldu where country='japan' and score> 60"), conn)
    print(df)


# In[212]:


#16)	List the top 5 universities with the highest patents in 2013.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT top 5 institution from Worldu where year=2013 order by patents DESC"), conn)
    print(df)


# In[213]:


#17)	Count the number of universities with a quality_of_faculty score between 5 and 10.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT count(institution) as COUN from Worldu where quality_of_faculty between 5 and 10"), conn)
    print(df)


# In[214]:


#18)	Calculate the average score for universities in the United Kingdom in 2014.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT  AVG(score) as AVGSCR  from Worldu where country='united kingdom' and year=2014"), conn)
    print(df)


# In[215]:


#19)	Find universities with a national_rank between 1 and 3 in 2012.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT  institution from Worldu where year=2012 and national_rank between 1 and 3"), conn)
    print(df)


# In[216]:


#20)	List universities with a citations rank less than 10.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("   SELECT Institution, country, citations FROM Worldu  WHERE citations < 10"), conn)
    print(df)


# In[217]:


#21)	Retrieve the university with the highest alumni_employment in 2013.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("   SELECT Institution, country FROM Worldu  WHERE year=2013 order by  alumni_employment DESC"), conn)
    print(df)


# In[218]:


#22)	Find the top 5 universities with the highest publications in 2012.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("   SELECT Top 5 Institution, country FROM Worldu  WHERE year=2012 order by publications DESC"), conn)
    print(df)


# In[219]:


#23)	Count the number of universities in each year.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("   SELECT count(institution), year from Worldu Group by year"), conn)
    print(df)


# In[220]:


#24)	Calculate the average alumni_employment score for universities in the USA.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT AVG(alumni_employment) as avgemployment FROM Worldu WHERE country ='USA'"), conn)
    print(df)


# In[221]:


#25)	Retrieve universities with a broad_impact score greater than 70.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT institution, country from Worldu where broad_impact > 70"), conn)
    print(df)


# In[222]:


#26)	List the top 10 universities with the highest influence in 2014.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT Top 10  institution, country from Worldu where year=2014 order by  influence DESC"), conn)
    print(df)


# In[223]:


#27)	Find universities with a patents rank equal to 1.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT   institution, country from Worldu where patents=1"), conn)
    print(df)


# In[224]:


#28)	Count the number of universities with a broad_impact between 20 and 30.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT COUNT(*) as num FROM Worldu WHERE broad_impact BETWEEN 20 AND 30"), conn)
    print(df)


# In[225]:


#29)	Calculate the average quality_of_faculty score for universities in the United Kingdom.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("  SELECT AVG(quality_of_faculty) FROM Worldu WHERE country = 'United Kingdom' "), conn)
    print(df)


# In[226]:


#30)	Find universities with an influence rank less than 5.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("  SELECT institution from Worldu where influence < 5"), conn)
    print(df)


# In[227]:


#31)	Retrieve universities with a score greater than 75 and a national_rank less than or equal to 10 in 2013.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT   institution, country from Worldu where score>70 and national_rank<=10 and year=2013"), conn)
    print(df)


# In[228]:


#32)	List the top 5 universities with the highest patents in 2014.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT Top 5 institution from Worldu where year=2014 Order by patents DESC"), conn)
    print(df)


# In[229]:


#33)	Count the number of universities with an alumni_employment score greater than 50.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT COUNT(institution) from Worldu where alumni_employment > 50"), conn)
    print(df)


# In[230]:


#34)	Calculate the average quality_of_education score for universities in Japan.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT AVG(quality_of_education) as QUALITYEDU FROM Worldu where country='japan'"), conn)
    print(df)


# In[231]:


#35)	Find universities with a quality_of_education rank equal to 1 in 2014.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT institution from Worldu where quality_of_education=1 and year=2014"), conn)
    print(df)


# In[232]:


#36)	Retrieve universities with a score greater than 80 and an alumni_employment rank less than 5.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT institution, country from Worldu where score>80 and alumni_employment<5"), conn)
    print(df)


# In[233]:


#37)	List the top 10 universities with the highest publications in 2013.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT top 10 Institution,publications FROM Worldu WHERE year=2013 ORDER BY publications DESC"), conn)
    print(df)


# In[234]:


#38)	Count the number of universities with a broad_impact score between 40 and 50.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT COUNT(institution) from Worldu where broad_impact between 40 and 50"), conn)
    print(df)


# In[235]:


#39)	Calculate the average score for universities in Australia.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT AVG(score) as AVGSCR from Worldu where country='Australia'"), conn)
    print(df)


# In[236]:


#40)	Find universities with an influence rank equal to 1 in 2012.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT institution from Worldu where influence=1 and year=2012"), conn)
    print(df)


# In[237]:


#41)	Retrieve universities with a quality_of_faculty score greater than 15.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT institution from Worldu where Quality_of_faculty>15"), conn)
    print(df)


# In[238]:


#42)	List the top 5 universities with the highest alumni_employment in 2014.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT top 5 institution from Worldu where year=2014 Order by alumni_employment DESC"), conn)
    print(df)


# In[239]:


#43)	Count the number of universities with a national_rank less than 20 in 2013.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT COUNT(institution) as cntinst from Worldu where national_rank<20 and year=2013"), conn)
    print(df)


# In[240]:


#44)	Calculate the average citations score for universities in Germany.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT AVG(citations) as AVGCIT from Worldu where country='Germany'"), conn)
    print(df)


# In[241]:


#45)	Find universities with a publications rank equal to 1.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT institution, country from Worldu where publications=1"), conn)
    print(df)


# In[242]:


#46)	Retrieve universities with a broad_impact score greater than 60 and a national_rank less than or equal to 5.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT institution, country from Worldu where broad_impact>60 and national_rank<=5"), conn)
    print(df)


# In[243]:


#47)	List the top 10 universities with the highest quality_of_education in 2012.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT TOP 10 institution from Worldu where year=2012 Order by quality_of_education DESC"), conn)
    print(df)


# In[244]:


#48)	Count the number of universities with a score greater than 90.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT Count(institution)as countt from Worldu where score>90"), conn)
    print(df)


# In[245]:


#49)	Calculate the average influence score for universities in the United Kingdom.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT AVG(influence) as avginf from Worldu where Country='United Kingdom'"), conn)
    print(df)


# In[246]:


#50)	Find universities with a quality_of_education rank less than or equal to 5 in 2014.
with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(" SELECT institution from Worldu where quality_of_education<=5 and year=2014"), conn)
    print(df)


# In[247]:


#TASK 5(using python)
#1)	What is the total number of records in the dataset?
data=pd.read_excel("D:\python projects\WorldUniversity.xlsx")
total_records = len(data)
print("Total number of records:", total_records)


# In[248]:


#2)	How many columns are there in the dataset?
df = pd.DataFrame(data)
column_names = list(df.columns)
num_columns = len(column_names)
print("Number of columns in the dataset:", num_columns)


# In[249]:


#3)	What is the datatype of the "world_rank" column?
Data_type = df["world_rank"].dtype
print("Datatype of the 'world_rank' column:", Data_type)


# In[250]:


#4)	Which country is represented the most in the dataset?
m_country = df["country"].value_counts().idxmax()
print("The country represented the most in the dataset is:", m_country)


# In[251]:


#5)	What is the average "quality_of_education" across all institutions?
AVG_education=df["quality_of_education"].mean()
print(AVG_education)


# In[252]:


#6)	Find the institution with the highest "alumni_employment" value.
MAX_AE = df["alumni_employment" ].idxmax
print(MAX_AE)


# In[253]:


#7)	In which year does the dataset end?
End_year = df["year"].max
("Ending year",End_year)


# In[254]:


#8)	How many unique countries are present in the dataset?
unique_countries = df["country"].nunique()
print("Number of unique countries in the dataset:", unique_countries)


# In[255]:


#9)	Which institution has the highest "score" in the year 2012?
df_2012 = df[df["year"] == 2012]

max_score_institution_2012 = df_2012.loc[df_2012["score"].idxmax()]["institution"]

print("The institution with the highest score in the year 2012 is:", max_score_institution_2012)


# In[256]:


#10)	What is the national rank of Harvard University in the year 2012?
harvard_2012 = df[(df["institution"] == "Harvard") & (df["year"] == 2012)]
harvard_national_rank_2012 = harvard_2012["national_rank"].values[0] if not harvard_2012.empty else None

print("The national rank of Harvard University in the year 2012 is:", harvard_national_rank_2012)


# In[257]:


#11)	Find the average "publications" value for institutions in the United Kingdom.
uk_institutions = df[df["country"] == "UK"]
average_publications_uk = uk_institutions["publications"].mean()

print( average_publications_uk)


# In[258]:


#12)	Identify the institution with the highest "influence" in the year 2013.
df_2013 = df[df['year'] == 2013]

highest_influence_2013 = df_2013[df_2013['influence'] == df_2013['influence'].max()]
print(highest_influence_2013[['institution', 'influence']])


# In[259]:


#13)	What is the minimum "broad_impact" value in the dataset?
min_impact = df["broad_impact"].min()
print("minimum broad impact",min_impact)


# In[260]:


#14)	How many institutions are from Japan in the year 2012?
insti_count= df[(df['year'] == 2012) & (df['country'] == 'Japan')]
num_insti_count = insti_count.shape[0]
print(num_insti_count)


# In[261]:


#15)	What is the average "patents" value for institutions in the USA in the year 2013?
usa_2013 = df[(df['year'] == 2013) & (df['country'] == 'USA')]
average_patents = usa_2013['patents'].mean()
print("Average patents value for institutions in the USA in 2013:", average_patents)


# In[262]:


#16)	Find the top 5 institutions with the highest "citations" in the year 2015.
df_2015 = df[df['year'] == 2015]
sorted_df = df_2015.sort_values(by='citations', ascending=False)

top_5_citations = sorted_df.head(5)

(top_5_citations[['institution', 'citations']])


# In[263]:


#17)	What is the median "international_students" percentage across all institutions?

#there is no column is there named as international_students


# In[264]:


#18)	Identify the institution with the lowest "income" in the year 2014.
#there is no column is there named as income


# In[265]:


#19)	How many missing values are there in the "total_score" column?
missing_values=df['score'].isnull().sum()
print(missing_values)


# In[266]:


#20)	Find the top 3 countries with the most institutions in the data
country_cnt=df['country'].value_counts()
top_3=country_cnt.head(3)
print(top_3)


# In[267]:


#21)	Calculate the percentage of institutions with a "research" score greater than 70.
high_score = df[df['score']>70]
percentage_h = (len(high_score) / len(df)) * 100
print(percentage_h)


# In[268]:


#22)	What is the difference in "teaching" score between MIT and Stanford University in 2016?
#data is not available


# In[269]:


#23)	How many institutions have a "world_rank" between 50 and 100 in the year 2011?
df_rank = df[(df['year'] == 2011) & (df['world_rank'] >= 50) & (df['world_rank'] <= 100)]
count_institutions = len(df_rank)
print(count_institutions)


# In[270]:


#24)	Find the country with the highest average "industry_income" across all years.
#no column name as industry income


# In[271]:


#25)	What is the standard deviation of "research" scores for institutions in the United States?
df_usa = df[df['country'] == 'USA']
standerd_dev = df_usa['score'].std()
print(standerd_dev)


# In[272]:


#26)	Identify the institution with the highest "alumni_employment" in the year 2015.
df_2015 = df[df['year'] == 2015]

highest_alumni = df_2015.loc[df_2015['alumni_employment'].idxmax()]['institution']

print(highest_alumni)


# In[273]:


#27)	Calculate the correlation between "score" and "research" across all years.
#research column not available


# In[274]:


#28)	How many institutions have a "broad_impact" greater than 800 in the year 2014?
filtered_df = df[(df['year'] == 2014) & (df['broad_impact'] > 800)]
num_institutions = len(filtered_df)
print("institution count is",num_institutions)


# In[275]:


#29)	Find the average "quality_of_eduacation" percentage for institutions in Australia.
country_aus = df[df['country']=='Australia']
avg_qual_edu=country_aus['quality_of_education'].mean()
print(avg_qual_edu)


# In[276]:


#30)	Identify the institution with the highest "total_score" in the year 2016.
df_2016 = df[df['year'] == 2016]

if not df_2016.empty:
    
    highest_total_score_institution = df_2016.loc[df_2016['total_score'].idxmax()]['institution']
    print(f"The institution with the highest 'total_score' in the year 2016 is: {highest_total_score_institution}")
else:
    print("No data available for the year 2016.")


# In[277]:


#31)	What is the percentage of missing values in the "female_male_ratio" column?
#data insufficiant


# In[278]:


#32)	How many institutions have a "score" greater than 90 in the year 2013?
high_score_2013 = df[(df['year'] == 2013) & (df['score'] > 90)].shape[0]

print(high_score_2013)


# In[279]:


#33)	Calculate the average "research" score for institutions in the top 10 of "total_score" in 2015.
top_10_2015 = df[df['year'] == 2015].nlargest(10, 'score')
average_top_10_2015 = top_10_2015['publications'].mean()

print(average_top_10_2015)


# In[ ]:





# In[280]:


#34)	Identify the institution with the lowest "international_students" percentage in the year 2012.
#no column is there in international_students


# In[281]:


#35)	What is the range of "influence" values in the dataset?
inf_range=df['influence'].max()-df['influence'].min()
print(inf_range)


# In[282]:


#36)	How many institutions have a "national_rank" of 1 in the year 2014?
count_rank_1_2014 = df[(df['year'] == 2014) & (df['national_rank'] == 1)].shape[0]

print(f"The number of institutions with a national rank of 1 in the year 2014 is: {count_rank_1_2014}")


# In[283]:


#37)	Find the country with the highest average "international_students" percentage.
#there is no column name as international_students


# In[284]:


#38)	Calculate the average "teaching" score for institutions in the top 5 of "world_rank" in 2016.
top_5_2016 = df[(df['year'] == 2016)].nlargest(5, 'world_rank')
average_teaching = top_5_2016['score'].mean()
print("The average teaching score is",average_teaching)


# In[285]:


#39)	Identify the institution with the highest "research" score in the year 2014.
#research not available


# In[286]:


#40)	How many institutions have a "world_rank" greater than 200 in the year 2015?
World_r=df[(df['year']==2015) & (df['world_rank']>200)]
(World_r)                                  


# In[287]:


#41)	What is the mode of the "country" column in the dataset?
mode_ctry=df['country'].mode()
print(mode_ctry)


# In[288]:


#42)	Identify the institution with the highest "industry_income" in the year 2011.
#industry income not available


# In[289]:


#43)	Calculate the average "citations" score for institutions in the bottom 10 of "world_rank" in 2013.
bottom_10 = df[(df['year'] == 2013)].nsmallest(10, 'world_rank')
average_bottom_10 = bottom_10['citations'].mean()

print(f"The average citations score for bottom 10",average_bottom_10)


# In[290]:


#44)	How many institutions have a "total_score" greater than 80 in the year 2016?
count_high_total_score_2016 = df[(df['year'] == 2016) & (df['score'] > 80)].shape[0]

print(count_high_total_score_2016)


# In[291]:


#45)	Find the country with the lowest average "score" across all years.
average_score = df.groupby('country')['score'].mean()
lowest_avg_score = average_score.idxmin()

print(f"The country with the lowest average 'score' across all years is: {lowest_avg_score}")


# In[292]:


#46)	Calculate the average "publications" percentage for institutions in the top 5 of "alumni_employment" in 2014.

top_5_alumni_employment_2014 = df[(df['year'] == 2014)].nlargest(5, 'alumni_employment')
average_international_students_top_5_2014 = top_5_alumni_employment_2014['publications'].mean()

print("The average publications percentage for institutions in the top 5 of alumni employment in 2014 is ",average_international_students_top_5_2014)


# In[293]:


#47)	Identify the institution with the lowest "quality_of_education" score in the year 2015.
lowest_quality_edu = df[df['year'] == 2015].nsmallest(1, 'quality_of_education')

# Print the institution with the lowest quality of education score in 2015
(lowest_quality_edu)


# In[294]:


#48)	How many missing values are there in the "research" column?
#no data available


# In[295]:


#49)	Find the average "female_male_ratio" for institutions in the United States.
#no column is there named as female_male_ratio


# In[296]:


#50)	What is the highest "influence" score in the dataset?
high_influence=df['influence'].max()
(high_influence)


# In[297]:


#task 6:
#visualization:
#1)	How can you use matplotlib to create a bar chart showing the top 10 universities by their scores in 2012?
top_10_2012 = df[df['year'] == 2012].nlargest(10, 'score')

plt.figure(figsize=(10, 6))
plt.bar(top_10_2012['institution'], top_10_2012['score'], color='lightgreen')
plt.xlabel('names of University')
plt.ylabel('Score')
plt.title('Top 10 Universities by Score in 2012')
plt.xticks(rotation=45) 
plt.tight_layout()

# Show the plot
plt.show()


# In[298]:


#2)	Create a line plot using seaborn to visualize the trend of scores for the University of Tokyo from 2012 to 2014.
import seaborn as sns
university_of_tokyo= df[(df['institution'] == 'University of Tokyo')] 
subset_years = [2012, 2013, 2014]
subset_data = university_of_tokyo[university_of_tokyo['year'].isin(subset_years)]

# Create a line plot using Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x='year', y='score', data=subset_data, marker='o', label='University of Tokyo')
plt.xlabel('Year')
plt.ylabel('Score')
plt.title('Scores for University of Tokyo (2012-2014)')
plt.show()


# In[299]:


#3)	How can you use Altair to create a scatter plot comparing the quality of faculty and alumni employment for all universities in 2013?
import altair as alt
data_13= df.loc[df['year']==2013]
alt.Chart(data_13).mark_circle(size = 50).encode(
    x='quality_of_faculty',
    y='alumni_employment',color='country').interactive()


# In[300]:


#4)	Using matplotlib, create a horizontal bar chart to display the top 10 universities in terms of influence in 2014.
data_14= df.loc[df['year']==2014]
influence_dt= data_14.nlargest(10,'influence')

inst= influence_dt['institution']
inf= influence_dt['influence']

plt.barh(inst,inf,color='grey')
plt.show()


# In[301]:


#5)	How can you use seaborn to create a boxplot for the distribution of scores among universities in 2012?
data_2012= df.loc[df['year'] == 2012]
sns.boxplot(x='score',data = data_2012,color='orange')
plt.show()


# In[302]:


#6)	Create a stacked area plot using Altair to represent the change in scores for the top 5 universities from 2012 to 2014.
change_scr = df.drop_duplicates()
top_5 = change_scr.nsmallest(5,'world_rank')

alt.Chart(top_5).mark_area().encode(
    x = 'year',
    y = 'score',
    color='institution:N'
).properties(width = 800,title = 'change in scores from 2012 to 2014')


# In[303]:


#7)	How can you use matplotlib to create a pie chart illustrating the distribution of universities in the United States and other countries in 2013?
pie_crt = data_13['country'].value_counts()
lbl = data_13['country'].drop_duplicates()

fig , piep = plt.subplots()
piep.pie(pie_crt,labeldistance = 1.1, radius = 2, labels = lbl)
plt.show()


# In[304]:


#8)	Using seaborn, create a violin plot to show the distribution of alumni employment scores among universities in 2014.
plt.figure(figsize=(10,8))
sns.violinplot(data = data_14 , x = 'alumni_employment',palette='viridis')
plt.title('Distribution of alumni employment score in 2014')
plt.xlabel('alumni employment score')
plt.show()


# In[305]:


#9)	How can you use Altair to create a bar chart for the top 10 universities with the highest scores in 2014?
srt= data_14.drop_duplicates()
top_data = srt.nlargest(10,'score')
alt.Chart(top_data,title= 'top 10 universities with high score in 2014').mark_bar(color = 'green').encode(
    x = 'institution',
    y = 'score'
).properties(width = 600 , height = 300 , padding ={"left":50 , "right":50,"top":40,"bottom":20})


# In[306]:


#10)	Create a scatter plot using matplotlib to visualize the correlation between the quality of education and the quality of faculty for all universities in 2012.
x= data_2012['quality_of_education']
y= data_2012['quality_of_faculty']

plt.figure(figsize=(10,6))
plt.scatter(x,y,s=20,color='lightgreen')
plt.xlabel('quality of education')
plt.ylabel('quality of faculty')
plt.title('correlation between quality of education and quality of faculty')
plt.show()


# In[307]:


#11)	How can you use seaborn to create a pair plot to visualize the relationships between the scores, influence, and citations for the top 10 universities in 2013?
top13= data_13.nsmallest(10,'world_rank')

cols = ['score' , 'influence' , 'citations']

sns.pairplot(top13[cols], height=2.5)
plt.suptitle('pair plot of scores,influence & citations', y = 1.02)
plt.show()


# In[308]:


#12)	Using Altair, create a bar chart to compare the scores of universities in the United States and the United Kingdom in 2014.
cntry_filt = data_14.loc[data_14['country'].isin(['USA','United kingdom'])]
clean_dt = cntry_filt.drop_duplicates()

alt.Chart(clean_dt, title = 'universities in USA and united kingdom ').mark_bar().encode(
    x= 'institution',
    y= 'score',
    color = 'country'
)


# In[309]:


#13)	How can you use matplotlib to create a stacked bar chart illustrating the distribution of universities in different countries in 2012?
country_counts = data_2012['country'].value_counts()

plt.figure(figsize=(10, 6))
country_counts.plot(kind='bar', stacked=True, color='skyblue')
plt.xlabel('Country')
plt.ylabel('Number of Universities')
plt.title('Distribution of Universities in Different Countries (2012)')
plt.xticks(rotation=45, ha='right') 
plt.tight_layout()

plt.show()


# In[310]:


#14)	Create a heatmap using seaborn to visualize the correlation matrix of the numerical columns in the dataset.
numerical_columns = df.select_dtypes(include=['float64', 'int64'])

correlation_matrix = numerical_columns.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()


# In[339]:


#15)	How can you use Altair to create a line chart showing the trend of scores for the top 5 universities in 2014?
top_5 = data_14.nsmallest(5, 'world_rank')

alt.Chart(top_5).mark_line(color='lightgrey').encode(
    x='institution:N',
    y=alt.Y("score:Q",scale=alt.Scale(domain=[40,130]))
).properties(title='University scores',width=500)



# In[329]:


#16)	Using matplotlib, create a bar chart to show the average scores for universities in each country in 2013.
average_scores = data_13.groupby('country')['score'].mean()

plt.figure(figsize=(12, 6))
average_scores.sort_values().plot(kind='bar', color='skyblue')
plt.xlabel('Country')
plt.ylabel('Average Score')
plt.title('Average Scores for Universities in Each Country (2013)')
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()

plt.show()


# In[336]:


#17)	How can you use seaborn to create a swarm plot to visualize the- distribution of scores among universities in 2014?
data_2014=data_14.nsmallest(25,'world_rank')
plt.figure(figsize=(20,6))
sns.swarmplot(size=5,x='institution', y='score', data=data_2014)
plt.xlabel('institution')
plt.ylabel('Score')
plt.title('Swarm Plot: Distribution of Scores Among Universities in 2014')
plt.xticks(rotation=45)  
plt.tight_layout()

plt.show()


# In[342]:


#18)	Create a treemap using Altair to represent the proportion of universities in each country in 2012.

import plotly.express as px
uni_country = data_2012['country'].value_counts().reset_index()
uni_country.columns = ['country', 'count']

fig = px.treemap(uni_country, path=['country'], values='count',
                 title=' Universities in Each Country (2012)',
                 color='count', color_continuous_scale='viridis')

fig.show()


# In[344]:


#19)	How can you use matplotlib to create a histogram showing the distribution of scores for all universities in 2014?
plt.figure(figsize=(10, 6))
plt.hist(data_14['score'], bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title(' Distribution of Scores for All Universities in 2014')
plt.tight_layout()

plt.show()


# In[351]:


#20)	Using Altair, create a bar chart to compare the influence scores of universities in Canada and Australia in 2013.

df_ca_au = df_2013[df_2013['country'].isin(['Canada', 'Australia'])]

bar_chart = alt.Chart(df_ca_au).mark_bar().encode(
    x='institution',
    y='influence',
    color='country'
).properties(
    title='Influence Scores of Universities in Canada and Australia (2013)'
)

bar_chart


# In[ ]:




