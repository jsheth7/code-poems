<?php
	
	/**
	Given an array of numbers, replace each number in each array value with the word for the number.
	Sample input: array(123)
	Sample output: array("OneTwoThree")
	*/
	$words = array(123, 4567, 409);
	print_r($words);
	
	$translations = array();
	
	foreach ($words as $word) {
		$replacePairs = array("Zero", "One", "Two", "Three", "Four", "Five", "Six","Seven","Eight","Nine","Ten");
		
		$translation = strtr($word, $replacePairs);
		$translations[] = $translation;
	}
	
	print_r($translations);
?>