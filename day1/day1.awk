NR==1 {n=$1}
NR>1 { if($1>n) {m++};print $1,n,m;n=$1; }
END{print m}
