
sub MAKE_UNIT {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xcid eq "0"){&ERR("재야인사는 실행할 수 없습니다.");}
	if($in{"name"} eq "재야" || $in{"name"} eq ""){&ERR("그 이름은 붙일 수 없습니다.");}
	elsif($in{'name'} eq "" || length($in{'name'}) < 4 || length($in{'name'}) > 16) { &ERR("부대명은 2문자 이상, 8문자 이하로 입력해주세요."); }
	elsif(length($in{'mes'}) > 40) { &ERR("부대 모집 코멘트는 20문자 이하로 입력해 주세요."); }
	if($kgold<1000){&ERR("금이 충분하지 않습니다.");}
	$kgold-=1000;

	open(IN,"$UNIT_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
	@UNI_DATA = <IN>;
	close(IN);

	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if($in{"name"} eq "$uunit_name"){&ERR("그 이름은 이미 존재합니다.");}
		if("$unit_id" eq "$kid"){&ERR("부대장은 부대를 작성할 수 없습니다.<BR>1번 부대를 해산시켜 주십시오.");}
		if("$uid" eq "$kid"){&ERR("부대에 소속해 있는 경우는 부대를 작성할 수 없습니다. 부대로부터 탈퇴해 주세요.");}
	}

	if($kcex < ($READER_POINT * 10)){$pass = 0;}else{$pass = int($kcex / 10);}
	unshift(@UNI_DATA,"$kid<>$in{'name'}<>$kcon<>1<>$kid<>$kname<>$kchara<>$in{'mes'}<>0<>0<>\n");
	open(OUT,">$UNIT_LIST") or &ERR('UNIT1 새로운 데이터를 기입할 수 없습니다.');
	print OUT @UNI_DATA;
	close(OUT);

	if($kcodea =~ /B2/){
		$kqpoint = 1;
	}

	&CHARA_MAIN_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$in{"name"}부대를 작성했습니다.</h2><p>

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