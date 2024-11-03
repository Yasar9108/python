import speedtest

class InternetSpeedChecker:
    def check_internet_speed(self):
        speed = speedtest.Speedtest()
        download_speed = speed.download() / 8000000  
        upld_speed = speed.upload() / 8000000       
        print(f"Download speed is: {download_speed:0.2f} MB")
        print(f"Upload speed is: {upld_speed:0.2f} MB")


ISC =InternetSpeedChecker()
ISC.check_internet_speed()        