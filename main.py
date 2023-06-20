import pandas as pd
area = [11.8, 89.1, 7.1, 4.6]
color = ["Pink","Yellow", \
         "Blue","Purple"]
are_ser = pd.Series(area, index=color)
print(are_ser)


are_ser.name= "Area"
print(are_ser)
print( )


print(are_ser["Yellow"])
print( )
print(are_ser[["Yellow","Purple"]])
print( )
print(are_ser["Yellow": "Purple"])
print( )

print(are_ser.iloc[1])
print("&", are_ser.iloc[[1,3]])
print("&&", are_ser.iloc[1:4])
print("average area",are_ser.mean())
print("standard deviation area:", \
      are_ser.std())
print( )

are_ser["Black"] = 3.1
print(are_ser)
print(len(are_ser))
print(are_ser.shape)
print( )
are_ser2 = pd.Series(dtype=float)
print(are_ser2)
are_ser2["Black"] = 3.1
print(are_ser2)
print( )

are_data = [
    ["Pink",11.8,"Shallow"],
    ["Yellow",89.1,"Shallow"],
    ["Blue",7.1,"Medium"],
    ["Purple",3.1,"Deep"]
]
header = ["Color", "Area" ,"Depth"]
are_df = pd.DataFrame(are_data, columns=header)
print(are_df)

are_ser3 = are_df["Area"]
print(type(are_ser3))
print(are_ser3)

are_ser4 =are_df.iloc[:, 1]
print(are_ser4)
print(are_df.iloc[0, 1])
are_df = are_df.set_index("Color")
print(are_df)
print(are_df.loc["Pink"] ["Area"])

print(are_df["Area"] ["Pink"])

hue_df = pd.read_csv("hue.csv",
                     index_col=0)
print(hue_df)
print( )
merged_df = are_df.merge(hue_df,
                         on=["Color"],
                         how="outer")
print(merged_df)
merged_df.to_csv("merged.csv")

grouped_by_depth = merged_df.groupby("Depth")
mean_are_ser = grouped_by_depth["Area"].mean()
mean_are_ser.name = "Mean Area"
print(mean_are_ser)
print(mean_are_ser)
print( )

shallow_df =grouped_by_depth.get_group("Shallow")
print(shallow_df)
print( )
shallow_df2 = \
            merged_df[merged_df["Depth"]== "Shallow"]
print(shallow_df2)
print( )
print(merged_df["Depth"].value_counts())
print( )
merged_df =\
    merged_df.sort_values("Area",
                          ascending=False)
print(merged_df)
print( )
print(merged_df.isnull())
print( )
print(merged_df.isnull().sum())
print( )
print(merged_df.isnull().sum().sum())

