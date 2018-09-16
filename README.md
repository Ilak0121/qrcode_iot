<h2>QR CODE Scanning and json server synchronize</h2>

<h3>this is the source codes for qr code scanning and iot project.</h3>

<h3>main directory</h3>
<p>1.main.py : main python program for iot device. scan and find, decode qrcode using webcam for promised QR code. after scanning, insert the data to local database. after database query. use backup python module to send server databse dump file</p>
<p>2.qrscan.py : qr code scanning module for scan qr code and decode.</p>
<p>3.imagescan.py : scanning QR code image file as argument of '-i' and decoding print program</p>
</br>

<h3>monitoring directory</h3>
<p>1.monitoring.c : background program for monitoring file change of sql dump file. if there is a change, write the timestamp of file to log.txt and load the data dump to server databse</p>
<p>2.load.c : loading database dump file to database</p>
</br>

<h3>midle_server directory</h3>
<p>1.dbcon.php : database connection php file</p>
<p>2.getjson.php : load database data and serve as json fomat</p>
</br>

<h3>QR code has 3 information about the code.</h3>
1. type
2. data
3. location

