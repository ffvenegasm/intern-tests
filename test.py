import pandas as pd
import re

def clean_dataframe(df):
    for col in df.columns:
        ''' Codigo original '''

        ''' Error: se intenta remover espacios vacíos en todas las columnas con str.strip(), pero
        no se chequea primero si la columna posee valores strings, numericos o nulos '''
        # df[col] = df[col].str.strip()

        ''' Error: se intenta substituir caracteres especiales con re.sub() incorrectamente, pues
        se aplica la función directamente a una serie de pandas (df[col]) en vez de a un string '''
        # df[col] = re.sub(r'\W+', '', df[col])

        ''' Esta parte es correcta, pues remplaza los valores nulos por strings vacíos '''
        # df[col].fillna('', inplace=True)

        
        ''' Código corregido '''

        ''' Verificamos si la columna es del tipo object (generalmente strings) '''
        if df[col].dtype == 'object':
            ''' Removemos espacios al inicio y al final con función original '''
            df[col] = df[col].str.strip()
            
            ''' Removemos caracteres especiales, usando función lambda para recorrer cada valor de
            la columna. Si no es nulo, aplicamos función original al string del valor '''
            df[col] = df[col].apply(lambda x: re.sub(r'\W+', '', str(x)) if pd.notnull(x) else x)

        ''' Reemplazamos valores nulos (NaN) con strings vacíos, como antes '''
        df[col].fillna('', inplace=True)

    return df


# Carga de datos
df = pd.read_csv('data/interns.csv')

# Testeo de la función
df_cleaned = clean_dataframe(df)

# Chequeo del resultados/errores
print(df_cleaned)

# Exportación de datos limpios a archivo Excel (post correción)
df_cleaned.to_excel('respuestas/felipe_test1.xlsx', index=False)
