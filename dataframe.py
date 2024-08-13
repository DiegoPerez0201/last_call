import pandas as pd

df_csv = pd.read_csv('./data/AFP_HABITAT_MONEDA-2024-04-01T00_00_00.000Z-a-2024-07-31T00_00_00.000Z-ultimo-estado-QmgUtJPAeP.csv', delimiter=';')

df_csv.rename(columns={
    'ID Ticket': 'id_ticket',
    'ID Llamada': 'id_llamada',
    'Oficina': 'oficina',
    'Codigo de Oficina': 'codigo_oficina',
    'Fila': 'fila',
    'Modulo': 'modulo',
    'Fecha': 'fecha',
    'Prefijo Ticket': 'prefijo_ticket',
    'Nro. Ticket': 'nro_ticket',
    'DNI Ejecutivo': 'dni_ejecutivo',
    'DNI Ejecutivo DV': 'dni_ejecutivo_dv',
    'Nombre Ejecutivo': 'nombre_ejecutivo',
    'DNI Cliente': 'dni_cliente',
    'DNI Cliente DV': 'dni_cleinte_dv',
    'Hora Emision Ticket': 'hora_emision_ticket',
    'Hora Llamada': 'hora_llamada',
    'Tiempo Espera': 'tiempo_espera',
    'Tiempo Atencion': 'tiempo_atencion',
    'Motivo Atencion': 'motivo_atencion',
    'Perdido': 'perdido',
    'Saltado': 'saltado',
    'Email Cliente': 'email_cliente',
    'Rating': 'rating',
    'Comentario': 'comentario',
    'Nombre Cliente': 'nombre_cliente',
    'Formulario': 'formulario',
    'Segmento': 'segmento',
    'ID de llamada anterior': 'id_llamada_anterior',
    'UTM': 'utm',
    'ID Submotivos': 'id_submotivo',
    'Submotivos de atencion': 'submotivo_atencion',
    'Carpeta': 'carpeta',
    'Categorizacion-Derivacion': 'categorizacion_derivacion',
    'Modalidad de atencion': 'modalidad_atencion',
    'Tipo de cliente': 'tipo_cliente',
    'Pregunta Botonera': 'pregunta_botonera',
    'Carpeta de motivos': 'carpeta_motivos',
    'Preferencia Usuario': 'preferencia_usuario',
    'Submotivos v2': 'submotivos_v2',
    'Sucursal de origen': 'sucursal_origen'
    }, inplace=True)

df_csv.to_csv('./clean_data/data.csv', index=False)

print(df_csv)