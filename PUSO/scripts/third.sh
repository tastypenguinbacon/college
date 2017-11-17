NOT_THREE=$(seq 10000 99999 | grep 5 | grep 6 | grep -v 3 | paste -sd+ | bc)
NOT_FIVE=$(seq 10000 99999 | grep 3 | grep 6 | grep -v 5 | paste -sd+ | bc)
NOT_SIX=$(seq 10000 99999 | grep 5 | grep 3 | grep -v 6 | paste -sd+ | bc)

SUM=$(echo $NOT_SIX+$NOT_FIVE+$NOT_THREE | bc)
echo $SUM

