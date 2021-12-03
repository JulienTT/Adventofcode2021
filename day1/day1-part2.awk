{n[NR]=$1}
END{
    print "NR ="NR;
    for(i=1;i<=NR-2;i++){
	m[i]=n[i]+n[i+1]+n[i+2];
	if(i>1&&m[i]>m[i-1])
	    nb++;
    }
    print nb;
}
