<?php
/**
 * I. Author: Jayesh Sheth / https://github.com/jsheth7
 *
 * II. Notes / TODO
 * for the ease of demonstration, all the code is in one file.
 * In a real-world scenario, each class would be in its own file, and auto-loaded according to the appropriate PSR standard.
 * Similarly, unit tests would be added using PHPUnit, building upon the sample code that reads test cases from samples.txt.
 *
 * III. Purpose / Methodology
 *
 * Examine request headers, and parse headers related to the forwarded HTTP request (coming from a proxy)
 * Parse either "Forwarded" header, or a combination of "X-Forwarded-For" and "X-Forwarded-Proto" into a standardized array.
 * e.g. array ['for' => [], 'proto' => [], 'by' => []]
 *
 * IV. How do I run this?
 *
 * 1) Ensure samples.txt is next to process_forwarded.php
 * 2) php ./process_forwarded.php
 *
 * V. Further reading
 * Forwarded: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Forwarded
 * X-Forwarded-For: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For
 * X-Forwarded-Proto: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Proto
 */

/**
 * Allow the successive processing of alternative regular expressions, without painful, nested conditions.
 * A little play on recursion in an object-oriented context.
 * Goal: more readable, less repetitive and more compact regex code.
 */
class RegexChain {

    /**
     * Regular expression matches
     * @var array
     */
    protected $matches;

    /**
     * Regular expression subject
     * @var string
     */
    protected $subject;

    /**
     * RegexChain constructor.
     * @param string $subject Subject to be matched
     * @param array $matches - optional [ only needs to be set to stop further processing for orMatch() ]
     */
    function __construct($subject, $matches = []){
        $this->subject = $subject;

        if(count($matches) > 0){
            $this->matches = $matches;
        }
        else{
            $this->matches = [];
        }
    }

    /**
     * Method to provide syntactic sugar for easy instantiation of object plus chaining of multiple orMatch() calls in one line
     * @param $subject
     * @return RegexChain
     */
    public static function getInstance($subject){
        $regexChain = new RegexChain($subject);
        return $regexChain;
    }

    /**
     * Match a pattern, in the case the same instance of this class has not already found a match (from a prior pattern)
     * @param $pattern
     * @return $this|RegexChain
     */
    public function orMatch($pattern){

        //Stop further processing, if match was previously found (in any of previous match operations)
        if(!empty($this->matches[1]) || empty($this->subject) ){
            return new RegexChain(null, $this->matches);
        }

        preg_match_all($pattern, $this->subject, $this->matches);

        if( !empty($this->matches[1]) ){ //Match was found - return current instance
            return $this;
        }
        else{
            $new = new RegexChain($this->subject);
            return $new;
        }

    }

    public function getMatches(){
        if(array_key_exists(1, $this->matches)){
            $this->matches = array_slice($this->matches, 1);
        }

        return $this->matches;
    }

}

class HeaderParser {

    function __construct(){

    }

    /**
     * Look for the request header(s), in the following order:
     *
     * - Forwarded
     * - X-Forwarded-For and/or X-Forwarded-Proto
     *
     * If the "Forwarded" header is found,  parse its value into an array of constituent parts.
     * Return an array in the format: ['for' => '', 'proto' => '', 'by' => '']
     *
     * If it's not found, return an array containing either (or both of the following): X-Forwarded-For and X-Forwarded-Proto.
     * e.g. ['for' => '', 'proto' => '']
     * @param $headers
     * @return mixed
     */
    public function parseHeaders($headers){
        $return = [];

        if(isset($headers['Forwarded'])){
            $return = $this->parseForwarded($headers['Forwarded']);
        }

        else {
            if(isset($headers['X-Forwarded-For'])){
                $return['for'] = $this->parseForwardedFor($headers['X-Forwarded-For']);
            }

            if(isset($headers['X-Forwarded-Proto'])){
                $return['proto'] = $headers['X-Forwarded-Proto'];
            }

            //$return['by'] = '';
        }

        return $return;
    }

    /**
     * Given the value of a "Forwarded" header, parse it into an array of constituent parts.
     * @param string $headerValue Header value
        Sample header values are below:
        for="_mdn"

        # case insensitive
        For="[2001:db8:cafe::17]:4711"

        # separated by semicolon
        for=192.0.2.60; proto=http; by=203.0.113.43

        # multiple values can be appended using a comma
        for=192.0.2.43, for=198.51.100.17
     *
     * @return array ['for' => [], 'proto' => [], 'by' => []]
     */
    protected function parseForwarded($headerValue){
        $matches = [];

        // Extract all possible variations of "for" within the header, including multiple matches:
        $matches['for'] = RegexChain::getInstance($headerValue)
                    ->orMatch('/for="([a-zA-z_]{1,})"/i') //Forwarded: for="_mdn"
                    ->orMatch('/for=([0-9.]{7,})/i') // Forwarded: for=192.0.2.43, for=198.51.100.17; proto=http; by=203.0.113.43
                    ->orMatch('/for="\[([:a-z0-9]{1,39})\](?::([0-9]{2,4}))?"/i') // For=["2001:db8:cafe::17"]:4900 OR For=["2001:db8:cafe::17"]
                    ->getMatches();

        //Extract protocol (http or https)
        $matches['proto'] = RegexChain::getInstance($headerValue)->orMatch('/proto=(https?)/')->getMatches();

        //Extract "by"
        $matches['by'] = RegexChain::getInstance($headerValue)->orMatch('/by=([0-9.]{7,})/')->getMatches();

        return $matches;
    }

    /**
     * Parse X-Forwarded-For header into array of IP addresses
     * @param $headerValue
     * @return array
     */
    protected function parseForwardedFor($headerValue){
        return RegexChain::getInstance($headerValue)->orMatch('/([0-9.]{7,})/')->getMatches();
    }

}



// Live request through Apache web server would be processed like this:
//$headers = apache_request_headers();

echo "TEST 1 (Forwarded absent):\n";
$headers = ['X-Forwarded-For' => '192.0.2.43, 198.51.100.17', 'X-Forwarded-Proto' => 'https'];
print_r($headers);
$headerParser = new HeaderParser();
$matches = $headerParser->parseHeaders($headers);
print_r($matches);

echo "TEST 2 (Forwarded present):\n";
$headers = ['X-Forwarded-For' => '192.0.2.43, 198.51.100.17', 'X-Forwarded-Proto' => 'https',
            'Forwarded' => 'for=192.0.2.43, for=198.51.100.17; proto=https; by=203.0.113.43'];
print_r($headers);
$headerParser = new HeaderParser();
$matches = $headerParser->parseHeaders($headers);
print_r($matches);


// Demonstration of parsing of various header test samples from text file (one at a time):
// The same parsing from live headers is shown in a commented-out example above.
echo "TEST 3 (SAMPLES):\n";
$lines = file('./samples.txt');
print_r($lines);

foreach($lines as $line){
    //$lineParts = explode(':', $line);

    //If the line starts with 'Forwarded:'
    $matches = [];
    if( preg_match("/(Forwarded|X-Forwarded-For|X-Forwarded-Proto): (.*)/", $line, $matches) ){
        $lineParts = [$matches[1] => $matches[2]];

        echo "{$matches[1]}: {$matches[2]}\n";

        $headerParser = new HeaderParser();
        $matches = $headerParser->parseHeaders($lineParts);

        echo "MATCHES: \n";
        print_r($matches);
    }

}


?>