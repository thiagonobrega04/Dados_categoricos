import pandas as pd

# data = {
#     'Type': ['Shirt', 'Pants', 'Dress', 'Pants', 'Shirt'],
#     'Size': ['Large', 'Medium', 'Small', 'Large', 'Medium']
# }

# df = pd.DataFrame(data)

# df_encoded = pd.get_dummies(df, columns=['Type'])

# # Manually encode the 'Size' column.
# size_to_num = {'Small': 0, 'Medium': 1, 'Large': 2}
# df_encoded['Size'] = df_encoded['Size'].map(size_to_num)

# print(df_encoded)

# data = {'ClothingType': ['T-shirt', 'Jeans', 'Sweater', 'T-shirt', 'Sweater'],
#         'Size': ['L', 'M', 'S', 'M', 'L']}

# df = pd.DataFrame(data)

# # Use label encoding for Size. Remember: S < M < L
# size_mapping = {'S': 1, 'M': 2, 'L': 3}
# df['Size'] = df['Size'].map(size_mapping)

# # Use label encoding for ClothingType
# clothing_dict = {'T-shirt': 1, 'Jeans': 2, 'Sweater': 3}
# df['ClothingType'] = df['ClothingType'].map(clothing_dict)

# print(df)

# inventory = pd.DataFrame({
#     'item_id': [1000, 2000, 3000, 4000, 5000],
#     'size': ['L', 'M', 'S', 'M', 'L'],
#     'color': ['Blue', 'Red', 'Blue', 'Green', 'Purple']
# })

# size_mapping = {'S': 0, 'M': 1, 'L': 2}
# inventory['size'] = inventory['size'].map(size_mapping)

# inventory = pd.get_dummies(inventory, columns=['color'])

# print(inventory)

# inventory = pd.DataFrame({
#     'item_id': [101, 102, 103, 104, 105],
#     'sizes': ['XS', 'S', 'M', 'L', 'XL']
# })

# # TODO: Create a mapping for sizes where XS is 0, S is 1, M is 2, L is 3, and XL is 4.
# size_mapping = {'XS': 0, 'S': 1, 'M': 2, 'L': 3, 'XL': 4}

# # TODO: Replace the sizes with their corresponding numerical values using the map() function.
# inventory['sizes'] = inventory['sizes'].map(size_mapping)

# print(inventory)

# TODO: Create an inventory DataFrame containing item_id, category, size, and color.
inventory = pd.DataFrame({
    'item_id': [100, 200, 300, 400, 500],
    'category': ['Shirts','Trousers','Shirts','Jackets','Hats'],
    'size' : ['S','M','L','M','XL'],
    'color' : ['Black','White', 'Black','Brown','Yellow']
})

# TODO: Apply Label Encoding to size.
size_mapping = {'S': 1, 'M': 2, 'L': 3, 'XL': 4}
inventory['size'] = inventory['size'].map(size_mapping)

# TODO: Apply One-Hot Encoding to color.
inventory = pd.get_dummies(inventory, columns=['color'])

# Convert the columns of 0s and 1s to integers
inventory = inventory.astype({col: int for col in inventory.columns if col.startswith('color')})

# TODO: Print out your final DataFrame.
print(inventory)


