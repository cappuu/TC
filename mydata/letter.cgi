sub LETTER {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	&HEADER;
	print <<"EOM";
<form action="$FILE_MYDATA" method="post">
<CENTER><img src="$IMG/b5.gif">
<BR>
<BR>다른 장수에게 서신을 보낼 수 있습니다.<BR>
<font size=2>(* 욕설이나 비방이 담긴 글을 받은 분은 관리자에게 연락해주십시오. 관리자메일 : kjs503@anyang.ac.kr)</font><BR>
<BR>
<input type="text" name=message size=65><br>
<select name=mes_id>
<option value="">보내는 상대를 선택
EOM

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

	@tmp = map {(split /<>/)[10]} @CL_DATA;
	@CL_DATA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/);
		if($eid eq $kid) { next; }
		if($cou_name[$econ] eq ""){
			$con[0] .= "<option value=$eid>$ename\n";
		}else{
			$con[$econ] .= "<option value=$eid>$ename\n";
		}
	}

	open(IN,"$COUNTRY_LIST") or &ERR2('파일을 열지 않았습니다. err no :country');
	@COU_NO = <IN>;
	close(IN);
	
	foreach(@COU_NO){
		($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi,$xxat)=split(/<>/);
		print "<option>==== $xxname ====\n";
		print "$con[$xxcid]";
	}
	$c_num = @COU_DATA;
print <<"EOM";
<option>==== 재야인사 ====\n
$con[0]
</select>
<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>
<input type=hidden name=id value=$kid>
<input type=hidden name=name value=$kname>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=MES_SEND>
<input type=submit value="서신을 보낸다"><br>
</form>
<HR size=0>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="메뉴로 돌아온다"></form>
EOM
	&FOOTER;
	exit;

}
1;