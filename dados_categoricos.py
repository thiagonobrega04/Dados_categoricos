import pandas as pd

# Concept of Label Encoding
# Label Encoding maps categories to numbers ranging from 0 through N-1, where N represents the unique category count. It's beneficial for ordered data like "Small", "Medium", and "Large".

# To illustrate, here is a Python list of shirt sizes:

sizes = ["Small", "Medium", "Large"]

# Python's Pandas library can be used to assign 0 to "Small", 1 to "Medium", and 2 to "Large":

df = pd.DataFrame({
    'item_id': [1302, 1440, 1220, 2038, 1102],
    'sizes': ['Small', 'Medium', 'Large', 'Small', 'Medium']
})

size_mapping = {"Small": 0, "Medium": 1, "Large": 2}
df['sizes'] = df['sizes'].map(size_mapping)  # Apply mapping to the specified column
print(df)
'''Output:
   item_id  sizes
0     1302      0
1     1440      1
2     1220      2
3     2038      0
4     1102      1
'''

# Concept of One-Hot Encoding
# One-Hot Encoding creates additional columns for each category, placing a 1 for the appropriate category and 0s elsewhere. It's preferred for nominal data, where order doesn't matter, such as "Red", "Green", "Blue".

# You can perform one-hot encoding with Pandas' .get_dummies():

df = pd.DataFrame({
    'item_id': [1302, 1440, 1220, 2038, 1102],
    'colors': ['Red', 'Green', 'Blue', 'Red', 'Green']
})

df = pd.get_dummies(df, columns=['colors'])  # One-hot encode specified column
print(df)
'''Output:
   item_id  colors_Blue  colors_Green  colors_Red
0     1302        False         False        True
1     1440        False          True       False
2     1220         True         False       False
3     2038        False         False        True
4     1102        False          True       False
'''

# Why One-Hot Encoding?
# As One-Hot encoding converts each category value into a new column and assigns a 1 or 0 (True/False) value to the column, it does not impose any ordinal relationship among categories where there is none. This can often be the case with labels like 'Red', 'Blue', 'Green'. Each of these categories is distinct, and there is no order. Converting these label categories into a numerical format using label encoding would imply an order, while one-hot encoding does not. It could be helpful for training machine learning models.

# Categorical Data Encoding Pitfalls
# Finally, let's address the potential pitfalls of encoding. Label Encoding can create an unintended order, which may mislead our model. One-Hot Encoding can slow down our model when used with many unique categories. Consider merging select categories or using different encoding techniques to combat these issues.

# For instance, the 'Species' feature in an 'Animal Shelter' dataset can be restructured to address such problems. Instead of Label Encoding or One-Hot Encoding each unique species like 'Dog', 'Cat', 'Rabbit', and 'Bird', we can merge 'Dog' and 'Cat' into a new category 'Pet', and 'Rabbit' and 'Bird' into 'Other'. This technique reduces our feature's unique categories, making it more model-friendly.