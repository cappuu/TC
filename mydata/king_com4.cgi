
sub KING_COM4 {

	if($in{'sel'} eq "") { &ERR("���õ��� �ʾҽ��ϴ�."); }

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	$sel = $in{'sel'};
	open(IN,"./charalog/main/$sel\.cgi") or &ERR2('ID�� PASS�� �ùٸ��� �ʽ��ϴ�.');
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);	if($kcon ne "$econ") { &ERR("�ùٸ��� �ʴ� ó���Դϴ�."); }
	if($kid eq "$eid") { &ERR("�ùٸ��� ���� ó���Դϴ�."); }

	&TIME_DATA;

	open(IN,"$UNIT_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@UNI_DATA = <IN>;
	close(IN);

	$mhit=0;$hit=0;@NEW_UNI_DATA=();
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if("$uid" eq "$eid"){
			if($eid eq "$unit_id"){
				$mhit = 1;
				$mid = $unit_id;
			}elsif($eid eq "uid"){
			}
		}else{
			push(@NEW_UNI_DATA,"$_");
		}
	}

	if($mhit){
		@NEW_UNI_DATA=();
		foreach(@UNI_DATA){
			($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
			if("$mid" eq "$unit_id"){
			}else{
				push(@NEW_UNI_DATA,"$_");
			}
		}
	}


	open(OUT,">$UNIT_LIST") or &ERR('UNIT3 ���ο� �����͸� ������ �� �����ϴ�.');
	print OUT @NEW_UNI_DATA;
	close(OUT);

	open(IN,"$TOWN_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@TOWN_DATA = <IN>;
	close(IN);

	$dkjf=0;
	foreach(@TOWN_DATA){
	($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/);
			if($eid eq "$zbong1"){
			$zbong1 = "";
	splice(@TOWN_DATA,$dkjf,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
	open(OUT,">$TOWN_LIST") or &ERR('TOWN �����͸� ������ �� �����ϴ�.');
	print OUT @TOWN_DATA;
	close(OUT);
			}elsif($eid eq "$zbong2"){
			$zbong2 = "";
	splice(@TOWN_DATA,$dkjf,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
	open(OUT,">$TOWN_LIST") or &ERR('TOWN �����͸� ������ �� �����ϴ�.');
	print OUT @TOWN_DATA;
	close(OUT);
			}elsif($eid eq "$zbong3"){
			$zbong3 = "";
	splice(@TOWN_DATA,$dkjf,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
	open(OUT,">$TOWN_LIST") or &ERR('TOWN �����͸� ������ �� �����ϴ�.');
	print OUT @TOWN_DATA;
	close(OUT);
			}
	$dkjf++;
	}

	open(IN,"$TOWN_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@TOWN_DATA = <IN>;
	close(IN);

	$dkjf=0;
	foreach(@TOWN_DATA){
	($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/);
			if($eid eq "$zbong1"){
			$zbong1 = "";
	splice(@TOWN_DATA,$dkjf,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
	open(OUT,">$TOWN_LIST") or &ERR('TOWN �����͸� ������ �� �����ϴ�.');
	print OUT @TOWN_DATA;
	close(OUT);
			}elsif($eid eq "$zbong2"){
			$zbong2 = "";
	splice(@TOWN_DATA,$dkjf,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
	open(OUT,">$TOWN_LIST") or &ERR('TOWN �����͸� ������ �� �����ϴ�.');
	print OUT @TOWN_DATA;
	close(OUT);
			}elsif($eid eq "$zbong3"){
			$zbong3 = "";
	splice(@TOWN_DATA,$dkjf,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
	open(OUT,">$TOWN_LIST") or &ERR('TOWN �����͸� ������ �� �����ϴ�.');
	print OUT @TOWN_DATA;
	close(OUT);
			}
	$dkjf++;
	}

	if($sel){
		$econ = 0;
		$res_mes = "$ename�� $xname���κ��� �ذ�Ǿ����ϴ�.";
		&MAP_LOG("<img src=$IMG/j15.gif> $ename�� $xname�����κ��� �ذ�Ǿ����ϴ�.");
	}

	open(IN,"./log_file/black_list.cgi");
	@B_LIST = <IN>;
	close(IN);

	@NEW_B_LIST=();
	$hit=0;
	foreach(@B_LIST){
		($bid,$bcon,$bname,$bsub) = split(/<>/);
		if($bid eq $eid && $bcon eq $econ){
			$hit=1;
			push(@NEW_B_LIST,"$eid<>$econ<>$ename<><>\n");
		}else{
			push(@NEW_B_LIST,"$_");
		}
	}

	if(!$hit){
		unshift(@NEW_B_LIST,"$eid<>$econ<>$ename<><>\n");
	}

	open(OUT,">./log_file/black_list.cgi");
	print OUT @NEW_B_LIST;
	close(OUT);
	&ENEMY_INPUT;

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