from itertools import groupby
from macquisition import macquisition as mac
from mwrangling import mwrangling as mwr
from manalysis import manalysis as man

#primero creamos el data frame, que no se llame dataframe

input_year = int(input('Introduzca el año de fabricación: '))

group_by_var ='Make'

if__name__ == '__main__':
    df_raw = mac.acquisition('./data/vehicles.csv')
    df_wrangled = mwr.wrangling(df_raw, input_year)
    final_message = man.analysis(df_wrangled,'Make', 'Combined MPG')
    print(final_message)







