for i in ../www/ger/*json
do
    mv $i $i.back
    ./sort-json.py $i.back > $i
done
