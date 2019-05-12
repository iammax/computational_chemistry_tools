rm final_animations/* 

for q in Me-.z Me+.z Transoid.z
do

python angle_fixer.py $q
python iteration_maker.py $q
done

echo "Done making z matrices for the iterations. Now converting to cartesian..."

for q in Me- Me+ Transoid
do
python mass_z_to_xyz.py $q.z
done

for q in Me- Me+ Transoid
do
for num in {0..100}
do
cat iterations/$q/$num.xyz >> ./final_animations/$q\_all_frames.xyz
done
done
