$1~/down/ {aim+=$2}
$1~/up/ {aim-=$2}
$1~/forward/ {h+=$2;d+=aim*$2}
END {print h,d,h*d}


