<?php
	
	$cliente = [
		"nombre" => "Daniel",
		"apellidos" => "Oliveira Vidal",
		"email" => "info@elorange.com"
	];
	
	foreach($cliente as $clave=>$valor){
		echo $clave.": ".$valor."<br>";
	}
		
?>
