STOPPED=0
trap ctrl_c INT TERM

ctrl_c() {
    STOPPED=1
}

# If this file entry already exists, socat may complain
rm -f /tmp/testACM0

while [ $STOPPED -eq 0 ]; do
    socat PTY,LINK=/tmp/testACM0,raw TCP:192.168.56.1:12346
done
