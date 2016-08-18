<?php

// Check to see if $input is a palindrome
// Examples of palindromes:
// redivider, noon, civic, radar, level, rotor, kayak, reviver, racecar, redder, madam, and refer.
function isPalindrome($word)
{
    echo "$word\n";
    $wordLength = strlen($word);

    echo "word length: $wordLength\n";

    $midPoint = (int)ceil($wordLength / 2) - 1;
    $midPointLetter = $word[$midPoint];

    echo "mid point index: $midPoint, $midPointLetter\n";

    $prevLetters = array();

    for ($currLetIdx = 0; $currLetIdx < $wordLength; $currLetIdx++) {
        $currentLetter = $word[$currLetIdx];
        $prevLetters[] = $currentLetter;

        $comparisonIndex = $wordLength - ($currLetIdx + 1);

        if ($currLetIdx > $midPoint) {
            echo "current index:"  . $currLetIdx . "\n";
            echo "current letter:" . $currentLetter . "\n";
            echo "comparison index:" . $comparisonIndex . "\n";
            echo "comparison letter:" . $prevLetters[$comparisonIndex] . "\n";
        }

        if ($currLetIdx > $midPoint && $currentLetter != $prevLetters[$comparisonIndex]) {
            echo "stopping ...\n";
            return false;
        }
    }

    return true;
}

$palindromes = array('noon', 'civic', 'reviver', 'word', 'racecar', 'redder');
foreach ($palindromes as $palindrome) {
    var_dump(isPalindrome($palindrome));
    echo "\n";
}


?>