VALID=$(echo $1 | grep [0-9] | grep -e [-@#\$%\&\*\+\=] | wc -c)

if [ $VALID -ge 8 ]
then
    echo 'OK'
else
    echo 'BAD'
fi

