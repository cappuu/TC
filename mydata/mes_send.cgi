
sub MES_SEND {

	if($in{'message'} eq "") { &ERR("�޼����� ���ԵǾ� ���� �ʽ��ϴ�."); }
	if($in{'mes_id'} eq "") { &ERR("��밡 �����Ǿ� ���� �ʽ��ϴ�."); }
	if(length($in{'message'}) > 200) { &ERR("������ ���� 100���� ���Ϸ� �Է����ּ���."); }
	&CHARA_MAIN_OPEN;
	if($in{'mes_id'} eq "$kid") { &ERR("�ڽſ��Դ� ���� �� �����ϴ�."); }
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	$mes_id = $in{'mes_id'};

    &F_LOCK;
	&TIME_DATA;

	$bum = length($mes_id);

	open(IN,"$MESSAGE_LIST") or &ERR('������ ���� �ʾҽ��ϴ�.');
	@MES_REG = <IN>;
	close(IN);

	&GWAN1;

	
	if($in{'mes_id'} eq "111"){
		$jname = "$zname";
	}elsif($in{'mes_id'} eq "333"){

		open(IN,"$UNIT_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
		@UNI_DATA = <IN>;
		close(IN);

		$uhit=0;
		foreach(@UNI_DATA){
			($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
			if("$uid" eq "$kid"){$uhit=1;last;}
		}
		if(!$uhit || "$xcid" eq "0"){&ERR("��ߴ� �δ뿡 ���� �� �����ϴ�.");}
		$jname = "$uunit_name �δ�";
		$hunit = $unit_id;
		if($unit_id eq $kid){
		$u_add ="<font color=FFCC33><B>[����]</b></font>";
		}else{
		$u_add ="<font color=33CCFF><B>[���]</b></font>";
		}
	}elsif($bum < 4){
		$jname = "$cou_name[$mes_id]��";
							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /����/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth�� : $qtalkd");
										}
									}	
								}
							}



	if($kcodea =~ /A4/ && $in{'message'} =~ /��ĥ�� �����/){
		$kqpoint = 1;
	}
	}else{
		open(IN,"./charalog/main/$in{'mes_id'}.cgi");
		@C_DATA = <IN>;
		close(IN);
		($jid,$jpass,$jname) = split(/<>/,$C_DATA[0]);
	if($kcodea =~ /A1/ && $in{'message'} =~ /�ȳ��ϼ��� ������ �ݰ����ϴ�/){
		$kqpoint = 1;
	}
	}

	$mes_num = @MES_REG;

	if($mes_num > $MES_MAX) { pop(@MES_REG); }

	unshift(@MES_REG,"$in{'mes_id'}<>$kid<>$kpos<>$kname<>$u_add$in{'message'}<>$jname<>$daytime<>$kchara<>$kcon<>$hunit<>$rank_mes<>\n");

	open(OUT,">$MESSAGE_LIST") or &ERR('������ ���� �ʾҽ��ϴ�.');
	print OUT @MES_REG;
	close(OUT);

	&UNLOCK_FILE();



	&CHARA_MAIN_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$jname���� ������ ���½��ϴ�.</h2><p>
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