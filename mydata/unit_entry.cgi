
sub UNIT_ENTRY {

	&CHARA_MAIN_OPEN;
   	&COUNTRY_DATA_OPEN("$kcon");

	if($xcid eq "0"){&ERR("재야인사는 실행할 수 없습니다.");}
	if($in{'unit_id'} eq "") { &ERR("소속하는 부대가 선택되어 있지 않습니다."); }

	open(IN,"$UNIT_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
	@UNI_DATA = <IN>;
	close(IN);

	@UNI_DATA2 = @UNI_DATA;

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("파일 오픈 에러!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	foreach(@CL_DATA) {
	($aid,$apass,$aname,$achara,$astr,$aint,$alea,$acha,$asol,$agat,$acon,$agold,$arice,$acex,$aclass,$aarm,$abook,$abank,$asub1,$asub2,$apos,$ames,$ahost,$adate,$amail,$aos) = split(/<>/);
		if($in{'unit_id'} eq $aid){$jung = int($acha/8);}
	}

	$hit=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if($uid eq $kid){&ERR("이미 $uunit_name 부대에 소속해 있습니다.");}
	}

	$hit=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if($unit_id eq $in{'unit_id'}){last;}
	}

	$unit_num = 1;
	foreach(@UNI_DATA2){
	($unit_id2,$uunit_name2,$ucon2,$ureader2,$uid2,$uname2,$uchara2,$umes2,$uflg2)=split(/<>/);
		if("$unit_id" eq "$unit_id2" && !$ureader2){
		$unit_num++;
		}
	}

	if($jung < $unit_num){&ERR("부대장의 매력치가 부대원을 받아들이는데 모자릅니다. [부대한계가입 : $jung명]");}

	if($uflg){
		&ERR("입대 거부가 되었습니다.");
	}

	if(!$hit){
		unshift(@UNI_DATA,"$unit_id<>$uunit_name<>$kcon<>0<>$kid<>$kname<>$kchara<>$umes<>$uflg<>\n");
		open(IN,"$MESSAGE_LIST") or &ERR('파일을 열지 않았습니다.');
		@MES_REG = <IN>;
		close(IN);

		$mes_num = @MES_REG;

		if($mes_num > $MES_MAX) { pop(@MES_REG); }
		unshift(@MES_REG,"$unit_id<>$kid<>$kpos<>$kname<><font color=00FF00>정보 : $kname님이 $uunit_name 부대에 입대했습니다.<>$uunit_name부대<>$daytime<>$kchara<>$kcon<>0<>\n");

		open(OUT,">$MESSAGE_LIST") or &ERR('파일을 열지 않았습니다.');
		print OUT @MES_REG;
		close(OUT);
	}

	open(OUT,">$UNIT_LIST") or &ERR('UNIT4 새로운 데이터를 기입할 수 없습니다.');
	print OUT @UNI_DATA;
	close(OUT);

	&CHARA_MAIN_INPUT;

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$uunit_name 부대에 입대했습니다.</h2><p>

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