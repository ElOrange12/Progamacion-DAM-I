'''
	Diccionario de partidos
	v1.0 Daniel Oliveira Vidal
	Este programa tiene un diccionario que almacena una serie de partidos y sus caracteristicas
'''


partidos = [
	{
		'equipo_local':'Real Madrid',
		'equipo_visitante':'FC Barcelona',
		'resultado':'0-4',
		'estadio':'Santiago Bernabeu'
	},{
		'equipo_local':'Manchester City',
		'equipo_visitante':'Liverpool',
		'resultado':'3-0',
		'estadio':'Etihad Stadium'
	},{
		'equipo_local':'Real Sociedad',
		'equipo_visitante':'Atletico de Madrid',
		'resultado':'1-1',
		'estadio':'Estadio de Anoeta'
	}
]

print('Equipo local primer equipo: 'partidos[0]['equipo_local'])

for partido in partidos:
	for i in partidos:
		print(partido[i])
