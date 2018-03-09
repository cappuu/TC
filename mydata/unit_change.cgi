
sub UNIT_CHANGE {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xcid eq "0"){&ERR("재야인사는 실행할 수 없습니다.");}

	open(IN,"$UNIT_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
	@UNI_DATA = <IN>;
	close(IN);

	$mhit=0;$hit=0;@NEW_UNI_DATA=();
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if("$uid" eq "$kid"){
			$hit=1;
			$uni_name = $uunit_name;
			if($uflg){
				$uflg = 0;
				$mess = "승낙";
			}else{
				$uflg = 1;
				$mess = "거부";
			}
			push(@NEW_UNI_DATA,"$unit_id<>$uunit_name<>$ucon<>$ureader<>$uid<>$uname<>$uchara<>$umes<>$uflg<>\n");
		}else{
			push(@NEW_UNI_DATA,"$_");
		}
	}

	if(!$hit){
		&ERR("대장 이외는 실행할 수 없습니다.");
	}

	open(OUT,">$UNIT_LIST") or &ERR('UNIT2 새로운 데이터를 기입할 수 없습니다.');
	print OUT @NEW_UNI_DATA;
	close(OUT);

	&CHARA_MAIN_INPUT;
	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$uni_name부대를 입대 [$mess]로 설정했습니다.</h2><p>

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