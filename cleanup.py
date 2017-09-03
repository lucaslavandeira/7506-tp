import pandas

df = pandas.read_csv("data/full_data.csv")
no_state = df[df['state_name'].isnull()]
no_state_capital = no_state.loc[no_state['place_with_parent_names'].str.contains('Capital Federal')]
no_state_sur = no_state.loc[no_state['place_with_parent_names'].str.contains('Zona Sur')]
no_state_norte = no_state.loc[no_state['place_with_parent_names'].str.contains('Zona Norte')]
no_state_oeste = no_state.loc[no_state['place_with_parent_names'].str.contains('Zona Oeste')]

propiedades = [no_state_capital, no_state_norte, no_state_sur, no_state_oeste]
pandas.concat(propiedades).to_csv("data_gba_no_state.csv")

zona_norte = df.loc[df['state_name'] == 'Bs.As. G.B.A. Zona Norte']
zona_sur = df.loc[df['state_name'] == 'Bs.As. G.B.A. Zona Sur']
zona_oeste = df.loc[df['state_name'] == 'Bs.As. G.B.A. Zona Oeste']
capital = df.loc[df['state_name'] == 'Capital Federal']

propiedades = [capital, zona_norte, zona_sur, zona_oeste]
pandas.concat(propiedades).to_csv("data_gba.csv")

data_gba = pandas.read_csv("data_gba.csv")
data_gba_no_state = pandas.read_csv("data_gba_no_state.csv")
propiedades = [data_gba, data_gba_no_state]
pandas.concat(propiedades).to_csv("data_gba_total.csv")

