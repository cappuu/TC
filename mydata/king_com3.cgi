
sub KING_COM3 {

	if($in{'sel'} eq ""){&ERR("�Ӹ� ��밡 �Էµ��� �ʾҽ��ϴ�.");}
	if($in{'type'} eq ""){&ERR("����� �Էµ��� �ʾҽ��ϴ�.");}
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN("$kcon");
	&TIME_DATA;

	open(IN,"./charalog/main/$in{'sel'}.cgi") || &ERR("�� ID�� �������� �ʽ��ϴ�.");
	@E_DATA = <IN>;
	close(IN);

	($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);

	if($econ ne $kcon){
		&ERR("���� �ٸ��ϴ�.");
	}


	if($x0 ne $eid && $x1 ne $eid && $x2 ne $eid && $x3 ne $eid && $x4 ne $eid && $x5 ne $eid && $x6 ne $eid && $x7 ne $eid && $x8 ne $eid && $x9 ne $eid && $x10 ne $eid && $x11 ne $eid && $x12 ne $eid && $x13 ne $eid && $x14 ne $eid && $x15 ne $eid && $x16 ne $eid && $x17 ne $eid && $x18 ne $eid && $x19 ne $eid && $x20 ne $eid && $x21 ne $eid && $x22 ne $eid && $x23 ne $eid && $x24 ne $eid && $x25 ne $eid && $x26 ne $eid){
	
	if($in{'type'} eq "0" && $xking eq $kid){
		$x0 = $eid;
		$tname = "����";
	}elsif($in{'type'} eq "1" && $xking eq $kid){
		$x1 = $eid;
		$tname = "���屺";
	}elsif($in{'type'} eq "2" && $x1 eq $kid){
		$x2 = $eid;
		$tname = "ǥ���屺";
	}elsif($in{'type'} eq "3" && $x1 eq $kid){
		$x3 = $eid;
		$tname = "�ű��屺";
	}elsif($in{'type'} eq "4" && $x1 eq $kid){
		$x4 = $eid;
		$tname = "���屺";
	}elsif($in{'type'} eq "5" && $x2 eq $kid){
		$x5 = $eid;
		$tname = "�����屺";
	}elsif($in{'type'} eq "6" && $x2 eq $kid){
		$x6 = $eid;
		$tname = "�����屺";
	}elsif($in{'type'} eq "7" && $x2 eq $kid){
		$x7 = $eid;
		$tname = "�����屺";
	}elsif($in{'type'} eq "8" && $x2 eq $kid){
		$x8 = $eid;
		$tname = "�����屺";
	}elsif($in{'type'} eq "9" && $x3 eq $kid){
		$x9 = $eid;
		$tname = "�����屺";
	}elsif($in{'type'} eq "10" && $x3 eq $kid){
		$x10 = $eid;
		$tname = "�����屺";
	}elsif($in{'type'} eq "11" && $x3 eq $kid){
		$x11 = $eid;
		$tname = "�����屺";
	}elsif($in{'type'} eq "12" && $x3 eq $kid){
		$x12 = $eid;
		$tname = "�����屺";
	}elsif($in{'type'} eq "13" && $x4 eq $kid){
		$x13 = $eid;
		$tname = "�ȵ��屺";
	}elsif($in{'type'} eq "14" && $x4 eq $kid){
		$x14 = $eid;
		$tname = "�ȼ��屺";
	}elsif($in{'type'} eq "15" && $x4 eq $kid){
		$x15 = $eid;
		$tname = "�ȳ��屺";
	}elsif($in{'type'} eq "16" && $x4 eq $kid){
		$x16 = $eid;
		$tname = "�Ⱥ��屺";
	}elsif($in{'type'} eq "17" && $xking eq $kid){
		$x17 = $eid;
		$tname = "�»�";
	}elsif($in{'type'} eq "18" && $x17 eq $kid){
		$x18 = $eid;
		$tname = "�º�";
	}elsif($in{'type'} eq "19" && $x17 eq $kid){
		$x19 = $eid;
		$tname = "�»�";
	}elsif($in{'type'} eq "20" && $x17 eq $kid){
		$x20 = $eid;
		$tname = "�º�";
	}elsif($in{'type'} eq "21" && $x18 eq $kid){
		$x21 = $eid;
		$tname = "�����";
	}elsif($in{'type'} eq "22" && $x18 eq $kid){
		$x22 = $eid;
		$tname = "����";
	}elsif($in{'type'} eq "23" && $x19 eq $kid){
		$x23 = $eid;
		$tname = "�̺λ�";
	}elsif($in{'type'} eq "24" && $x19 eq $kid){
		$x24 = $eid;
		$tname = "ȣ�λ�";
	}elsif($in{'type'} eq "25" && $x20 eq $kid){
		$x25 = $eid;
		$tname = "���λ�";
	}elsif($in{'type'} eq "26" && $x20 eq $kid){
		$x26 = $eid;
		$tname = "���λ�";
	}else{&ERR("�� ������ �Ӹ��� �ź��� �ƴմϴ�.");}
	}else{&ERR("�ش������ �̹� �ٸ� ������ ������ �ֽ��ϴ�.");}

	$xsub = "$x0,$x1,$x2,$x3,$x4,$x5,$x6,$x7,$x8,$x9,$x10,$x11,$x12,$x13,$x14,$x15,$x16,$x17,$x18,$x19,$x20,$x21,$x22,$x23,$x24,$x25,$x26,$xxsub1,$xxsub2,";

	&COUNTRY_DATA_INPUT;
	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$tname�� $ename�� �Ӹ��߽��ϴ�.</h2><p>
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