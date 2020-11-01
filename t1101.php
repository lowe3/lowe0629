
<html>
	<?php
	$dbconn = pg_connect("host=ec2-34-200-101-236.compute-1.amazonaws.com dbname=d4jgiqvfjf2nde user=rdvsrzpesjtzad password=eddaf28d42616aba0fd4de92aeb8df4d1e33c6e1ae6a202da17fd1d6cd39fbaf")
	?>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>餐點紀錄</title>
    <script src="https://d.line-scdn.net/liff/1.0/sdk.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
		function get() {
			col1 = $("#column1").val();
			col2 = $("#column2").val();
			$.get("ajax1.php", {
					c1: $("#column1").val(),
					c2: $("#column2").val()
				})
				.done(function(data) {
					$("#column3").empty();
					$("#column3").append(data);
				});
		}
		function onChangeColumn() {

		}
	</script>
</head>

<body>
    <div class="row" style="margin: 10px">
		<div class="col-12" style="margin: 10px">
		<label>超商</label>
		<select id="column1" onChange="get()">
			<option selected>請選擇</option>
				<?php
					echo '<option value="7-11">7-11</option>
						 <option value="全家">全家</option>';
				
                ?>			
		</select>
		<br />
		<label>種類</label>
		<select id="column2" onChange="get()">
			<option selected>請選擇</option>
				<?php
					echo '<option value="飯類">飯類</option>
						 <option value="麵類">麵類</option>
						 <option value="沙拉">沙拉</option>
						 <option value="麵包">麵包</option>
						 <option value="飲料">飲料</option>
						 <option value="關東煮">關東煮</option>
						 <option value="甜點">甜點</option>
						 <option value="湯類">湯類</option>
						 <option value="水果">水果</option>
						 <option value="醬料">醬料</option>
						 <option value="其他">其他</option>';
				
                ?>	

		</select>
		<br />
		<label>產品名稱</label>	
		<select id="column3" >
		<option selected>請選擇</option>
		</select>
</body>

</html>