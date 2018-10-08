rm *frames*

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
cp itergeo/$q/$num.z .
python xyz_matrix_maker.py $num.z
rm $num.z
mv results/$num.xyz itergeo/$q/$num.xyz
done
done

for q in Me- Me+ Transoid
do
for num in {0..100}
do
cat itergeo/$q/$num.xyz >> ./$q\_all_frames.xyz
mv itergeo/$q/$num.xyz itergeo/$q/$q\_$num.xyz
done
done
