
<?php
	$c1=$_GET['c1'];
	$c2=$_GET['c2'];
	$host='ec2-34-200-101-236.compute-1.amazonaws.com';
	$dbname='d4jgiqvfjf2nde';
	$user='rdvsrzpesjtzad';
	$password='eddaf28d42616aba0fd4de92aeb8df4d1e33c6e1ae6a202da17fd1d6cd39fbaf';
	$dbconn = pg_connect($host,$dbname,$user,$password);
	$sql = "SELECT * FROM funclapi_food while convenience==$c1 and kind==$c2";
	$result = pg_query($sql);
    if (!$result)
    {
        die(pg_last_error($dbconn));
    }
    while ($row = pg_fetch_row($result)) //從資料庫中抓出類別的資料，供使用者可以直接選擇
    {
        echo "<option value=".$row[0].">".$row[1]."</option>";
    }
	pg_close($dbconn);
?>