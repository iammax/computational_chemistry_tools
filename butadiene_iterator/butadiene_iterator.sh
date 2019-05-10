rm final_animations/* 

for q in Me-.z Me+.z Transoid.z
do

python angle_fixer.py $q
python iteration_maker.py $q
done

echo "Done making z matrices for the iterations. Now converting to cartesian..."

for q in Me- Me+ Transoid
do
for num in {0..100}
do
echo $q $num
cp iterations/$q/$num.z .
python xyz_matrix_maker.py $num.z
rm $num.z
mv results/$num.xyz iterations/$q/$num.xyz
done
done

for q in Me- Me+ Transoid
do
for num in {0..100}
do
cat iterations/$q/$num.xyz >> ./final_animations/$q\_all_frames.xyz
mv iterations/$q/$num.xyz iterations/$q/$q\_$num.xyz
done
done
