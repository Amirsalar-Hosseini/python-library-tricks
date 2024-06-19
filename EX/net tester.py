import speedtest
speed_test = speedtest.speedtest()
download_speed = speed_test.download()/(1024*1024)
upload_speed = speed_test.upload()/(1024*1024)
print('your download speed is ', download_speed, 'MB')
print('your upload speed is ', upload_speed, 'MB')