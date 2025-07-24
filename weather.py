import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel,QBoxLayout,QVBoxLayout,QLineEdit,QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor,QFontDatabase
import requests

class WeatherApp(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setGeometry(700, 450, 300, 100)
    self.setWindowTitle('Weather App')
    self.label=QLabel("Enter your city name",self)
    self.box=QLineEdit(self)
    self.submit=QPushButton("Get Weather",self)
    self.label1=QLabel(self)
    self.label2=QLabel(self)
    self.label3=QLabel(self)
    self.initUI()
    

  def initUI(self) :
    vbox=QVBoxLayout()
    vbox.addWidget(self.label)
    vbox.addWidget(self.box)
    vbox.addWidget(self.submit)
    vbox.addWidget(self.label1)
    vbox.addWidget(self.label2)
    vbox.addWidget(self.label3)
    self.setLayout(vbox)
    self.label.setAlignment(Qt.AlignCenter)
    self.box.setAlignment(Qt.AlignCenter)
    self.label1.setAlignment(Qt.AlignCenter)
    self.label2.setAlignment(Qt.AlignCenter)
    self.label3.setAlignment(Qt.AlignCenter)

    self.label.setObjectName("label")
    self.box.setObjectName("box")
    self.submit.setObjectName("submit")
    self.label1.setObjectName("label1")
    self.label2.setObjectName("label2")
    self.label3.setObjectName("label3")
    self.setStyleSheet("""QLabel,QPushButton{font-family:calibri;}
                       QLabel#label{font-size:40px;
                       font-style:itelaic;
                       }
                       QLineEdit#box{font-size:40px;}
                       QPushButton#submit{font-size:30px;}
                       QLabel#label1{font-size:75px;}
                       QLabel#label2{font-size:105px;
                       font-family:segoe UI emoji;}
                       QLabel#label3{font-size:75px;}
""")
    self.submit.clicked.connect(self.get_weather)
  def get_weather(self):

    city = self.box.text()
    api_key = "3e9273c009cc8dd2c0a7dd34920f84fe"
    url="https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try : 
      response=requests.get(url.format(city=city,api_key=api_key))
      response.raise_for_status()
      data=response.json()
      if data["cod"] == 200:
        self.dispaly_weather(data)
    except requests.exceptions.HTTPError as htpp_error:
      match response.status_code:
        case 400:
          self.error("Bad Request : \nThe request was invalid.")
        case 401:
          self.error("Unauthorized :\n The authentication details were invalid.")
        case 403:
          self.error("Forbidden :\n The server understood the request but refuses to authorize it.")
        case 404:
          self.error(" City Not Found :\n The server can not find the requested resource.")
        case 500:
          self.error("Internal Server Error :\n The server encountered an unexpected condition which prevented it from fulfilling ")
        case 502:
          self.error("Bade Gateway:\n Invalid HTTP response from the upstream server.")
        case 503:
          self.error("Service Unavailable :\nserver is currently unable to handle the request due to a temporary overload or scheduled maintenance.")
        case 504:
          self.error("Gateway Timout :\n Please check your internet")                    
        case _:
          self.error(f"An error occurred{htpp_error}") 
    except requests.exceptions.RequestException:
      self.error("Connection Error : \nPlease check your internet")
    except requests.exceptions.Timeout:
      self.error("Timeout Error :\n Please check your internet")
    except requests.exceptions.TooManyRedirects:
      self.error("Too Many Redirects :\n Please check your internet")
    except requests.exceptions.RequestException as e:
      self.error(f"An error occurred {e}")


                  
       
    

    


    
  def error(self,p):
    self.label1.setStyleSheet("font-size:20px;")
    self.label1.setText(p)
    self.label2.clear()
    self.label3.clear()
  def dispaly_weather(self,data):
    self.label1.setStyleSheet("font-size:75px;")
    da=(data["main"]["temp"]-273.3)
    self.label1.setText(f"{da:.2f}°C")
    weather_des=data["weather"][0]["description"]
    self.label3.setText(weather_des)
    self.label2.setText(self.get_emoji(data["weather"][0]["id"]))
        
  @staticmethod      
  def get_emoji(code):
    print(code)
    if 200<=code<=232:
      return "🌦️"
    elif 300<=code<=321:
      return "🌧️"
    elif 500<=code<=531:
      return "☁️"
    elif 600<=code<=622:
      return "❄️"
    elif 701<=code<=762:
      return "☀️"
    elif 800<=code<=804:
      return "☀️"
    else:
      return "😐"


  


 
    #self.time_update()

  # def time_update(self):
  #   current_time = QTime.currentTime()
  #   self.label.setText(current_time.toString('hh:mm:ss'))
     



def main():
  app = QApplication(sys.argv)
  window = WeatherApp()
  window.show()
  sys.exit(app.exec_())

if __name__=="__main__":
  main()