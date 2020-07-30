#!/bin/bash

sudo hciconfig hci0 down
sudo hciconfig hci0 up
sudo bluetoothctl <<EOF
scan on
remove fa:d9:1d:ed:cf:53
pair fa:d9:1d:ed:cf:53
EOF
