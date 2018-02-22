Sample PHP 4 (PHP 5 compatible) code that counts from 1 to 1,000,000 in words
E.g. 39000 is outputted as "thirty nine thousand"

File:
count.php (main script)
countRoutines (related functions included by count.php)

Command-line usage:
It can be used from the command line, or over the web.
If it's used from the command line, pass an integer from one to one million as the first parameter to count.php.
E.g.:
php count.php 39000

Web-usage:
If you run it over the web (or from the command line without any parameter), set the value of $limit in count.php, and it will count up to that number, in words.

Notes: this script was written rather quickly over two days. There is room for improvement in terms of:
- better grammar
- support for mutliple languages (German, Spanish, etc.)
- optimized algorithms (notes are in the code where improvements could be made)
- better organization of code into classes


