# Read from the file file.txt and output the tenth line to stdout.
count=`wc -l file.txt | awk '{print $1}'`
if [ $count -lt 10 ];then
    echo ""
else
    head -10 file.txt | tail -1
fi
