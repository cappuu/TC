
sub MAKE_UNIT {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xcid eq "0"){&ERR("����λ�� ������ �� �����ϴ�.");}
	if($in{"name"} eq "���" || $in{"name"} eq ""){&ERR("�� �̸��� ���� �� �����ϴ�.");}
	elsif($in{'name'} eq "" || length($in{'name'}) < 4 || length($in{'name'}) > 16) { &ERR("�δ���� 2���� �̻�, 8���� ���Ϸ� �Է����ּ���."); }
	elsif(length($in{'mes'}) > 40) { &ERR("�δ� ���� �ڸ�Ʈ�� 20���� ���Ϸ� �Է��� �ּ���."); }
	if($kgold<1000){&ERR("���� ������� �ʽ��ϴ�.");}
	$kgold-=1000;

	open(IN,"$UNIT_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@UNI_DATA = <IN>;
	close(IN);

	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if($in{"name"} eq "$uunit_name"){&ERR("�� �̸��� �̹� �����մϴ�.");}
		if("$unit_id" eq "$kid"){&ERR("�δ����� �δ븦 �ۼ��� �� �����ϴ�.<BR>1�� �δ븦 �ػ���� �ֽʽÿ�.");}
		if("$uid" eq "$kid"){&ERR("�δ뿡 �Ҽ��� �ִ� ���� �δ븦 �ۼ��� �� �����ϴ�. �δ�κ��� Ż���� �ּ���.");}
	}

	if($kcex < ($READER_POINT * 10)){$pass = 0;}else{$pass = int($kcex / 10);}
	unshift(@UNI_DATA,"$kid<>$in{'name'}<>$kcon<>1<>$kid<>$kname<>$kchara<>$in{'mes'}<>0<>0<>\n");
	open(OUT,">$UNIT_LIST") or &ERR('UNIT1 ���ο� �����͸� ������ �� �����ϴ�.');
	print OUT @UNI_DATA;
	close(OUT);

	if($kcodea =~ /B2/){
		$kqpoint = 1;
	}

	&CHARA_MAIN_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$in{"name"}�δ븦 �ۼ��߽��ϴ�.</h2><p>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�޴��� ���ƿ´�"></form></CENTER>
EOM
	&FOOTER;
	exit;
}
1;