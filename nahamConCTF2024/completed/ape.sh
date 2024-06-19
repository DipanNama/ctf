state=$(<theflag)
for i in {1..50}; do
	echo $i
	echo " "
	
   state=$(<<<"$state" base64 --decode)
done
echo "$state"
