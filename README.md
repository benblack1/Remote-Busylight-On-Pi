# Remote-Busylight-On-Pi

This application allows you to update a busylight based on your Microsoft Teams presence. It consists of two parts: 

1. The local application: This part runs on your machine and checks your Microsoft Teams presence status. It communicates with the Raspberry Pi to update the busylight accordingly.

2. The Raspberry Pi application: This part runs on the Raspberry Pi and listens for updates from the local application. It receives the presence status and updates the busylight accordingly.

To use this application, follow these steps:

1. Run the `local_main.py` script on your machine.
2. Run the `pi_main.py` script on the Raspberry Pi.
3. Ensure that the Raspberry Pi is connected to the busylight device.
4. The local application will periodically check your Microsoft Teams presence and send updates to the Raspberry Pi.
5. The Raspberry Pi application will receive the updates and update the busylight accordingly.

Please note that you need to have Microsoft Teams installed and configured on your machine for this application to work properly.