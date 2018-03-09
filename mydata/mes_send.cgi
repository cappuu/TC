
sub MES_SEND {

	if($in{'message'} eq "") { &ERR("메세지가 기입되어 있지 않습니다."); }
	if($in{'mes_id'} eq "") { &ERR("상대가 지정되어 있지 않습니다."); }
	if(length($in{'message'}) > 200) { &ERR("편지는 전각 100문자 이하로 입력해주세요."); }
	&CHARA_MAIN_OPEN;
	if($in{'mes_id'} eq "$kid") { &ERR("자신에게는 보낼 수 없습니다."); }
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	$mes_id = $in{'mes_id'};

    &F_LOCK;
	&TIME_DATA;

	$bum = length($mes_id);

	open(IN,"$MESSAGE_LIST") or &ERR('파일을 열지 않았습니다.');
	@MES_REG = <IN>;
	close(IN);

	&GWAN1;

	
	if($in{'mes_id'} eq "111"){
		$jname = "$zname";
	}elsif($in{'mes_id'} eq "333"){

		open(IN,"$UNIT_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
		@UNI_DATA = <IN>;
		close(IN);

		$uhit=0;
		foreach(@UNI_DATA){
			($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
			if("$uid" eq "$kid"){$uhit=1;last;}
		}
		if(!$uhit || "$xcid" eq "0"){&ERR("재야는 부대에 보낼 수 없습니다.");}
		$jname = "$uunit_name 부대";
		$hunit = $unit_id;
		if($unit_id eq $kid){
		$u_add ="<font color=FFCC33><B>[대장]</b></font>";
		}else{
		$u_add ="<font color=33CCFF><B>[대원]</b></font>";
		}
	}elsif($bum < 4){
		$jname = "$cou_name[$mes_id]국";
							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /서신/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth월 : $qtalkd");
										}
									}	
								}
							}



	if($kcodea =~ /A4/ && $in{'message'} =~ /흑칠랑 사랑해/){
		$kqpoint = 1;
	}
	}else{
		open(IN,"./charalog/main/$in{'mes_id'}.cgi");
		@C_DATA = <IN>;
		close(IN);
		($jid,$jpass,$jname) = split(/<>/,$C_DATA[0]);
	if($kcodea =~ /A1/ && $in{'message'} =~ /안녕하세요 만나서 반갑습니다/){
		$kqpoint = 1;
	}
	}

	$mes_num = @MES_REG;

	if($mes_num > $MES_MAX) { pop(@MES_REG); }

	unshift(@MES_REG,"$in{'mes_id'}<>$kid<>$kpos<>$kname<>$u_add$in{'message'}<>$jname<>$daytime<>$kchara<>$kcon<>$hunit<>$rank_mes<>\n");

	open(OUT,">$MESSAGE_LIST") or &ERR('파일을 열지 않았습니다.');
	print OUT @MES_REG;
	close(OUT);

	&UNLOCK_FILE();



	&CHARA_MAIN_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$jname에게 서신을 보냈습니다.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="확인"></form></CENTER>
EOM
	&FOOTER;

	exit;

}
1;