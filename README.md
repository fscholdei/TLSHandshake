# TLS-Handshake

1. Starte den Server in einem Terminalfenster: `python server.py`
2. Starten den Client in einem anderen Terminalfenster: `python client.py`

## Kommunikation mit Wireshark aufzeichnen
Vorbedingung: [Wireshark](https://www.wireshark.org/) sollte auf dem System installiert sein.

1. Öffne Wireshark und wähle `Loopback:lo` als Netzwerkinterface aus, da wir lokal arbeiten. 
2. Soll die Menge der angezeigten Informationen weiter reduziert werden, kann mit `tcp.port == 8443` ein Filter auf den Port `8443` gesetzt werden.
3. Starte die Aufzeichnung in Wireshark, anschließend Server und Client.
4. Datenanalyse stoppen.
5. Ergebnis auswerten. Der [Follow TCP Stream](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection.html)-Dialog kann dabei nützlich sein.
7. Optional: TLS-Schlüssel verwenden, dazu unter Edit -> Preferences -> Protocols -> TLS und Pfad zu privaten Schlüssel angeben (server.key).
8. Optional: Pre-Master-Secret Log File angeben: Pfad aus client.py angeben (premastersecret.log)
