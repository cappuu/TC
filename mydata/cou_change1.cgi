
sub COU_CHANGE {

	if($in{'sel'} eq "") { &ERR("���õ��� �ʾҽ��ϴ�."); }
	if($in{'hcon'} eq "$kcon") { &ERR("�ڱ��Դϴ�."); }

	if($REFREE){
		$r_str = length("$SANGOKU_URL");
		$r_url = substr("$ENV{'HTTP_REFERER'}", 0, $r_str);
	}

	$sel = $in{'sel'};
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($zcon);

	&TIME_DATA;

	if($sel){
		$egold += 100;
		$epos = $in{'hpos'};
		$econ = $in{'hcon'};
		$res_mes = "$ename, $cou_name[$econ]������ �����ϴ�.";
		&MAP_LOG("<img src=$IMG/j16.gif> $ename, $cou_name[$econ]������ �����ϴ�.");
	}else{
		$res_mes = "$ename���� $kname���� �Ӱ��� ������� �ʾҽ��ϴ�.";
	}

	open(IN,"$MESSAGE_LIST2");
	@MES = <IN>;
	close(IN);

	@NEW_MES=();
	foreach(@MES){
		($pid,$hid,$hpos,$hname,$hmessage,$pname,$htime,$hchara,$hcon) = split(/<>/);
		if($in{'hcon'} eq $hcon && $in{'hpos'} eq $hpos && $pid eq $kid && $htime eq "9999"){
			open(IN,"./charalog/main/$hid\.cgi") or &ERR('�� ĳ���ʹ� ����� �� �����ϴ�.');
			@E_DATA = <IN>;
			close(IN);
			($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
			unshift(@NEW_MES,"$hid<>$kid<>$kpos<>$kname<>$res_mes<>$ename<>$daytime<>$kchara<>$kcon<>\n");
		}else{
			push(@NEW_MES,"$_");
		}
	}

	open(OUT,">$MESSAGE_LIST2");
	print OUT @NEW_MES;
	close(OUT);
	&CHARA_MAIN_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$res_mes</h2><p>
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