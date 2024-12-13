/[a-z]+\([^+]+[+]/  {tag= 1;}
tag == 0  {tag = 0;}
tag == 1 {print $0; tag= 0;}
