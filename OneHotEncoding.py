from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse=False)
encoded_data = encoder.fit_transform(df[['columna_categorica']])
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out())
df = pd.concat([df, encoded_df], axis=1).drop(['columna_categorica'], axis=1)
print(df.head())
