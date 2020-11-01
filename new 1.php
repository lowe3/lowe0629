<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>餐點紀錄</title>
    <script src="https://d.line-scdn.net/liff/1.0/sdk.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
<script>
	function initializeApp(data) {  //初始化LIFF
		var userid = data.context.userId;  //取得ID
	}

	function pushMsg(sdatetime, sstore, skind) {
		if (sdatetime == '' || sstore == '' || skind == '') {  //資料檢查
			alert('每個項目都必須輸入！');
			return;
		}
		var msg = "***";  //回傳訊息字串
		msg = msg + sdatetime + "/";
		msg = msg + sstore + "/";
		msg = msg + skind;
		liff.sendMessages([  //推播訊息
			{ type: 'text',
			  text: msg
			}
		])
			.then(() => {
				liff.closeWindow();  //關閉視窗
			});
	}

	$(document).ready(function () {
		liff.init(function (data) {  //初始化LIFF
			initializeApp(data);
		});
		
		$('#sure').click(function (e) {  //按下確定鈕
			pushMsg($('#datetime').val(), $('#store').val(), $('#kind').val());
		});
	});
</script>
</head>
<body>
<?php
					$dbconn = pg_connect("host=ec2-34-200-101-236.compute-1.amazonaws.com dbname=d4jgiqvfjf2nde user=rdvsrzpesjtzad password=eddaf28d42616aba0fd4de92aeb8df4d1e33c6e1ae6a202da17fd1d6cd39fbaf")
						or die('Could not connect:'. pg_last_error());
					$query = 'SELECT * FROM funclapi_food';
					$result = pg_query($query) or die('Query failed: ' . pg_last_error());
					echo "<table>\n";
					while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
						echo "\t<tr>\n";
						foreach ($line as $col_value) {
							echo "\t\t<td>$col_value</td>\n";
						}
						echo "\t</tr>\n";
					}
					echo "</table>\n";

					// 釋放結果集
					pg_free_result($result);

					// 關閉連接
					pg_close($dbconn);
					?>
    <div class="row" style="margin: 10px">
        <div class="col-12" style="margin: 10px">
            <label>日期時間</label>
            <input type="datetime-local" id="datetime" value="" class="form-control" />
            <br />
            <label>超商</label>
            <select id="store" class="form-control">
                <option selected>7-11</option>
                <option>全家</option>
            </select>
            <br />
            <label>食物種類</label>
            <select id="kind" class="form-control">
                <option selected>飯類</option>
                <option>麵類</option>
				<option>關東煮</option>
				<option>甜點</option>
				<option>沙拉</option>
				<option>麵包</option>
				<option>湯類</option>
				<option>飲料</option>
				<option>醬料</option>
				<option>其他</option>
            </select>
			<select id="items"class="form-control">
				<option selected>請選擇</option>
						
				<option> </option>
			</select>
            <br />
			
            <button class="btn btn-success btn-block" id="sure">確定</button>
        </div>
    </div>
</body>
</html>
