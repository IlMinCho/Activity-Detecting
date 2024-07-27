# Activity-Detecting, Live Sensor Streaming
![---------](https://github.com/user-attachments/assets/13a5ed9c-825b-46b6-bb17-c2eb24b6c742)
link: https://ilmincho.me/activity-detecting-mobile-sensing/


## `Note:`

Chrome seems to have the best performance on Windows. If the live update is not running well, changes the `MAX_DATA_POINTS` and/or `UPDATE_FREQ_MS` to improve performance.

---
## Prerequisite

### Mobile App:

We'll be using Sensorlogger (https://www.tszheichoi.com/sensorlogger) app for streaming:

For iOS: https://apps.apple.com/app/id1531582925

For Android: https://play.google.com/store/apps/details?id=com.kelvin.sensorapp&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1

The above link is also available at the app's website.

### PC:

You can download Anaconda (https://www.anaconda.com/) for python environment.

For Windows user, Windows Subsystem Linux can be used if configured correctly. 

The code requires `dash` python library, install by:

```
conda install dash
# or
pip install dash
```

---

### Example code:

The `sensor_logger.py` file contains the code to retrieve and display live sensor data.

```
python sensor_logger.py
```

You will see something like these on the command prompt:

```
Dash is running on http://0.0.0.0:8000/

 * Serving Flask app 'sensor_logger'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://192.168.212.126:8000
Press CTRL+C to quit
```

The line:

```
 * Running on http://192.168.212.126:8000
```

shows the IP address the server is running. set the same IP address on the senor logger app.


---

### Example Data Received

```
{"messageId":46,"sessionId":"c5ae-60-4-95-1917","deviceId":"62be-97-4f-a7-e06b",
    "payload":[
        {"name":"accelerometer","values":{"z":-0.1116943359375,"y":0.0022122859954833984,"x":-0.01123344898223877},"accuracy":3,"time":1675646835546228200},
        {"name":"gyroscope","values":{"z":-0.011682453565299511,"y":-0.00908635277301073,"x":0.020997874438762665},"accuracy":3,"time":1675646835546228200},
        {"name":"gravity","values":{"z":9.144111633300781,"y":3.5274763107299805,"x":0.33542969822883606},"accuracy":3,"time":1675646835546228200},
        {"name":"orientation","values":{"qz":0.9826133847236633,"qy":0.182196706533432,"qx":0.022537777200341225,"qw":0.02770204283297062,"roll":-0.03665274381637573,"pitch":-0.3675247132778168,"yaw":-3.092036247253418},"accuracy":3,"time":1675646835535921700},
        {"name":"magnetometer","values":{"z":-24.937501907348633,"y":-47.79375076293945,"x":0.75},"accuracy":3,"time":1675646835562376400},
        {"name":"barometer","values":{"relativeAltitude":0.03963470458984375,"pressure":1010.418212890625},"accuracy":3,"time":1675646835579372800},
        {"name":"microphone","time":1675646835513000000,"values":{"dBFS":-160}},
        {"name":"light","values":{"lux":30},"accuracy":3,"time":1675646835628545000},
         {"name":"accelerometeruncalibrated","time":1675649057981134600,"values":{"z":-0.5808258056640625,"y":-0.0010833740234375,"x":-0.8082275390625}},
        {"name":"magnetometeruncalibrated","time":1675649057982749700,"values":{"z":1542.572509765625,"y":-484.08282470703125,"x":-2455.663330078125}},
        {"name":"gyroscopeuncalibrated","time":1675649057989510700,"values":{"z":-0.005875465925782919,"y":0.014363492839038372,"x":-0.004509796854108572}},
        {"name":"microphone","time":1675649057793000000,"values":{"dBFS":-47.886932373046875}}
    ]
}
```

You may refer to function `data()` in `sensor_logger.py` on how the data is processed.
