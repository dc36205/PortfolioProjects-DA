#!/usr/bin/env python
# coding: utf-8

# # Hola Daniel! <a class="tocSkip"></a>
# 
# Mi nombre es Oscar Flores y tengo el gusto de revisar tu proyecto. Si tienes algún comentario que quieras agregar en tus respuestas te puedes referir a mi como Oscar, no hay problema que me trates de tú.
# 
# Si veo un error en la primera revisión solamente lo señalaré y dejaré que tú encuentres de qué se trata y cómo arreglarlo. Debo prepararte para que te desempeñes como especialista en Data, en un trabajo real, el responsable a cargo tuyo hará lo mismo. Si aún tienes dificultades para resolver esta tarea, te daré indicaciones más precisas en una siguiente iteración.
# 
# Te dejaré mis comentarios más abajo - **por favor, no los muevas, modifiques o borres**
# 
# Comenzaré mis comentarios con un resumen de los puntos que están bien, aquellos que debes corregir y aquellos que puedes mejorar. Luego deberás revisar todo el notebook para leer mis comentarios, los cuales estarán en rectángulos de color verde, amarillo o rojo como siguen:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
#     
# Muy bien! Toda la respuesta fue lograda satisfactoriamente.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Existen detalles a mejorar. Existen recomendaciones.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Se necesitan correcciones en el bloque. El trabajo no puede ser aceptado con comentarios en rojo sin solucionar.
# </div>
# 
# Cualquier comentario que quieras agregar entre iteraciones de revisión lo puedes hacer de la siguiente manera:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta estudiante.</b> <a class="tocSkip"></a>
# </div>
# 

# ## Resumen de la revisión 1 <a class="tocSkip"></a>

# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Hola, debes corregir el cálculo de la tarifa. Las duraciones de llamadas deben ser aproximadas individualmente y el uso de internet debe ser agrupado en el uso mensual por usuario. Corrige esto y seguiré con la revisión.
#     
# Saludos!    
# </div>

# ## Resumen de la revisión 2 <a class="tocSkip"></a>

# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Muy bien con los avances! Lo único que falta de la primera parte es calcular correctamente los gb de consumo, estos se deben aproximar hacia arriba, no redondear. Para la parte final, nota que debes hacer primero el test de levene y, según el resultado, aplicar igualdad de varianza o no. Dejé comentarios más detallados en esa parte.
#     
# Saludos!    
# 
# </div>

# ## Resumen de la revisión 3 <a class="tocSkip"></a>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v3</b> <a class="tocSkip"></a>
# 
# Buen trabajo Daniel! Has completado todo lo requerido para tu notebook, está aprobado.
#     
# Saludos!    
# 
# </div>

# ----

# # ¿Cuál es la mejor tarifa?
# 
# Trabajas como analista para el operador de telecomunicaciones Megaline. La empresa ofrece a sus clientes dos tarifas de prepago, Surf y Ultimate. El departamento comercial quiere saber cuál de las tarifas genera más ingresos para poder ajustar el presupuesto de publicidad.
# 
# Vas a realizar un análisis preliminar de las tarifas basado en una selección de clientes relativamente pequeña. Tendrás los datos de 500 clientes de Megaline: quiénes son los clientes, de dónde son, qué tarifa usan, así como la cantidad de llamadas que hicieron y los mensajes de texto que enviaron en 2018. Tu trabajo es analizar el comportamiento de los clientes y determinar qué tarifa de prepago genera más ingresos.

# [Te proporcionamos algunos comentarios para orientarte mientras completas este proyecto. Pero debes asegurarte de eliminar todos los comentarios entre corchetes antes de entregar tu proyecto.]
# 
# [Antes de sumergirte en el análisis de datos, explica por tu propia cuenta el propósito del proyecto y las acciones que planeas realizar.]
# 
# [Ten en cuenta que estudiar, modificar y analizar datos es un proceso iterativo. Es normal volver a los pasos anteriores y corregirlos/ampliarlos para permitir nuevos pasos.]

# ## Inicialización

# In[375]:


# Cargar todas las librerías

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import scipy.stats as st

import matplotlib.pyplot as plt
from importlib import reload
plt=reload(plt)


# ## Cargar datos

# In[376]:


# Carga los archivos de datos en diferentes DataFrames

df_megaline_calls = pd.read_csv('/datasets/megaline_calls.csv')
df_megaline_internet = pd.read_csv('/datasets/megaline_internet.csv')
df_megaline_messages = pd.read_csv('/datasets/megaline_messages.csv')
df_megaline_plans = pd.read_csv('/datasets/megaline_plans.csv')
df_megaline_users = pd.read_csv('/datasets/megaline_users.csv')


# ## Preparar los datos
 
# [Los datos para este proyecto se dividen en varias tablas. Explora cada una para tener una comprensión inicial de los datos. Si es necesario, haz las correcciones requeridas en cada tabla.]

# ## Tarifas

# In[377]:


# Imprime la información general/resumida sobre el DataFrame de las tarifas

df_megaline_plans.info()
df_megaline_plans.shape


# In[378]:


# Imprime una muestra de los datos para las tarifas

df_megaline_plans.head(5)


# [Describe lo que ves y observas en la información general y en la muestra de datos impresa para el precio de datos anterior. ¿Hay algún problema (tipos de datos no adecuados, datos ausentes, etc.) que pudieran necesitar investigación y cambios adicionales? ¿Cómo se puede arreglar?]

# ## Corregir datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[ ]:





# ## Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[ ]:





# ## Usuarios/as

# In[379]:


# Imprime la información general/resumida sobre el DataFrame de usuarios

df_megaline_users.info()


# In[380]:


# Imprime una muestra de datos para usuarios
df_megaline_users.head(5)


# [Describe lo que ves y observas en la información general y en la muestra de datos impresa para el precio de datos anterior. ¿Hay algún problema (tipos de datos no adecuados, datos ausentes, etc.) que pudieran necesitar investigación y cambios adicionales? ¿Cómo se puede arreglar?]

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[381]:


df_megaline_users['churn_date'] = pd.to_datetime(df_megaline_users['churn_date'])


# ### Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[382]:


df_megaline_users.info()


# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto
# </div>

# ## Llamadas

# In[383]:


# Imprime la información general/resumida sobre el DataFrame de las llamadas

df_megaline_calls.info()


# In[384]:


# Imprime una muestra de datos para las llamadas

df_megaline_calls.head(5)


# [Describe lo que ves y observas en la información general y en la muestra de datos impresa para el precio de datos anterior. ¿Hay algún problema (tipos de datos no adecuados, datos ausentes, etc.) que pudieran necesitar investigación y cambios adicionales? ¿Cómo se puede arreglar?]

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[385]:


df_megaline_calls['call_date'] = pd.to_datetime(df_megaline_calls['call_date'])
df_megaline_calls.info()


# ### Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[ ]:





# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto, aunque en esta parte también se podría haber obtenido la duración de llamadas que se usará para el cálculo de tarifas
# </div>

# ## Mensajes

# In[386]:


# Imprime la información general/resumida sobre el DataFrame de los mensajes

df_megaline_messages.info()


# In[387]:


# Imprime una muestra de datos para los mensajes

df_megaline_messages.head(5)


# [Describe lo que ves y observas en la información general y en la muestra de datos impresa para el precio de datos anterior. ¿Hay algún problema (tipos de datos no adecuados, datos ausentes, etc.) que pudieran necesitar investigación y cambios adicionales? ¿Cómo se puede arreglar?]

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[388]:


df_megaline_messages['message_date'] = pd.to_datetime(df_megaline_messages['message_date'])
df_megaline_messages.info()


# ### Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[ ]:





# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto
# </div>

# ## Internet

# In[389]:


# Imprime la información general/resumida sobre el DataFrame de internet

df_megaline_internet.info()


# In[390]:


# Imprime una muestra de datos para el tráfico de internet

df_megaline_internet.head(5)


# [Describe lo que ves y observas en la información general y en la muestra de datos impresa para el precio de datos anterior. ¿Hay algún problema (tipos de datos no adecuados, datos ausentes, etc.) que pudieran necesitar investigación y cambios adicionales? ¿Cómo se puede arreglar?]

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[391]:


df_megaline_internet['session_date'] = pd.to_datetime(df_megaline_internet['session_date'])
df_megaline_internet.info()


# ### Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[ ]:





# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto
# </div>

# ## Estudiar las condiciones de las tarifas

# [Es sumamente importante entender cómo funcionan las tarifas, cómo se les cobra a los usuarios en función de su plan de suscripción. Así que te sugerimos imprimir la información de la tarifa para ver una vez más sus condiciones.]

# In[392]:


# Imprime las condiciones de la tarifa y asegúrate de que te quedan claras

df_megaline_plans.head(5)  #Corregido tal y como se indicó 


# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Esta no es la información de la tarifa, esa información está en df_megaline_plans
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Muy bien, corregido!
# </div>

# ## Agregar datos por usuario
# 
# [Ahora que los datos están limpios, agrega los datos por usuario y por periodo para que solo haya un registro por usuario y por periodo. Esto facilitará mucho el análisis posterior.]

# In[393]:


# Calcula el número de llamadas hechas por cada usuario al mes. Guarda el resultado.

df_megaline_calls['month'] = df_megaline_calls['call_date'].dt.month
df_megaline_calls.groupby(['user_id', 'month'])['call_date'].count() 


# In[394]:


# Calcula la cantidad de minutos usados por cada usuario al mes. Guarda el resultado.

df_megaline_calls['duration'] = (df_megaline_calls['duration']).apply(np.ceil) 
groupcall=df_megaline_calls.groupby(['user_id', 'month'])['duration'].sum()


# In[395]:


groupcall  


# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Antes de agrupar la duración, debes calcular la duración redondeada, que es sobre la cual se calculará el costo del plan
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Muy bien, corregido!
# </div>

# In[396]:


# Calcula el número de mensajes enviados por cada usuario al mes. Guarda el resultado.

df_megaline_messages['month'] = df_megaline_messages['message_date'].dt.month
groupmen=df_megaline_messages.groupby(['user_id', 'month'])['message_date'].count() 


# In[397]:


# Calcula el volumen del tráfico de Internet usado por cada usuario al mes. Guarda el resultado.

df_megaline_internet['month'] = df_megaline_internet['session_date'].dt.month

# Redondeando los gb hacia arriba 
df_megaline_internet['mb_used'] = (df_megaline_internet['mb_used']).apply(np.ceil) 
groupinter=df_megaline_internet.groupby(['user_id', 'month'])['mb_used'].sum()


# In[398]:


merging_all = groupcall.to_frame().merge(groupmen, on = ['user_id', 'month'], how = 'outer') 
merging_all = merging_all.merge(groupinter, on = ['user_id', 'month'], how = 'outer') 
merging_all.fillna(0, inplace= True)
merging_all.head(20)


# In[399]:


# Obteniendo total de calls por usuario

grouptotalcalls=df_megaline_calls.groupby(['user_id', 'month'])['call_date'].count()
grouptotalcalls


# In[400]:


merging_all = merging_all.merge(grouptotalcalls, on = ['user_id', 'month'], how = 'outer').reset_index() 
merging_all


# In[401]:


merging_allnew = merging_all.rename({'user_id': 'user_id', 'month': 'month','call_date': 'calls', 'duration': 'duration','message_date': 'totalmessages', 'mb_used': 'mg_used'}, axis=1)

# Convirtiendo los mb a gb tal y como se indicó
merging_allnew['mg_used'] =  (merging_allnew['mg_used']/1024)

merging_allnew['mg_used'] = (merging_allnew['mg_used']).apply(np.ceil) 

merging_allnew = merging_allnew.fillna(0)

merging_allnew['calls'] = (merging_allnew['calls']).apply(np.ceil) 

merging_allnew.head(20)


# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Bien con como se juntó la información, los merge debían ser outer tal cual se realizó
# </div>

# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Cada llamada individual se debe aproximar al minuto hacia arriba para contaiblizarla, esto lo debes realizar antes de agruparlas. Por el lado de los mb, se deben converitr primero a gb y luego aproximar hacia arriba.
# </div>

# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Muy bien, se corrigió casi todo pero los gb deben ser aproximados hacia arriba, no redondeados.
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v3</b> <a class="tocSkip"></a>
# 
# 
# Bien, corregido
# </div>

# [Junta los datos agregados en un DataFrame para que haya un registro que represente lo que consumió un usuario único en un mes determinado.]

# In[402]:


# Fusiona los datos de llamadas, minutos, mensajes e Internet con base en user_id y month

merging_allnew =  merging_allnew[['user_id', 'month', 'calls', 'duration', 'totalmessages', 'mg_used' ]]


# In[403]:


df_megaline_users['churn_date'] = df_megaline_users['churn_date'].dt.month
df_megaline_users.head(5)


# In[404]:


# Añade la información de la tarifa

merging_allnew = merging_allnew.merge(df_megaline_users)

merging_allnew2 =  merging_allnew[['user_id', 'month', 'calls', 'duration', 'totalmessages', 'mg_used', 'plan', 'churn_date' ]]
merging_allnew2 = pd.merge(merging_allnew2, df_megaline_plans, left_on='plan', right_on='plan_name')
merging_allnew2.fillna(0, inplace= True)
merging_allnew2['duration'] =  merging_allnew2['duration'].astype(int) # Convertida la columna de duration
merging_allnew2['mg_used'] =  merging_allnew2['mg_used'].astype(int)  # Convertida la columna de uso de internet
merging_allnew2.head(25) 


# In[ ]:





# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# Correcto al agregar los datos de los planes
#     
# </div>

# [Calcula los ingresos mensuales por usuario (resta el límite del paquete gratuito del número total de llamadas, mensajes de texto y datos; multiplica el resultado por el valor del plan de llamadas; añade la tarifa mensual en función del plan de llamadas). Nota: Dadas las condiciones del plan, ¡esto podría no ser tan trivial como un par de líneas! Así que no pasa nada si dedicas algo de tiempo a ello.]

# In[405]:


# Calcula el ingreso mensual para cada usuario

merging_allnew2['total_minutes_fee'] = np.where( merging_allnew2['plan_name'] == 'surf', (merging_allnew2['duration'] - merging_allnew2['minutes_included']) * 0.03, (merging_allnew2['duration'] - merging_allnew2['minutes_included']) * 0.01 )
merging_allnew2['total_minutes_fee'] = merging_allnew2['total_minutes_fee'].clip(lower = 0)

merging_allnew2['total_message_fee'] = np.where( merging_allnew2['plan_name'] == 'surf', (merging_allnew2['totalmessages'] - merging_allnew2['messages_included']) * 0.03, (merging_allnew2['totalmessages'] - merging_allnew2['messages_included']) * 0.01 )
merging_allnew2['total_message_fee'] = merging_allnew2['total_message_fee'].clip(lower = 0)

merging_allnew2['total_megas_fee'] = np.where( merging_allnew2['plan_name'] == 'surf', (merging_allnew2['mg_used'] - merging_allnew2['mb_per_month_included']) * 10, (merging_allnew2['mg_used'] - merging_allnew2['mb_per_month_included']) * 7)

merging_allnew2['total_megas_fee'] = merging_allnew2['total_megas_fee'].clip(lower = 0)

merging_allnew2['total_to_pay'] = merging_allnew2['total_minutes_fee']+merging_allnew2['total_message_fee']+merging_allnew2['total_megas_fee']+ merging_allnew2['usd_monthly_pay']


# In[406]:


merging_allnew2.head(20)


# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer</b> <a class="tocSkip"></a>
# 
# El cálculo de las tarifas es incorrecto debido a que falta convertir correctamente las columnas de duración y uso de internet. Corregiré hasta aquí dado que las siguientes partes dependen de esto.
#     
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v3</b> <a class="tocSkip"></a>
# 
# Correcto
# </div>

# ## Estudia el comportamiento de usuario

# [Calcula algunas estadísticas descriptivas para los datos agregados y fusionados que nos sean útiles y que muestren un panorama general captado por los datos. Dibuja gráficos útiles para facilitar la comprensión. Dado que la tarea principal es comparar las tarifas y decidir cuál es más rentable, las estadísticas y gráficas deben calcularse por tarifa.]
# 
# [En los comentarios hallarás pistas relevantes para las llamadas, pero no las hay para los mensajes e Internet. Sin embargo, el principio del estudio estadístico que se aplica para ellos es el mismo que para las llamadas.]

# ### Llamadas

# In[407]:


# Compara la duración promedio de llamadas por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.

merging_allnew2.groupby(['plan_name', 'month'])['calls'].mean()


# In[408]:


# Trazando gráfico de barras 

df = pd.DataFrame()
mis_booleans = ( merging_allnew2['plan_name']=='surf' )
dfg = merging_allnew2[mis_booleans].groupby(['month'])['calls'].mean() 
df['surf'] = dfg.values

mis_booleans = ( merging_allnew2['plan_name']=='ultimate' )
dfg = merging_allnew2[mis_booleans].groupby(['month'])['calls'].mean() 
df['ultimate'] = dfg.values
df.reset_index()
df.index = np.arange(1, len(df) + 1)
df


# In[409]:



plt.style.use('ggplot')
df.plot(kind='bar', figsize = (12, 6), rot = 0)
plt.xlabel("Meses del año")
plt.ylabel("Número de llamadas")
plt.title("Distribución de las llamadas por plan y mes") 
plt.legend(['Surf', 'ultimate'], title='Planes')
plt.show()


# <div class="alert alert-block alert-warning">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Muy bien con el gráfico, muestra la evolución de los planes lado a lado. NOta eso sí que los meses del año son incorrectos, deberían ir de 1 a 12. Para corregir este detalle debes aplicar reset_index() a dfg para obtener los meses como una columna adicional a la cantidad de llamadas.
#     
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v3</b> <a class="tocSkip"></a>
# 
# Muy bien, corregido
# </div>

# In[410]:


# Preparing data for the graph
df2 = pd.DataFrame()

mis_booleans = ( merging_allnew2['plan_name']=='surf' )
dfg = merging_allnew2[mis_booleans].groupby(['month'])['duration'].mean().apply(np.ceil) 
df2['surf'] = dfg.values

mis_booleans = ( merging_allnew2['plan_name']=='ultimate' )
dfg = merging_allnew2[mis_booleans].groupby(['month'])['duration'].mean().apply(np.ceil) 
df2['ultimate'] = dfg.values
df2.index = np.arange(1, len(df2) + 1)
df2


# In[411]:


# Compara el número de minutos mensuales que necesitan los usuarios de cada plan. Traza un histograma.

plt.style.use('ggplot')
df2.plot(kind='bar', figsize = (12, 6), rot = 0)
plt.xlabel("Meses del año")
plt.ylabel("Número de llamadas")
plt.title("Distribución de los minutos por plan y meses del año") 
plt.legend(['Surf', 'ultimate'], title='Planes')
plt.show()


# <div class="alert alert-block alert-warning">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Bien, pero mismo comentario anterior
#     
# </div>

# [Calcula la media y la variable de la duración de las llamadas para averiguar si los usuarios de los distintos planes se comportan de forma diferente al realizar sus llamadas.]

# In[412]:


# Calcula la media y la varianza de la duración mensual de llamadas.

df = merging_allnew2.groupby(['month'])['calls'].agg(['mean', 'var'])
df


# In[413]:


mis_booleans = (merging_allnew2['plan_name']=='surf')
dfsurf = merging_allnew2[mis_booleans].groupby('month')['duration'].sum()

mis_booleans = (merging_allnew2['plan_name']=='ultimate')
dfulti = merging_allnew2[mis_booleans].groupby('month')['duration'].sum()
df = pd.DataFrame({'surf': dfsurf.values, 'ultimate': dfulti.values})
df


# In[414]:


# Traza un diagrama de caja para visualizar la distribución de la duración mensual de llamadas

plt.style.use('ggplot')
# Set the figure size
plt.rcParams["figure.figsize"] = [12, 8]
plt.rcParams["figure.autolayout"] = True

# Plot the dataframe
ax = df[['surf', 'ultimate']].plot(kind='box', title='boxplot')
ax = fig.add_subplot(111)
ax.set_title('Distribución de la duración mensual de llamadas')
ax.set_xlabel('Duración')
ax.set_ylabel('Cantidad de llamadas')
plt.show()


# <div class="alert alert-block alert-warning">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Esto es correcto, pero idealmente deberías trazar un histograma para cada plan
#     
# </div>

# [Elabora las conclusiones sobre el comportamiento de los usuarios con respecto a las llamadas. ¿Su comportamiento varía en función del plan?]

# ### Mensajes

# In[415]:


# Compara el número de mensajes que tienden a enviar cada mes los usuarios de cada plan

plt.style.use('ggplot')
dfg = merging_allnew2.groupby(['plan_name', 'month'])['totalmessages'].sum()
dfg.plot(kind='bar', title='Mensajes por planes y mes', ylabel='Cantidad de mensajes', xlabel='meses', figsize=(14, 6))


# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Muy bien!
#     
# </div>

# In[416]:


# Compara la cantidad de tráfico de Internet consumido por usuarios por plan

plt.style.use('ggplot')
dfg = merging_allnew2.groupby(['plan_name', 'month'])['mg_used'].sum()
dfg.plot(kind='bar', title='Megas utilizados por plan y mes', ylabel='Cantidad de megas', xlabel='meses', figsize=(14, 6))


# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Muy bien!
#     
# </div>

# In[417]:


x = merging_allnew2[merging_allnew2['plan_name'] == 'surf'].groupby(['month'])['mg_used'].sum()
y = merging_allnew2[merging_allnew2['plan_name'] == 'ultimate'].groupby(['month'])['mg_used'].sum()


# In[418]:


labels =  [1,2,3,4,5,6,7,8,9,10,11,12]
dataa = {'Surf': x.values,
        'Ultimate': y.values,
        'axis': labels
       }
df = pd.DataFrame(dataa)
df.index = np.arange(1, len(df2) + 1)
#df


# In[419]:


plt.style.use('ggplot')

ax = df[['Surf', 'Ultimate']].plot(kind='bar', title =" Tráfico de Internet consumido por usuarios por plan",figsize=(14,8),legend=True, fontsize=12, rot = 0)
ax.set_xlabel("Meses del año",fontsize=12)
ax.set_ylabel("Cantidad de megas consumidos",fontsize=12)
plt.setp(ax.get_xticklabels(), rotation=0, horizontalalignment='right')
plt.show()
# Se corrigieron los labels de los meses y se recalculó el consumo de gb


# [Elabora las conclusiones sobre el comportamiento de los usuarios con respecto a los mensajes. ¿Su comportamiento varía en función del plan?]
# 
# A partir del análisis del gráfico sobre la cantidad de mensajes que tienden a  enviar los usuarios, se observa que existen diferencias entre cantidad enviada por usuarios del plan Surf y la cantidad enviada por usuarios del plan Ultimate, de tal modo que, en todos los meses la cantidad de mensajes enviados de los usuarios del plan Surf supera al de los usuarios del plan ultimate, no obstante, la cantidad mensual se va incrementando paulatinamente en la medida en que transcurren los meses del año para ambos planes. 

# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Correcta la forma del gráfico y las conclusiones, pero también se tiene el detalle de que los meses son incorrectos y además hay que recalcular el consumo de gb según la corrección indicada anteriormente.
#     
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v3</b> <a class="tocSkip"></a>
# 
# Bien, corregido
#     
# </div>

# ### Internet

# <div class="alert alert-block alert-warning">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# El gráfico anterior debería estar en esta sección
#     
# </div>

# [Elabora las conclusiones sobre cómo los usuarios tienden a consumir el tráfico de Internet. ¿Su comportamiento varía en función del plan?]
# 
# Luego de analizado el gráfico de barra del consumo de megas por navegación de internet por parte de los usuarios, se aprecia que existen diferencias entre el tráfico de internet consumido por usuarios tanto de plan Surf así como los pertenecientes al plan Ultimate, observándose que, para clientes de ambos planes se va incrementando el tráfico a medida que transcurre el año, siendo mayor el incremento para aquellos clientes del plan surf, pudiendo ser debido a que es un plan más económico y asequible para un mayor número de personas. En ambos planes el pico máximo de consumo se alcanza en el mes de diciembre.

# ## Ingreso

# [Del mismo modo que has estudiado el comportamiento de los usuarios, describe estadísticamente los ingresos de los planes.]

# In[420]:


x = merging_allnew2[merging_allnew2['plan_name'] == 'surf'].groupby(['month'])['total_to_pay'].sum()

mis_booleans = ( merging_allnew2['plan_name']=='ultimate')
y = merging_allnew2[mis_booleans].groupby(['month'])['total_to_pay'].sum()


# In[426]:


labels =  [1,2,3,4,5,6,7,8,9,10,11,12]
dataa = {'Surf': x.values,
        'Ultimate': y.values,
        'axis': labels
       }
df = pd.DataFrame(dataa)
df.index = np.arange(1, len(df) + 1)


# In[427]:


plt.style.use('ggplot')

ax = df[['Surf', 'Ultimate']].plot(kind='bar', title =" Ingresos por plan",figsize=(14,6),legend=True, fontsize=12)
ax.set_xlabel("Meses del año",fontsize=12)
ax.set_ylabel("Ingresos",fontsize=12)
plt.setp(ax.get_xticklabels(), rotation=0, horizontalalignment='right')
plt.show()


# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Bien con la idea del gráfico, pero se revisará nuevamente una vez corregido el conteo de consumo de internet
#     
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v3</b> <a class="tocSkip"></a>
# 
# Excelente, corregido
#     
# </div>

# [Elabora las conclusiones sobre cómo difiere el ingreso entre los planes.]
# 
# Luego de analizado el gráfico sobre el ingreso mensual por plan, se aprecia que existe una diferencia notable en cuanto a los ingresos de ambos planes, observándose que los ingresos obtenidos por los usuarios inscritos en el plan Ultimate son superiores a los ingresos obtenidos por los usuarios inscritos en el plan Surf analizados mes a mes. El comportamiento en ambos grupos es similar, siendo con tendencia creciente, aunque el ingreso de usuarios ultimate es superior en todos los meses a los de usuarios surf, siendo el mes de mayor ingreso, el mes de diciembre, obteniéndose ingresos por valor de 14316332.66 (unidades en miles de pesos).

# ## Prueba las hipótesis estadísticas

# [Prueba la hipótesis de que son diferentes los ingresos promedio procedentes de los usuarios de los planes de llamada Ultimate y Surf.]

# [Elabora las hipótesis nula y alternativa, escoge la prueba estadística, determina el valor alfa.]
# 
# ### Definiendo las hipótesis:
# H_0: Los ingresos promedio procedentes de los usuarios de los planes de llamada Ultimate y Surf son iguales.
# 
# H_1: Los ingresos promedio procedentes de los usuarios de los planes de llamada Ultimate y Surf son diferentes.
# 
# ### Estadístico de prueba:
# 
# 
# ### Región de rechazo:
# 
# Estadístico t-test utilizado
# 
# alpha = 0.05 

# In[425]:


# Prueba las hipótesis

x = merging_allnew2[merging_allnew2['plan_name'] == 'surf'].groupby(['month'])['total_to_pay'].sum()
y = merging_allnew2[merging_allnew2['plan_name'] == 'ultimate'].groupby(['month'])['total_to_pay'].sum()

st.levene(x, y)


# El resultado del test de levene arroja 1.52 en el estadístico de prueba y 0.22 en el p-value, siendo éste último mayor que el nivel de significancia, tras lo cual no hay evidencia suficiente para rechazar la hipótesis nula, por tanto las varianzas de las poblaciones son iguales.

# In[424]:


st.ttest_ind(x, y, equal_var = True)


# El parámetro equal_va se mantiene en True ya que la prueba de levene arrojó que las varianzas de las poblaciones son iguales.

# [Elabora las hipótesis nula y alternativa, escoge la prueba estadística, determina el valor alfa.]
# 
# Se aplicó la prueba T-test, obteniéndose un p-valor de 0.29 y -1.07 para el estadístico, notando que el p-valor es mayor que el nivel de significancia, tras lo cual no hay evidencia suficiente para rechazar la hipótesis nula. 

# 2-[Prueba la hipótesis de que el ingreso promedio de los usuarios del área NY-NJ es diferente al de los usuarios de otras regiones.]
# 
# 

# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Se tiene la idea correcta de los test, pero debes proceder primero realizando el test de levene y luego, según el resultado del test de levene, usar equal_var con True o False. Recuerda que el test de Levene determina si las poblaciones tienen igual o diferente varianza, si se rechaza la hip. nula de levene, las varianzas son diferentes, si no, son iguales. Según ese resultado, aplica el correspondiente t-test.
#     
# Revisaré el resultado después de que se corrija el cálculo de consumo de internet e ingreso.
#     
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v3</b> <a class="tocSkip"></a>
# 
# Excelente, corregido
#     
# </div>

# # Prueba las hipótesis
# 
# ### Definiendo las hipótesis:
# H_0: Los ingresos promedio de los usuarios que viven en NY-NJ es igual al de otros usuarios de otras regiones.
# 
# H_1: Los ingresos promedio de los usuarios que viven en NY-NJ es diferente al de otros usuarios de otras regiones.
# 
# ### Estadístico de prueba:
# 
# 
# ### Región de rechazo:
# 
# Estadístico t-test utilizado
# alpha = 0.05

# In[370]:


# Prueba las hipótesis

merging_allnew2 = merging_allnew2.merge(df_megaline_users)
contain_values = merging_allnew2[merging_allnew2['city'].str.contains('NY-NJ')]
groupinter = contain_values.groupby(['month'])['total_to_pay'].sum()
x =groupinter

contain_valuess = merging_allnew2[~merging_allnew2['city'].str.contains('NY-NJ')]
groupinterr = contain_valuess.groupby(['month'])['total_to_pay'].sum()
y =groupinterr
st.levene(x, y)


# Al aplicar el test de levene se obtiene que el valor del estadístico de prueba es 8.90 y 0.007 en el p-value, siendo elte último menor que el nivel de significancia previamente establecido (0.05), tras lo cual se puede decir que se rechaza la hipóteis nula de levene, o sea, las varianzas de las poblaciones son diferentes. 

# In[369]:


st.ttest_ind(x, y, equal_var = False)


# Se aplicó la prueba T-test, obteniéndose -1.16 en el estadístico y 0.26 para el p-value, notando que el p-valor es mayor que el nivel de significancia, tras lo cual se rechaza la hipótesis nula. 

# <div class="alert alert-block alert-danger">
# <b>Comentario de Reviewer v2</b> <a class="tocSkip"></a>
# 
# Mismo comentario anterior
#     
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v3</b> <a class="tocSkip"></a>
# 
# Excelente, corregido
#     
# </div>

# ## Conclusión general
# 
# [En esta sección final, enumera tus conclusiones importantes. Asegúrate de que estas abarquen todas las decisiones (suposiciones) importantes que adoptaste y que determinaron la forma elegida para procesar y analizar los datos.]
# 
# 1- Se obtuvo como resultado que a partir del análisis del gráfico sobre la cantidad de mensajes que tienden a enviar los usuarios, se observa que existen diferencias entre cantidad enviada por usuarios del plan Surf y la cantidad enviada por usuarios del plan Ultimate, de tal modo que, en todos los meses la cantidad de mensajes enviados de los usuarios del plan Surf supera al de los usuarios del plan ultimate, no obstante, la cantidad mensual se va incrementando paulatinamente en la medida en que transcurren los meses del año para ambos planes.
# 
# 2- También se obtuvo luego de analizado el gráfico de barra del consumo de megas por navegación de internet por parte de los usuarios, se aprecia que existen diferencias entre el tráfico de internet consumido por usuarios tanto de plan Surf así como los pertenecientes al plan Ultimate, observándose que, para clientes de ambos planes se va incrementando el tráfico a medida que transcurre el año, siendo mayor el incremento para aquellos clientes del plan surf, pudiendo ser debido a que es un plan más económico y asequible para un mayor número de personas. En ambos planes el pico máximo de consumo se alcanza en el mes de diciembre.
# 
# 3- Luego de analizado el gráfico sobre el ingreso mensual por plan, se aprecia que existe una diferencia notable en cuanto a los ingresos de ambos planes, observándose que los ingresos obtenidos por los usuarios inscritos en el plan Ultimate son superiores a los ingresos obtenidos por los usuarios inscritos en el plan Surf analizados mes a mes. El comportamiento en ambos grupos es similar, siendo con tendencia creciente, aunque el ingreso de usuarios ultimate es superior en todos los meses a los de usuarios surf, siendo el mes de mayor ingreso, el mes de diciembre, obteniéndose ingresos por valor de 14316332.66 (unidades en miles de pesos).
# 
# 4- Adicionalemente, se aplicó la prueba T-test, obteniéndose un p-valor de 0.29 y 1.07 para el estadístico, notando que el p-valor es mayor que el nivel de significancia, tras lo cual no hay evidencia suficiente para rechazar la hipótesis nula. 
# 
# 5- Por último, Se aplicó la prueba T-test, obteniéndose -1.16 en el estadístico y 0.26 para el p-value, observándose que el p-valor es mayor que el nivel de significancia, tras lo cual se rechaza la hipótesis nula.   

# <div class="alert alert-block alert-success">
# <b>Comentario de Reviewer v3</b> <a class="tocSkip"></a>
# 
# Felicitaciones por las conclusiones, muy completas. Es muy bueno que hayas incluido métricas clave del desarrollo del notebook, permiten darle fuerza y objetividad a las conclusiones
#     
# </div>
