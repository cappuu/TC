
sub KING_COM2 {

	if($in{'mes'} eq ""){&ERR("������ �Էµ��� �ʾҽ��ϴ�.");}
	if(length($in{'mes'}) > 100) { &ERR("������ ���� 50 ���� ���Ϸ� �Է��� �ּ���."); }
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xking ne $kid && $x0 ne $kid){&ERR("���̳� ���� �ƴϸ� ������ �� �����ϴ�.");}

	if($xking eq $kid){
		$add = "����";
	}elsif($x0 eq $kid){
		$add = "����";
	}

	$xmes = "$in{'mes'}($add $kname��)";
	&COUNTRY_DATA_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>������ �Է��߽��ϴ�.</h2><p>
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