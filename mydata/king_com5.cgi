
sub KING_COM5 {

	if($in{'mes'} eq ""){&ERR("������ �Էµ��� �ʾҽ��ϴ�.");}
	if(length($in{'mes'}) > 100) { &ERR("������ ���� 50 ���� ���Ϸ� �Է��� �ּ���."); }
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	open(IN,"$COUNTRY_MES");
	@C_MES = <IN>;
	close(IN);

	if($xking eq $kid){
		$add = "����";
	}elsif($x0 eq $kid){
		$add = "����";
	}

	@NEW_C_MES=();
	foreach(@C_MES){
		($mes,$cno)=split(/<>/);
		if($cno eq $kcon){
			$chit=1;
			push(@NEW_C_MES,"$in{'mes'}($add $kname��)<>$kcon<>\n");
		}else{
			push(@NEW_C_MES,"$_");
		}
	}

	if(!$chit){
		unshift(@NEW_C_MES,"$in{'mes'}($add $kname��)<>$kcon<>\n");
	}

	open(OUT,">$COUNTRY_MES");
	print OUT @NEW_C_MES;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>�������� �ۼ��߽��ϴ�.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="Ȯ��"></form></CENTER>
EOM

	&FOOTER;

	exit;

}
1;