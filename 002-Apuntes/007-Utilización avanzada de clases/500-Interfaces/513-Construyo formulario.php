<?php
	
	$campos_cliente = [
		"nombre",
		"apellidos",
		"email",
		"telefono",
		"dirección",
		"población"
	];
	
	foreach($campos_cliente as $campo){
		echo '<input type="text" placeholder="'.$campo.'"><br>';
	}
	
?>
