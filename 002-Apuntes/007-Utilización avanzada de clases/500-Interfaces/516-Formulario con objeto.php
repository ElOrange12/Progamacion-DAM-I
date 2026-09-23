<?php
	
	$cliente = [
		"nombre" => "Daniel",
		"apellidos" => "Oliveira Vidal",
		"email" => "info@elorange.com"
	];
	
	foreach($cliente as $clave=>$valor){
		echo "<label>".$clave."</label>";
		echo "<input type='text' value='".$valor."'>";
	}
	
?>
