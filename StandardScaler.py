from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.select_dtypes(include=np.number))
df_scaled = pd.DataFrame(scaled_data, columns=df.select_dtypes(include=np.number).columns)
print(df_scaled.head())
