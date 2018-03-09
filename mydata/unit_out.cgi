
sub UNIT_OUT {

	&CHARA_MAIN_OPEN;

	if($in{'did'} eq $kid){&ERR("자신은 해고할 수 없습니다.");}

	open(IN,"$UNIT_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
	@UNI_DATA = <IN>;
	close(IN);

	$mhit=0;$hit=0;@NEW_UNI_DATA=();
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if("$unit_id" eq "$kid"){
			$hit=1;
			last;
		}
	}

	if(!$hit){
		&ERR("대장 이외에 실행할 수 없습니다.");
	}

	@NEW_UNI_DATA=();
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
			if("$uid" eq "$in{'did'}"){
				open(IN,"./charalog/main/$in{'did'}.cgi");
				@E_DATA = <IN>;
				close(IN);
				($eid,$epass,$ename) = split(/<>/,$E_DATA[0]);
				$mess = "$uunit_name 부대로부터 $ename를 해고했습니다.";
			}else{
				push(@NEW_UNI_DATA,"$_");
			}
	}

	open(IN,"$MESSAGE_LIST") or &ERR('파일을 열지 않았습니다.');
	@MES_REG = <IN>;
	close(IN);

	$mes_num = @MES_REG;
	if($mes_num > $MES_MAX) { pop(@MES_REG); }
	unshift(@MES_REG,"$unit_id<>$kid<>$kpos<>$kname<><font color=FF0000>정보 : $mess<>$uname<>$daytime<>$kchara<>$kcon<>0<>\n");

	$mes_num = @MES_REG;
	if($mes_num > $MES_MAX) { pop(@MES_REG); }
	unshift(@MES_REG,"$eid<>$kid<>$kpos<>$kname<><font color=FF0000>정보 : $mess<>$ename<>$daytime<>$kchara<>$kcon<>0<>\n");
	open(OUT,">$MESSAGE_LIST") or &ERR('파일을 열지 않았습니다.');
	print OUT @MES_REG;
	close(OUT);

	open(OUT,">$UNIT_LIST") or &ERR('UNIT3 새로운 데이터를 기입할 수 없습니다.');
	print OUT @NEW_UNI_DATA;
	close(OUT);

	&CHARA_MAIN_INPUT;

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$mess</h2><p>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="메뉴로 돌아온다"></form></CENTER>
EOM
	&FOOTER;
	exit;
}
1;