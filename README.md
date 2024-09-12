# TLS-Handshake

1. Generate a private key: `openssl genrsa -out server.key 2048`.
2. Create a self-signed certificate: `openssl req -new -x509 -key server.key -out server.crt -days 365`.
3. Start the server in a terminal window: `python server.py`
4. Start the client in another terminal window: `python client.py`

## Recording communication with Wireshark
1. Open [Wireshark](https://www.wireshark.org/) and select `Loopback:lo` as the network interface, as we are working locally.
2. If you want to further reduce the amount of information displayed, you can set a filter on the port `8443` with `tcp.port == 8443`.
3. Start the recording in Wireshark, then server and client.
4. Stop data analysis.
5. Evaluate the result. The [Follow TCP Stream](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection.html) dialog can be useful for this.
7. Optional - Use TLS key: Go to Edit -> Preferences -> Protocols -> TLS and enter the path to the private key (server.key).
8. Optional - Specify pre-master secret log file: Specify path from client.py (premastersecret.log)