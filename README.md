

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/thiagobucca/bucalarm-iot">
    <img src="images/appIcon.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">BucAlarm</h3>

  <p align="center">
    Minimalist Alarm Control App
    <br />
  </p>
</p>


<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/thiagobucca/bucalarm-iot)

The idea behind this project, is to make a very minimalist security Home Alarm control smart button.
Here i use ESP32 based M5Stick-C device to connect to the Alarm backend and toggle the alarm state.
This is especially useful when i don't have my phone next to me or it ran out of battery.


More Details here: [Backend](https://github.com/thiagobucca/bucalarm-api)
                   [Frontend](https://github.com/thiagobucca/bucalarm-ui)


### Built With

* [MicroPython](https://micropython.org/)
* [M5Stick-C](https://m5stack.com/products/stick-c)
* [UiFlow](https://flow.m5stack.com/)


### Running

1. Clone the repo
   ```sh
   git clone https://github.com/thiagobucca/bucalarm-iot.git
   ```
2. Use M5Burner to burn latest UIFlow to your stick
   ```sh
   https://m5stack.com/pages/download
   ```
3. Enter UIFlow by connecting with generated API KEY
   ```sh
   https://flow.m5stack.com/
   ```
4. Set your Wi-Fi credentials and backend IP in the main script
   ```sh
   alarm.py
   ```
4. Paste alarm.py script in Python block


<!-- LICENSE -->
## License

Distributed under the GNU License. See `LICENSE` for more information.

<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: images/screenshots.png