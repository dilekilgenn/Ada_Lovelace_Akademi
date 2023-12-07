
import pandas as pd
infected_dataset= pd.read_csv(r"C:\\Users\\90530\\Desktop\covid\time_series_covid19_confirmed_global (4).csv")
print(infected_dataset)

deaths_dataset= pd.read_csv(r"C:\\Users\\90530\\Desktop\covid\time_series_covid19_deaths_global.csv")
print(deaths_dataset)

recovered_dataset = pd.read_csv(r"C:\\Users\\90530\\Desktop\covid\time_series_covid19_recovered_global.csv")
print(recovered_dataset)

infected_dataset.index
print(infected_dataset.index)

infected_dataset.columns
print(infected_dataset.columns)

infected_dataset.info()
print(infected_dataset.info())

infected_dataset.describe()
print(infected_dataset.describe())

infected_dataset.size
print(infected_dataset.size)

infected_dataset.shape
print(infected_dataset.shape)

infected_dataset.iloc[5]
print(infected_dataset.iloc[5])

infected_dataset["Lat"]
print(infected_dataset["Lat"])

infected_dataset["Long"].to_frame()
print(infected_dataset["Long"].to_frame())

infected_dataset[["Lat", "Long"]]
print(infected_dataset[["Lat", "Long"]])

infected_dataset[1 :3]
print(infected_dataset[1 :3])

infected_dataset.loc["Lat": "Long"]
print(infected_dataset.loc["Lat": "Long"])

infected_dataset.loc[infected_dataset["Lat"] > 40]
print(infected_dataset.loc[infected_dataset["Lat"] > 40])

infected_dataset.drop(columns= ["Lat", "Long"])
print(infected_dataset.drop(columns= ["Lat", "Long"]))

infected_dataset[["Country/Region","Lat"]]
print(infected_dataset[["Country/Region","Lat"]])

infected_dataset[["Long","Lat"]] / 100
print(infected_dataset[["Long","Lat"]] / 100)

new_row = pd.Series({
    "Lat" : 830.000 ,
    "Long" : -15.5894 ,
    "Country/Region" : "Türkçe"
}, name = "Türkiyedeki covid")
print(new_row)
pd.concat([infected_dataset, new_row.to_frame().T], ignore_index= False )
print(pd.concat([infected_dataset, new_row.to_frame().T], ignore_index= False ))

deaths_dataset.head()
print(deaths_dataset.head()) # Varsayılan olarak dataframein ilk beş satırını çıktı olarak verir.


print(recovered_dataset)
print(type(recovered_dataset))
print(recovered_dataset.values)
print(recovered_dataset.columns)

recovered_dataset_ind = recovered_dataset.sort_values("Lat")
print(recovered_dataset_ind.head()) #sort_values metoduyla sütunları sıraladık head de ilk beş sütunu verdi.

recovered_dataset_count = recovered_dataset.sort_values("Lat", ascending= False)
print(recovered_dataset_count)
#Sütunlar azalan olarak sıralamya yararayn method

death_country= deaths_dataset[["Country/Region", "Lat"]]
print(death_country.head())









