<?php
$data = json_decode(file_get_contents('https://api.covid19api.com/summary'), true);
echo json_encode($data);
echo "ayaj";
?>