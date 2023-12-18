<?php 
$mysqli = mysqli_connect('jameslynn.ipagemysql.com', 'dev2', 'RS6w5A8R2Mu8PMd!', 'dev2'); 
if (!$mysqli) { 
    die('Could not connect: ' . mysql_error()); 
} 
echo 'Connected successfully' . PHP_EOL; 
echo '<h1>TEST CONNECT </h1>';
echo "Host information: " . mysqli_get_host_info($mysqli) . PHP_EOL;
echo '<p/>';

// Return name of current default database
if ($result = $mysqli -> query("SELECT DATABASE()")) {
  $row = $result -> fetch_row();
  echo "Default database is " . $row[0];
  $result -> close();
}

?> 
;