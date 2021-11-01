# Project_Sharks_Attacks
# Este es un proyecto en el que se realiza una limpieza del dataset de los ataques de los tiburones ( descargado desde el siguiente enlace: https://www.kaggle.com/teajay/global-shark-attacks)

# En la elaboración de este proyecto se han usado la librería pandas, seaborn y matplotlib
# Una vez descargado y hecho el estudio, se formulan las siguientes hipotesis:
# 1-Los tiburones atacan mas a los hombres que a las mujeres
# 2-Los ataques provocados son mas mortales
# 3-Hubo mas ataques despues del año 2000

# Para la realiación del estudio, lo primero que se hace es eliminar las columnas innecesarias y vacías. Una vez hecho eso, se hace lo mismo con las filas que sólo estén llenas de NaNs.

# Para la demostración de la primera hipótesis, se renombran los valores ya que los que venian con el dataset no servían. Posteriormente se crea un barplot con las columnas deseadas y se muestar el gráfico.

# La demostración de la segunda hipótesis es muy similar. Se seleccionan las columnas deseadas, se filtran los valores a unos más manejables y se construye un barplot.

# Por último, para la última hipótesis, se limpia y utiliza únicamente la columna que se refiere al año para formar un lineplot.

# La primera hipótesis resulta ser cierta, la segunda falsa y la tercera es cierta.