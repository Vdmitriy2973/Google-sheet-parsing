import pandas

googlesheetid = "1e_NGOcSSCu3s3EnCmiNDEn_sU-YR3ZIb_6uoW8odOHU"
worksheet = "Test"

url = "https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}".format(
    googlesheetid,
    worksheet
)

data = pandas.read_csv(url)
df = pandas.DataFrame(data)
print(data)   