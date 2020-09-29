from bs4 import BeautifulSoup
import pandas as pd
from requests import get
from time import sleep
from random import randint


def add_language_courses(language, url, df):
    """ Adds the courses to the data frame given the url to the courses.  """

    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    course_block_titles = html_soup.find_all('h4', class_='course-block__title')
    
    for course in course_block_titles:
        new_row = {'language':language, 'tech':course.text}
        df = df.append(new_row, ignore_index=True)

    return df

# Create an empty data frame
df = pd.DataFrame(columns=['language', 'tech'])

# Add all the R courses from Datacamp
df = add_language_courses("R", "https://datacamp.com/courses/tech:r", df)
# Add all the Python courses from Datacamp
df = add_language_courses("Python", "https://datacamp.com/courses/tech:python", df)

# Save the dataframe to csv
df.to_csv('courses.csv', index=False)
