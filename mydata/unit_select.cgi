
sub UNIT_SELECT {

	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&COUNTRY_DATA_OPEN($kcon);


	open(IN,"$TOWN_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
	@TOWN_DATA = <IN>;
	close(IN);
	foreach(@TOWN_DATA){
		($zcid,$zname,$zele,$zcon,$zmoney,$zmes)=split(/<>/);
		if("$zcid" eq "$in{town}"){last;}
	}

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


	open(IN,"$UNIT_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
	@UNI_DATA = <IN>;
	close(IN);

	@UNI_DATA2 = @UNI_DATA;
	$i=0;

	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
	foreach(@CL_DATA) {
	($aid,$apass,$aname,$achara,$astr,$aint,$alea,$acha,$asol,$agat,$acon,$agold,$arice,$acex,$aclass,$aarm,$abook,$abank,$asub1,$asub2,$apos,$ames,$ahost,$adate,$amail,$aos) = split(/<>/);
			if($uid eq "$kid" && $unit_id eq "$aid"){
			$com_list = "";
				open(IN,"./charalog/command/$aid.cgi");
				@COM_DATA = <IN>;
				close(IN);
				for($i=0;$i<$MAX_COM;$i++){
					($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/,$COM_DATA[$i]);
					$no = $i+1;
					if($cid eq ""){
					$com_list .= "$no: - <BR>";
					}else{
					$com_list .= "$no:$cname<BR>";
					}
					if($i>=23){last;}
				}
			}
	if($unit_id eq $aid){
	($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/,$TOWN_DATA[$apos]);
	$good = int($acha/8);
	}
	}

		if("$ucon" eq "$kcon" && $ureader){

			$unit_num=0;
			$unit_list = "$uname";

			if($uid eq $kid){
				foreach(@UNI_DATA2){
					($unit_id2,$uunit_name2,$ucon2,$ureader2,$uid2,$uname2,$uchara2,$umes2,$uflg2)=split(/<>/);
					if("$unit_id" eq "$unit_id2" && !$ureader2){
						$unit_list .= ",<a href=\"javascript:info('$uid2')\">$uname2</a>";
						$unit_num++;
						$u_member .= "<option value=$uid2><a href=\"javascript:info('$uid2')\">$uname2</a>";
					}
				}

			}else{
				foreach(@UNI_DATA2){
					($unit_id2,$uunit_name2,$ucon2,$ureader2,$uid2,$uname2,$uchara2,$umes2,$uflg2)=split(/<>/);
				open(IN,"./charalog/main/$uid2.cgi");
				@GOODA = <IN>;
				close(IN);
				($bid,$bpass,$bname,$bchara,$bstr,$bint,$blea,$bcha,$bsol,$bgat,$bcon,$bgold,$brice,$bcex,$bclass,$barm,$bbook,$bbank,$bsub1,$bsub2,$bpos,$bmes,$bhost,$bdate,$bmail,$bos) = split(/<>/,$GOODA[0]);
					if("$unit_id" eq "$unit_id2" && !$ureader2){
						if($bsol >= 500){
						$unit_list .= ",<a href=\"javascript:info('$uid2')\">$uname2</a>[X]";
						}else{
						$unit_list .= ",<a href=\"javascript:info('$uid2')\">$uname2</a>";
						}
						$unit_num++;
					}
				}
			}
			if($uflg eq "1"){
				$u_mes = "입대거부";
			}else{
				$u_mes = "입대승낙";
			}
			$unit_party .= "<TR><TD bgcolor=$TD_C3><input type=radio name=unit_id value=$unit_id></TD><TD bgcolor=$TD_C2><img src=\"$IMG/$uchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$uname\"></TD><TD bgcolor=$TD_C1><center><b>$uunit_name부대</b><BR>부대장 : <a href=\"javascript:info('$uid')\">《$uname》</a><br>위치:$zname성</TD><td bgcolor=$TD_C1>$unit_list</td><td bgcolor=$TD_C2><center>$unit_num / <font color=red>$good</font></td><td bgcolor=$TD_C2>$umes</td><TD bgcolor=$TD_C1><center>$u_mes</TD></tr>";
		}

		if($uid eq $kid){
			$k_hit=1;
			$kunit_name = $uunit_name;
		}
	}

	if(!$k_hit){
		$kunit_name = "없음";
	}

	if($xking eq $kid || $x0 eq $kid || $x1 eq $kid || $x2 eq $kid|| $x3 eq $kid || $x4 eq $kid || $x5 eq $kid ||$x6 eq $kid ||$x7 eq $kid ||$x8 eq $kid || $x9 eq $kid || $x10 eq $kid|| $x11 eq $kid || $x12 eq $kid || $x13 eq $kid || $x14 eq $kid || $x15 eq $kid || $x16 eq $kid || $x17 eq $kid || $x18 eq $kid || $x19 eq $kid || $x20 eq $kid || $x21 eq $kid || $x22 eq $kid || $x23 eq $kid || $x24 eq $kid || $x25 eq $kid || $x26 eq $kid){
		$come ="<input type=submit value=부대창설>";
		}else{$come = "국가수뇌부들만 창설할 수 있습니다.";}


	&HEADER;

	print <<"EOM";
<table width="100%" cellpadding="0" cellspacing="0" border=0><tr><td>
<TABLE WIDTH="100%" border=0>
<TBODY><TR>
<TD BGCOLOR=$ELE_BG[$kele] WIDTH=100% height=5> <font color=$ELE_C[$kele] size=4>　　　＜＜<B> * 부대 배속·편성*</B>＞＞</font></TD>
</TR><TR>
<TD bgcolor=$TD_C4 height=5>
<TABLE border="0"><TBODY>
<TR>
<TD bgcolor=$TD_C2>$simg</TD>
<TD bgcolor=$TD_C3>$timg</TD>
<TD bgcolor=$TD_C4 WIDTH=100% align=center>
<table cellpadding="0" cellspacing="0" border=0><tr><td bgcolor=993300>
<TABLE border="0" cellspacing="2">
<TBODY>
<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>무력</TD><TH>$kstrt</TH><TD>지력</TD><TH>$kintt</TH><TD>통솔력</TD><TH>$kleat</TH></TR>
<TR><TD>금</TD><TH>$kgold</TH><TD>쌀</TD><TH>$krice</TH><TD>공헌</TD><TH>$kcex</TH></TR>
<TR><TD><center>$kname</TD><TH colspan=2></TH><TD>병사</TD><TH>$ksol</TH><TD>훈련</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</td></tr></table>
</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD height="5">
<TABLE  border="0"><TBODY>
<TR><TD width="100%" bgcolor=$TALK_BG><font color=$TALK_FONT><center>여기에서는 자국이 소속하는 부대를 배속할 수가 있습니다.<BR> 부대에 소속하면 부대 채팅이나 집합 커맨드로 통제를 하기 쉬워집니다.<br>당신은 현재 <font color=red>$kunit_name</font> 부대에 소속해 있습니다.<BR>부대창설은 고위수뇌부들만 할 수 있고 가입은 누구나 할 수 있습니다.<br>부대창설비는 <font color=red>금 1000 괴</font>입니다.<br>부대장은 모집가능인원을 자신의 매력/8 만큼 모집할 수 있습니다.<br>집합시 집합원들은 피로도가 올라가게 되며 병력 500명이상 가지고 있는 부대원들은 집합할 수 없습니다.</font></TD>
<TD bgcolor=$TD_C4></TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD><BR><BR>
<form action="$FILE_MYDATA" method="post">
<CENTER><TABLE bgcolor=$TABLE_C><TBODY><TR>
<TD bgcolor=$TD_C3>선택</TD><TD bgcolor=$TD_C2><center>대장</TD><TD bgcolor=$TD_C1><center>부대명</TD><TD bgcolor=$TD_C1><center>배속된 부대원들</TD><TD bgcolor=$TD_C1><center>부대원/모집가능</TD><TD bgcolor=$TD_C2><center>부대 모집 메세지</TD><TD bgcolor=$TD_C1><center>입대접수여부</TD></TR>
EOM


print <<"EOM";
$unit_party
</TR></TBODY></TABLE></CENTER>
자신의 부대장의 턴<br>$com_list
<BR>
<center><input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=UNIT_ENTRY>
<input type=submit value="해당 부대에 소속됩니다."></form>
<HR size=0>
<h3><font color=3355AA><img src="$IMG/b6.gif"></h3>

<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=UNIT_CHANGE>
<input type=submit value="입대 거부·허가"></form>
* 실행하면 다른 사람은 그 부대에 입대할 수 없게 됩니다.<p>

<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<select name=did>$u_member</select>
<input type=hidden name=mode value=UNIT_OUT>
<input type=submit value="부대원 해고"></form>
* 실행하면 그 부대원은 퇴출당합니다.<p>


<HR size=0>

<b class=\"clit\"><img src="$IMG/b7.gif">
<form action="$FILE_MYDATA" method="post">
<TABLE bgcolor=$TABLE_C><TR><TD bgcolor=$TD_C3><center>부대명</TD><TD bgcolor=$TD_C2><input type=text name=name size=30><BR>[전각 대문자로 2~8문자 이내]</TD></TR>
<TD bgcolor=$TD_C3>부대 모집의 코멘트</TD><TD bgcolor=$TD_C2><input type=text name=mes size=30><BR>[전각 대문자로 0~20 문자 이내]</TD>
</TABLE>
<br>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=MAKE_UNIT>
<font color=red>$come</font></form>
<HR size=0>
<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=UNIT_DELETE>
<input type=submit value="부대 탈퇴 & 해산"></form>
<HR size=0>


<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="메뉴로 돌아온다"></form>
</TD>
</TR>
</TBODY></TABLE>
</td></tr></table>
EOM

	&FOOTER;
	exit;
}
1;