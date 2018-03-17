<?php
$host = 'localhost';
$user = 'root';
$pass = ' ';

mysql_connect($host, $user, $pass);

mysql_select_db('demo');

$select_path="select * from image_table";

$var=mysql_query($select_path);

while($row=mysql_fetch_array($var))
{
 $image_name=$row["myimage"];
 $image_path=$row["/C:/Users/Zarif/OneDrive/Documents/Python Projects/images/"];
 echo "img src=".$image_path."/".$image_name." width=100 height=100";
}
?>
