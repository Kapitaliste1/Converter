import pandas as pd

# ios Files
en_iOS = pd.read_excel("en_iOS.xlsx")
es_iOS = pd.read_excel("es_iOS.xlsx")
fr_iOS = pd.read_excel("fr_iOS.xlsx")
pt_iOS = pd.read_excel("pt_iOS.xlsx")

#  android Files
eng_Android = pd.read_excel("eng_Android.xlsx")
es_Android = pd.read_excel("es_Android.xlsx")
fr_Android = pd.read_excel("fr_Android.xlsx")
pt_Android = pd.read_excel("pt_Android.xlsx")

# #  inner join drive Files
# inner_join_english = pd.read_excel("inner_join_english.xlsx")
# inner_join_french = pd.read_excel("inner_join_french.xlsx")
# inner_join_portuguees = pd.read_excel("inner_join_portuguees.xlsx")
# inner_join_spanish = pd.read_excel("inner_join_spanish.xlsx")




# Inner join
# inner_join_english = en_iOS.merge(eng_Android, how="inner", on="key")
# inner_join_english.to_excel("inner_join_english.xlsx")

# inner_join_spanish = es_iOS.merge(es_Android, how="inner", on="key")
# inner_join_spanish.to_excel("inner_join_spanish.xlsx")

# inner_join_french = fr_iOS.merge(fr_Android, how="inner", on="key")
# inner_join_french.to_excel("inner_join_french.xlsx")

# inner_join_portuguees = pt_iOS.merge(pt_Android, how="inner", on="key")
# inner_join_portuguees.to_excel("inner_join_portuguees.xlsx")



# outer join
outer_join_english = en_iOS.merge(eng_Android, how="outer", on="key")
outer_join_english.to_excel("outer_join_english.xlsx")

outer_join_spanish = es_iOS.merge(es_Android, how="outer", on="key")
outer_join_spanish.to_excel("outer_join_spanish.xlsx")

outer_join_french = fr_iOS.merge(fr_Android, how="outer", on="key")
outer_join_french.to_excel("outer_join_french.xlsx")

outer_join_portuguees = pt_iOS.merge(pt_Android, how="outer", on="key")
outer_join_portuguees.to_excel("outer_join_portuguees.xlsx")