#!/usr/bin/perl


require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR2("로딩중입니다. 잠시만 기다려 주십시오"); }
&DECODE;
$adminid = "관리자아이디1";
$adminpass = "관리자패스워드1";

$adminid2 = "관리자아이디2";
$adminpass2 = "관리자아이디2";

$adminid3 = "관리자아이디3";
$adminpass3 = "관리자아이디3";

if($mode eq 'CHANGE') { &CHANGE; }
elsif($mode eq 'CHANGE2') { &CHANGE2; }
elsif($mode eq 'MENTE') { &MENTE; }
elsif($mode eq 'MENTE1') { &MENTE1; }
elsif($mode eq 'MENTE2') { &MENTE2; }
elsif($mode eq 'QUEST_ENTRY') { &QUEST_ENTRY; }
elsif($mode eq 'QUEST_EDIT') { &QUEST_EDIT; }
elsif($mode eq 'QUEST_EDIT_COM') { &QUEST_EDIT_COM; }
elsif($mode eq 'QUEST_ADD') { &QUEST_ADD; }
elsif($mode eq 'QUEST_ADD_COM') { &QUEST_ADD_COM; }
elsif($mode eq 'BBS') { &BBS; }
elsif($mode eq 'GG') { &GG; }
elsif($mode eq 'GG1') { &GG1; }
elsif($mode eq 'CHANGE1') { &CHANGE1; }
elsif($mode eq 'DEL') { &DEL; }
elsif($mode eq 'DEL2') { &DEL2; }
elsif($mode eq 'DEL_LIST') { &DEL_LIST; }
elsif($mode eq 'ALL_DEL') { &ALL_DEL; }
elsif($mode eq 'INIT_DATA') { &INIT_DATA; }
elsif($mode eq 'EVENT_ON') { &EVENT_ON; }
else{&TOP;}

sub TOP {

if(($in{'id'} eq "$adminid" && $in{'pass'} eq "$adminpass")){
	&HEADER;
	print <<"EOM";
<h2>관리툴</h2>
<CENTER>
<table width=80% cellspacing=1 border=0 bgcolor=$TABLE_C><TBODY bgcolor=$TD_C4>
<TR><TH colspan=2>관리메뉴</TH></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=MENTE>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='캐릭터 편집'>
</Th></form><TD>
플레이어들의 데이터를 편집합니다. 평소엔 이쪽에서 편집해주세요.
참가자의 수가 증가하면 사용을 할 수 없게 되는 가능성도 있으니 유의바랍니다.
</TD></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=INIT_DATA>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='초기화'>
</Th></form><TD>
모든 데이터를 초기화합니다.
</TD></TD></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=QUEST_ENTRY>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='퀘스트작성'>
</Th></form><TD>
퀘스트를 작성합니다.
</TD></TD></TR>

</TBODY></TABLE>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=EVENT_ON>
<input type=hidden name=mode1 value=1>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='이벤트접수시작'></form>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=EVENT_ON>
<input type=hidden name=mode1 value=2>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='이벤트대회시작'></form>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=EVENT_ON>
<input type=hidden name=mode1 value=3>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='이벤트종료'></form>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=BBS>
공지사항:<input type=text name=message size=40>
관련URL링크:<input type=text name=message1 size=40>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='글쓰기'>
<br></form>

<form method="post" action="dkajlfjeioaefhoiwqhfeouihwefwefksdjklfjwe.cgi">
</select><input type=submit value='편집을 끝낸다'>
<br></form>
</CENTER>

EOM
}elsif(("$adminid3" eq $in{'id'} && $in{'pass'} eq "$adminpass3")){
	&HEADER;
	print <<"EOM";
<h2>관리툴</h2>
<CENTER>
<table width=80% cellspacing=1 border=0 bgcolor=$TABLE_C><TBODY bgcolor=$TD_C4>
<TR><TH colspan=2>부운영자 관리메뉴</TH></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=MENTE1>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='캐릭터 편집'>
</Th></form><TD>
플레이어들의 데이터를 편집합니다. 평소엔 이쪽에서 편집해주세요.
참가자의 수가 증가하면 사용을 할 수 없게 되는 가능성도 있으니 유의바랍니다.
</TD>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=QUEST_ENTRY>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='퀘스트작성'>
</Th></form><TD>
퀘스트를 작성합니다.
</TD></TD></TR>
</TBODY></TABLE>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=BBS>
공지사항:<input type=text name=message size=40>
관련URL링크:<input type=text name=message1 size=40>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='글쓰기'>
<br></form>

<form method="post" action="dkajlfjeioaefhoiwqhfeouihwefwefksdjklfjwe.cgi">
</select><input type=submit value='편집을 끝낸다'>
<br></form>
</CENTER>

EOM
}elsif(("$adminid2" eq $in{'id'} && $in{'pass'} eq "$adminpass2")){
	&HEADER;
	print <<"EOM";
<h2>관리툴</h2>
<CENTER>
<table width=80% cellspacing=1 border=0 bgcolor=$TABLE_C><TBODY bgcolor=$TD_C4>
<TR><TH colspan=2>퀘스트메이커 관리메뉴</TH></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=QUEST_ENTRY>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='퀘스트작성'>
</Th></form><TD>
퀘스트를 작성합니다.
</TD></TD></TR>
</TBODY></TABLE>

<form method="post" action="dkajlfjeioaefhoiwqhfeouihwefwefksdjklfjwe.cgi">
</select><input type=submit value='편집을 끝낸다'>
<br></form>
</CENTER>

EOM
}else{&ERR2("ID, 패스워드 에러 $num ");}
	open(IN,"$ADMIN_BBS");
	@A_BBS = <IN>;
	close(IN);

print "<center><table width=80% border=0 >@A_BBS</table></center>";

	&FOOTER;
	exit;
}



sub EVENT_ON{

	
	open(IN,"./log_file/event_on.cgi");
	@EVENT = <IN>;
	close(IN);

	($eventon,$emoney,$etime) = split(/<>/,$EVENT[0]);

	if($in{'mode1'} == 1){
	$eventon = 1;
	$emoney = 0;
	$etime = time();
	}elsif($in{'mode1'} ==2){
	$eventon = 2;
	}else{
	$eventon = 0;
	$emoney = 0;
	}



	@EVENT_DATA=();
	unshift(@EVENT_DATA,"$eventon<>$emoney<>$etime<>");
	open(OUT,">./log_file/event_on.cgi") or &ERR('MAIN 새로운 데이터를 기입할 수 없습니다.');
	print OUT @EVENT_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>무쌍대회이벤트가 변경되었습니다.</h2><p>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='돌아온다'>
</form></CENTER>
EOM

	&FOOTER;

	exit;

}



sub MENTE {

$dir="./charalog/main";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "검색 : $dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file가 발견되지 않았습니다.<br>\n";
			return 1;
		}
		@page = <page>;
		close(page);
		$list[$i]="$file";
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$page[0]);

		if("$in{'serch'}" ne ""){
			if("$ename" =~ "$in{'serch'}"){
				$human_data[$i]="$ehost<>$ename<>$eid<>";
			}else{
				next;
			}
		}else{
			if($in{'no'} eq "2"){
				$human_data[$i]="$ename<>$ehost<>$eid<>$epass<>$email<>$eos<>";
			}elsif($in{'no'} eq "3"){
				$human_data[$i]="$eid<>$ehost<>$ename<>$epass<>$email<>$eos<>";
			}elsif($in{'no'} eq "4"){
				$human_data[$i]="$epass<>$ehost<>$ename<>$eid<>$email<>$eos<>";
			}elsif($in{'no'} eq "5"){
				$human_data[$i]="$email<>$epass<>$ehost<>$ename<>$eid<>$eos<>";
			}elsif($in{'no'} eq "6"){
				$human_data[$i]="$eos<>$ename<>$ehost<>$eid<>$epass<>$email<>";
			}else{
				$human_data[$i]="$ehost<>$ename<>$eid<>$epass<>$email<>$eos<>";
			}
		}
		push(@newlist,"@page<br>");
		$i++;
	}
}
	closedir(dirlist);

	@human_data = sort @human_data;

$tt = time - (60 * 60 * 24 * 34);
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($tt);
$year += 1900;
$mon++;
$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);


	&HEADER;
	print <<"EOM";
<h2>캐릭터 관리툴</h2>
<br>
ID는 파일명과 같게 되었으니 변경하지 말아주세요.<br>
호스트명은 수시로 갱신하고 있습니다.<br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CHANGE>편집하는 파일 : 
<select name=fileno>
EOM
$i=0;$w_host="";
foreach(@human_data){
	if($in{'no'} eq "2"){
		($ename,$ehost,$eid,$epass,$email,$eos) = split(/<>/);
	}elsif($in{'no'} eq "3"){
		($eid,$ehost,$ename,$epass,$email,$eos) = split(/<>/);
	}elsif($in{'no'} eq "4"){
		($epass,$ehost,$ename,$eid,$email,$eos) = split(/<>/);
	}elsif($in{'no'} eq "5"){
		($email,$epass,$ehost,$ename,$eid,$eos) = split(/<>/);
	}elsif($in{'no'} eq "6"){
		($eos,$ename,$ehost,$eid,$epass,$email) = split(/<>/);
	}else{
		($ehost,$ename,$eid,$epass,$email,$eos) = split(/<>/);
	}
	print "<option value=$eid\.cgi>［인증:$eos］［ID:$eid］［이름:$ename］［호스트:$ehost］［비번:$epass］［이멜:$email］\n";
	if($in{'no'} eq "" || $in{'no'} eq "1"){
		if($w_host eq "$ehost"){
			$mess .= "$ename | $w_name<BR>\n";
		}
	}
	$w_host = "$ehost";
	$w_name = "$ename";
	$i++;
}
print <<"EOM";
</select><input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='편집'>
<br></form>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=MENTE>
<br><input type=radio name=no value="1">호스트명 순서(<font color=red>2중 등록 체크</font>)<br>
<input type=radio name=no value="2">이름순<br>
<input type=radio name=no value="3">ID순서<br>
<input type=radio name=no value="4">비번<br>
<input type=radio name=no value="5">이메일<br>
<input type=radio name=no value="6">인증 (Yes:1 | No:0)<br>
이름검색<input type=text name=serch size=20><br>
<input type=submit value='순서변경'>
<br></form>

<h2>파일 제거</h2>
2중등록자를 강제 삭제합니다.<BR>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=DEL_LIST>
<input type=submit value='삭제자 리스트'>
<br></form>


2중등록 의심자(이거 뜨는 사람들 가차없이 접속차단입니다. by 칠랑)<p>
<font color=red>$mess</font>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='TOP'>
<br></form>

EOM
	open(IN,"$ADMIN_LIST");
	@A_LOG = <IN>;
	close(IN);
print "@A_LOG";
	&FOOTER;
	exit;
}

sub MENTE1 {


$dir="./charalog/main";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "검색 : $dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file가 발견되지 않았습니다.<br>\n";
			return 1;
		}
		@page = <page>;
		close(page);
		$list[$i]="$file";
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$page[0]);

		if("$in{'serch'}" ne ""){
			if("$ename" =~ "$in{'serch'}"){
				$human_data[$i]="$ehost<>$ename<>$eid<>";
			}else{
				next;
			}
		}else{
			if($in{'no'} eq "2"){
				$human_data[$i]="$ename<>$ehost<>$eid<>$email<>$eos<>";
			}elsif($in{'no'} eq "3"){
				$human_data[$i]="$eid<>$ehost<>$ename<>$email<>$eos<>";
			}elsif($in{'no'} eq "5"){
				$human_data[$i]="$email<>$ehost<>$ename<>$eid<>";
			}elsif($in{'no'} eq "6"){
				$human_data[$i]="$eos<>$ename<>$ehost<>$eid<>$email<>";
			}else{
				$human_data[$i]="$ehost<>$ename<>$eid<>$email<>$eos<>";
			}
		}
		push(@newlist,"@page<br>");
		$i++;
	}
}
	closedir(dirlist);

	@human_data = sort @human_data;

$tt = time - (60 * 60 * 24 * 34);
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($tt);
$year += 1900;
$mon++;
$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);


	&HEADER;
	print <<"EOM";
<h2>캐릭터 관리툴</h2>
<br>
ID는 파일명과 같게 되었으니 변경하지 말아주세요.<br>
호스트명은 수시로 갱신하고 있습니다.<br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CHANGE1>편집하는 파일 : 
<select name=fileno>
EOM
$i=0;$w_host="";
foreach(@human_data){
	if($in{'no'} eq "2"){
		($ename,$ehost,$eid,$email,$eos) = split(/<>/);
	}elsif($in{'no'} eq "3"){
		($eid,$ehost,$ename,$email,$eos) = split(/<>/);
	}elsif($in{'no'} eq "5"){
		($email,$ehost,$ename,$eid,$eos) = split(/<>/);
	}elsif($in{'no'} eq "6"){
		($eos,$ename,$ehost,$eid,$email) = split(/<>/);
	}else{
		($ehost,$ename,$eid,$email,$eos) = split(/<>/);
	}
	print "<option value=$eid\.cgi>［인증:$eos］［ID:$eid］［이름:$ename］［호스트:$ehost］［이멜:$email］\n";
	if($in{'no'} eq "" || $in{'no'} eq "1"){
		if($w_host eq "$ehost"){
			$mess .= "$ename | $w_name<BR>\n";
		}
	}
	$w_host = "$ehost";
	$w_name = "$ename";
	$i++;
}
print <<"EOM";
</select><input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='편집'></form>
<br>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=MENTE1>
<br><input type=radio name=no value="1">호스트명 순서(<font color=red>2중 등록 체크</font>)<br>
<input type=radio name=no value="2">이름순<br>
<input type=radio name=no value="3">ID순서<br>
<input type=radio name=no value="5">이메일<br>
<input type=radio name=no value="6">인증(Yes:1 | No:0)<br>
이름검색<input type=text name=serch size=20><br>
<input type=submit value='순서변경'>
<br></form>

<h2>파일 제거</h2>
2중등록자를 강제 삭제합니다.<BR>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=DEL_LIST>
<input type=submit value='삭제자 리스트'>
<br></form>


2중등록 의심자(이거 뜨는 캐릭터들 모조리 차단바랍니다. by 칠랑)<p>
<font color=red>$mess</font>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='TOP'>
<br></form>

EOM
	open(IN,"$ADMIN_LIST");
	@A_LOG = <IN>;
	close(IN);
print "@A_LOG";
	&FOOTER;
	exit;
}


sub BBS {

	&TIME_DATA;

	if($in{'id'} eq "$adminid"){
	$goodname = "[Gm]갈량";
	$goodname1 = "b20";
	}elsif($in{'id'} eq "$adminid1"){
	$goodname = "[Gm]조운";
	$goodname1 = "gm1";
	}elsif($in{'id'} eq "$adminid2"){
	$goodname = "[Gm]춘추";
	$goodname1 = "gm2";
	}elsif($in{'id'} eq "$adminid3"){
	$goodname = "[Gm]마초";
	$goodname1 = "gm3";
	}

	open(IN,"$ADMIN_BBS");
	@AD_DATA = <IN>;
	close(IN);

	if($in{'message'} eq "") { &ERR2("메세지가 기입되어 있지 않습니다."); }
	if(length($in{'message'}) > 50) { &ERR2("좀 더 간략하게 글을 써주세요"); }

	$bbs_num = @AD_DATA;
	if($bbs_num > 40) { pop(@AD_DATA); }

	&MAP_LOG3("[$goodname] <a href=$in{'message1'} target=_blank>$in{'message'}</a>");

	unshift(@AD_DATA,"<font color=red>$in{'message'}</font> $goodname님 ($mday일$hour시$min분)<BR><hr size=0>\n");

	open(OUT,">$ADMIN_BBS");
	print OUT @AD_DATA;
	close(OUT);

	&HEADER;
	print <<"EOM";
<h2>기입했습니다.</h2>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='돌아온다'>
<br></form>
EOM
	&FOOTER;
	exit;
}

sub CHANGE {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("ID, 패스워드 에러 $num ");}
	$dir="./charalog/main";
	if(!open(page,"$dir/$in{'fileno'}")){
		$datames .= "$dir/$file가 발견되지 않았습니다.<br>\n";
		return 1;
	}
	@page = <page>;
	close(page);
	
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$page[0]);
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($edate);
	$year += 1900;
	$mon++;
	$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
	$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);
	
	&HEADER;
	print <<"EOM";
<form method="post" action="admin.cgi">
<h3><img src="$IMG/$echara.gif" width="$img_wid" height="$img_height" border=0> <font size=5 color=orange>$ename</font>의 정보</h3>
<table>
<tr>
<th>ID</th><td><input type=text name=eid value='$eid'></td>
<th>PASS</th><td><input type=text name=epass value='$epass'></td>
<th>NAME</th><td><input type=text name=ename value='$ename'></td>
<th>그림 ID</th><td><input type=text name=echara value='$echara'></td>
<tr>
<th>무력</th><td><input type=text name=estr value='$estr'></td>
<th>지력</th><td><input type=text name=eint value='$eint'></td>
<th>통솔력</th><td><input type=text name=elea value='$elea'></td>
<th>매력</th><td><input type=text name=echa value='$echa'></td>
</TR>
<tr>
<th>병사수</th><td><input type=text name=esol value='$esol'></td>
<th>훈련</th><td><input type=text name=egat value='$egat'></td>
<th>국</th><td><input type=text name=econ value='$econ'></td>
<th>금</th><td><input type=text name=egold value='$egold'></td>
</TR>
<tr>
<th>군량미</th><td><input type=text name=erice value='$erice'></td>
<th>공헌</th><td><input type=text name=ecex value='$ecex'></td>
<th>계급치</th><td><input type=text name=eclass value='$eclass'></td>
<th>무기</th><td><input type=text name=earm value='$earm'></td>
</TR>
<tr>
<th>서적</th><td><input type=text name=ebook value='$ebook'></td>
<th>충성</th><td><input type=text name=ebank value='$ebank'></td>
<th>서브1</th><td><input type=text name=esub1 value='$esub1'></td>
<th>서브2</th><td><input type=text name=esub2 value='$esub2'></td>
</TR>
<tr>
<th>현재 위치</th><td><input type=text name=epos value='$epos'></td>
<th>메시지</th><td><input type=text name=emes value='$emes'></td>
<th>호스트</th><td><input type=text name=ehost value='$ehost'></td>
<th>갱신일시</th><td><input type=text name=edate value='$edate'></td>
</TR>
<tr>
<th>MAIL</th><td><input type=text name=email value='$email'></td>
<th>행동 체크</th><td><input type=text name=eos value='$eos'></td>
<th>특기</th><td><input type=text name=eskill value='$eskill'></td>
<th>특기포인트</th><td><input type=text name=epoint value='$epoint'></td>
</TR>
<tr>
<th>고향</th><td><input type=text name=ect value='$ect'></td>
<th>레벨</th><td><input type=text name=elevel value='$elevel'></td>
<th>경험치</th><td><input type=text name=eexp value='$eexp'></td>
<th>퀘스트전</th><td><input type=text name=ecodea value='$ecodea'></td>
</TR>
<tr>
<th>퀘스트후</th><td><input type=text name=ecodeb value='$ecodeb'></td>
<th>퀘스트포인트</th><td><input type=text name=eqpoint value='$eqpoint'></td>
<th></th><td></td>
<th></th><td></td>
</TR>



</table>
<br>
<input type=hidden name=mode value=CHANGE2>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='편집'>
<br></form><form method="post" action="admin.cgi">
<input type=hidden name=mode value=GG>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='인증확인'>
<br></form><form method="post" action="admin.cgi">
<input type=hidden name=mode value=GG1>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='접속차단'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='편집을 그만둔다'>
</form>
<br>
<br>
<br>
<br>
MAP 로그 있음<br>
<form method="post" action="admin.cgi">
<input type=hidden name=filename value=$in{'fileno'}>
<input type=hidden name=mode value=DEL>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='이 파일을 삭제'>
</form>
<br>
<br>
<br>
MAP 로그 없음<br>
<form method="post" action="admin.cgi">
<input type=hidden name=filename value=$in{'fileno'}>
<input type=hidden name=mode value=DEL2>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='이 파일을 삭제'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}



sub QUEST_ENTRY {

	open(IN,"$QUEST_DATA");
	@QUEST_DATA = <IN>;
	close(IN);

	foreach(@QUEST_DATA){
		($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
		$list .= "<option value=$qnum>『퀘스트제목:$quest』『의뢰자:$qname』『수행레벨:$qlevel』『코드:$qcode』『필수코드:$qflag』";
		}
	&HEADER;

	print <<"EOM";
	<form method="post" action="admin.cgi">
<select name=questlist>
$list
</select>
<br>
$in{'questlist'}
<input type=hidden name=mode value=QUEST_EDIT>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='퀘스트 편집'>
<br></form><form method="post" action="admin.cgi">
<input type=hidden name=mode value=QUEST_ADD>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='퀘스트 생성'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='퀘스트작성중지'>
</form>
EOM

	&FOOTER;
	exit;
}


sub QUEST_EDIT {

	open(IN,"$QUEST_DATA");
	@QUEST_DATA = <IN>;
	close(IN);
	


	foreach(@QUEST_DATA){
		($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
		if($qnum == $in{'questlist'}){
			$qnum1 = "$qnum";
			$qcode1 = "$qcode";
			$qface1 = "$qface";
			$qname1 = "$qname";
			$qlevel1 = "$qlevel";
			$quest1 = "$quest";
			$qlimit1 = "$qlimit";
			$qtalka1 = "$qtalka";
			$qtalkb1 = "$qtalkb";
			$qtalkc1 = "$qtalkc";
			$qgold1 = "$qgold";
			$qrice1 = "$qrice";
			$qstr1 = "$qstr";
			$qint1 = "$qint";
			$qlea1 = "$qlea";
			$qcha1 = "$qcha";
			$qcex1 = "$qcex";
			$qexp1 = "$qexp";
			$qseal1 = "$qseal";
			$qflag1 = "$qflag";
			$qcategory1 = "$qcategory";
			$qrate1 = "$qrate";
			$qtalkd1 = "$qtalkd";
			$qup1 = "$qup";
			}

		$list .= "<option value=$qnum>『퀘스트제목:$quest』『의뢰자:$qname』『수행레벨:$qlevel』『코드:$qcode』";

		}
	&HEADER;

		$not1 = $qtalka1;
		$not1 =~ s/<br>/\n/ig;
		$not2 = $qtalkb1;
		$not2 =~ s/<br>/\n/ig;
		$not3 = $qtalkc1;
		$not3 =~ s/<br>/\n/ig;

	print <<"EOM";
<form method="post" action="admin.cgi">
<h3><font size=5 color=orange>퀘스트 $quest1</font>의 정보</h3>
<table border="1" cellspacing="0" width="900" bordercolordark="white" bordercolorlight="black">
    <tr>
        <td width="200" height="60" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">퀘스트번호</span></b></p>
        </td>
        <td width="300" height="60" bgcolor="#999999"><input type=text name=qnum1 value='$qnum1'></td>
        <td width="393" height="60" bgcolor="#999999">
            <p><span style="font-size:9pt;">퀘스트의 고유번호입니다.</span></p>
            <p><span style="font-size:9pt;">다른 퀘스트 번호와 절대 겹치게 하지 
            않습니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="91" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">퀘스트코드</span></b></p>
        </td>
        <td width="300" height="91" bgcolor="#999999"><input type=text name=qcode1 value='$qcode1'></td>
        <td width="393" height="91" bgcolor="#999999">
            <p><span style="font-size:9pt;">퀘스트의 코드번호입니다.</span></p>
            <p><span style="font-size:9pt;">퀘스트의 코드번호는 A0~A9 다음에 
            B0~B9, C0~C9식으로 입력합니다.</span></p>
            <p><span style="font-size:9pt;">절대 9이상을 넘어가면 다음 알파벳으로 
            교체해줘야 합니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">NPC얼굴이미지</span></b></p>
        </td>
        <td width="300" bgcolor="#999999"><input type=text name=qface1 value='$qface1'></td>
        <td width="393" bgcolor="#999999">
            <p><span style="font-size:9pt;">NPC의 얼굴 이미지입니다. 현재 등록된 
            인물은 다음과 같습니다.</span></p>
            <p><span style="font-size:9pt;">npc1 : 살수 흑칠랑</span></p>
            <p><span style="font-size:9pt;">npc2 : 신참 문관</span></p>
            <p><span style="font-size:9pt;">npc3 : 친절한 왕서방</span></p>
            <p><span style="font-size:9pt;">npc4 : 마담 설비향</span></p>
            <p><span style="font-size:9pt;">npc5 : 무관 왕진명</span></p>
            <p><span style="font-size:9pt;">npc6 : 창비호</span></p>
            <p><span style="font-size:9pt;">npc7 : 장인 조종천</span></p>
            <p><span style="font-size:9pt;">npc8 : 고참 문관</span></p>
            <p><span style="font-size:9pt;">npc9 : 애인 곽미령</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">NPC이름명</span></b></td>
        <td width="300" bgcolor="#999999"><input type=text name=qname1 value='$qname1'></td>
        <td width="393" bgcolor="#999999">
            <p><span style="font-size:9pt;">NPC의 이름은 위에 얼굴 이미지와 
            맞춰서 해주시면 됩니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">제한레벨</span></b></p>
        </td>
        <td width="300" bgcolor="#999999"><input type=text name=qlevel1 value='$qlevel1'></td>
        <td width="393" bgcolor="#999999">
            <p><span style="font-size:9pt;">이 퀘스트를 깨기 위해 필요한 레벨입니다.</span></p>
            <p><span style="font-size:9pt;">이 레벨에 도달하지 않으면 퀘스트가 
            보이지 않습니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="34" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">퀘스트제목</span></b></p>
        </td>
        <td width="300" height="34" bgcolor="#999900"><input type=text name=quest1 value='$quest1' size="40"></td>
        <td width="393" height="34" bgcolor="#999900">
            <p><span style="font-size:9pt;">퀘스트의 제목을 표시합니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">퀘스트대사前</span></b></td>
        <td width="300" height="56" bgcolor="#999900"><textarea name=qtalka1 rows=15 cols=54>$not1</textarea></td>
        <td width="393" height="56" bgcolor="#999900">
            <p><span style="font-size:9pt;">퀘스트를 수주받기 전의 대사가 나타냅니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">퀘스트대사後</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#999900"><textarea name=qtalkb1 rows="15" cols="54">$not2</textarea></td>
        <td width="393" height="56" bgcolor="#999900">
            <p><span style="font-size:9pt;">퀘스트를 수주를 받았으나 완료되지 
            않았을 때 대사를 나타냅니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">퀘스트완료대사</span></b></td>
        <td width="300" height="56" bgcolor="#999900"><textarea name=qtalkc1 rows="15" cols="54">$not3</textarea></td>
        <td width="393" height="56" bgcolor="#999900">
            <p><span style="font-size:9pt;">퀘스트가 완료되었을 때 대사를 나타냅니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="92" bgcolor="#999900">
            <p align="center"><span style="font-size:9pt;"><b>개인로그출력</b></span></p>
        </td>
        <td width="300" height="92" bgcolor="#999900"><input type=text name="qtalkd1" value="$qtalkd1" size="40"></td>
        <td width="393" height="92" bgcolor="#999900">
            <p><span style="font-size:9pt;">퀘스트를 수행 중에 개인로그에 출력되는 
            문장을 나타냅니다.</span></p>
            <p><span style="font-size:9pt;">상황에 맞춰서 대사를 넣어주시면 
            됩니다.</span></p>
            <p><span style="font-size:9pt;">출력을 원치 않으면 아무 것도 적지 
            않으면 됩니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">금액보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qgold1 value='$qgold1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 금액을 설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">군량보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qrice1 value='$qrice1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 군량을 설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">무력경험보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qstr1 value='$qstr1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 무력경험보상을 
            설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">지력경험보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qint1 value='$qint1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 지력경험보상을 
            설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">통솔경험보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qlea1 value='$qlea1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 통솔경험보상을 
            설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">매력경험보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qcha1 value='$qcha1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 매력경험보상을 
            설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">공헌치보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qcex1 value='$qcex1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 공헌치 보상을 
            설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">경험치보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qexp1 value='$qexp1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 경험치 보상을 
            설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#FF6600">
            <p align="center"><b><span style="font-size:9pt;">개인정보창제목</span></b></p>
        </td>
        <td width="300" bgcolor="#FF6600"><input type=text name=qseal1 value='$qseal1'></td>
        <td width="393" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">개인 스테이터스 화면 창에 해당 퀘스트의 
            정보를 간략하게 요약해서 표시합니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#FF6600">
            <p align="center"><b><span style="font-size:9pt;">필수퀘스트코드</span></b></p>
        </td>
        <td width="300" bgcolor="#FF6600"><input type=text name=qflag1 value='$qflag1'></td>
        <td width="393" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">이 퀘스트를 깨기 위해서 필요한 퀘스트 
            코드를 기입합니다.</span></p>
            <p><span style="font-size:9pt;">기입한 필수퀘스트를 클리어하지 않으면 
            해당 퀘스트가 보이지 않습니다.</span></p>
            <p><span style="font-size:9pt;">단, 절대 한 개의 퀘스트 코드만 기입해야 
            합니다.</span></p>
            <p><select name=questlist>$list</select></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="92" bgcolor="#FF6600">
            <p align="center"><b><span style="font-size:9pt;">퀘스트종류</span></b></p>
        </td>
        <td width="300" height="92" bgcolor="#FF6600"><input type=text name=qcategory1 value='$qcategory1'></td>
        <td width="393" height="92" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">퀘스트의 종류를 기입합니다.</span></p>
            <p><span style="font-size:9pt;">수주할 수 있는 퀘스트의 종류는 한 
            개만 설정해야 하고&nbsp;다음과 같습니다.</span></p>
            <p><span style="font-size:9pt;">농업 : 농업개발</span></p>
            <p><span style="font-size:9pt;">상업 : 상업개발</span></p>
            <p><span style="font-size:9pt;">기술 : 기술개발</span></p>
            <p><span style="font-size:9pt;">민심 : 쌀을 베품</span></p>
            <p><span style="font-size:9pt;">전쟁 : 출병</span></p>
            <p><span style="font-size:9pt;">요격 : 요격</span></p>
            <p><span style="font-size:9pt;">방어 : 방어시설구축</span></p>
            <p><span style="font-size:9pt;">서신 : 다른 장수에게 서신</span></p>
            <p><span style="font-size:9pt;">밀서 : 다른 장수에게 밀서</span></p>
            <p><span style="font-size:9pt;">하야 : 하야</span></p>
            <p><span style="font-size:9pt;">일기토 : 겨루기에서 일기토입력시</span></p>
            <p><span style="font-size:9pt;">설전 : 겨루기에서 설전입력시</span></p>
	<p><span style="font-size:9pt;">수색 : 수색</span></p>
	<p><span style="font-size:9pt;">훈련 : 훈련,맹훈련</span></p>
	<p><span style="font-size:9pt;">송금 : 송금</span></p>
	<p><span style="font-size:9pt;">휴식 : 휴식</span></p>
	<p><span style="font-size:9pt;">숙박 : 숙박</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#FF6600">
            <p align="center"><span style="font-size:9pt;"><b>퀘스트확률</b></span></p>
        </td>
        <td width="300" height="56" bgcolor="#FF6600"><input type=text name="qrate1" value="$qrate1"></td>
        <td width="393" height="56" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">해당 퀘스트를 진행시 성공하는 확률을 
            기입합니다.</span></p>
            <p><span style="font-size:9pt;">100%로 설정하면 무조건 성공합니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#FF6600">
            <p align="center"><span style="font-size:9pt;"><b>퀘스트상한치</b></span></p>
        </td>
        <td width="300" height="56" bgcolor="#FF6600"><input type=text name="qlimit1" value="$qlimit1"></td>
        <td width="393" height="56" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">퀘스트를 클리어하기 위해 필요한 상한치를 설정합니다.</span></p>
            <p><span style="font-size:9pt;">퀘스트증가폭에 맞춰서 상한치를 설정해야 합니다.</span></p>
        </td>
    </tr>    <tr>
        <td width="200" height="56" bgcolor="#FF6600">
            <p align="center"><span style="font-size:9pt;"><b>퀘스트증가폭</b></span></p>
        </td>
        <td width="300" height="56" bgcolor="#FF6600"><input type=text name="qup1" value="$qup1"></td>
        <td width="393" height="56" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">퀘스트를 실행시에 늘어나는 폭을 설정합니다.</span></p>
            <p><span style="font-size:9pt;">숫자로 설정하면 해당 숫자만큼 늘어나지만 다음과 같이 글자를 넣으면 해당 수치만큼 오릅니다.</span></p>
		<p><span style="font-size:9pt;">농업 : 자신의 농업치만큼 상승</span></p>
		<p><span style="font-size:9pt;">상업 : 자신의 상업치만큼 상승</span></p>
		<p><span style="font-size:9pt;">기술 : 자신의 기술치만큼 상승</span></p>
		<p><span style="font-size:9pt;">민심 : 자신의 민심치만큼 상승</span></p>
		<p><span style="font-size:9pt;">징병 : 자신의 징병수만큼 상승</span></p>
		<p><span style="font-size:9pt;">수비 : 자신의 수비대수만큼 상승</span></p>
	<p><span style="font-size:9pt;">방어 : 자신의 방어시설만큼 상승</span></p>
	<p><span style="font-size:9pt;">훈련 : 자신의 훈련만큼 상승</span></p>
	<p><span style="font-size:9pt;">송금 : 자신의 송금액수만큼 상승</span></p>
        </td>
    </tr>
</table>
<br>
<input type=hidden name=mode value=QUEST_EDIT_COM>
<input type=hidden name=questlist value=$in{'questlist'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='퀘스트 수정'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='퀘스트작성중지'>
</form>
EOM

	&FOOTER;
	exit;
}


sub QUEST_ADD {
	open(IN,"$QUEST_DATA");
	@QUEST_DATA = <IN>;
	close(IN);

	foreach(@QUEST_DATA){
		($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
		$list .= "<option value=$qnum>『퀘스트제목:$quest』『의뢰자:$qname』『수행레벨:$qlevel』『코드:$qcode』";
		}

	&HEADER;
	print <<"EOM";
<form method="post" action="admin.cgi">
<h3><font size=5 color=orange>퀘스트 $quest1</font>의 정보</h3>
<table border="1" cellspacing="0" width="1111" bordercolordark="white" bordercolorlight="black">
    <tr>
        <td width="200" height="60" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">퀘스트번호</span></b></p>
        </td>
        <td width="300" height="60" bgcolor="#999999"><input type=text name=qnum1 value='$qnum1'></td>
        <td width="393" height="60" bgcolor="#999999">
            <p><span style="font-size:9pt;">퀘스트의 고유번호입니다.</span></p>
            <p><span style="font-size:9pt;">다른 퀘스트 번호와 절대 겹치게 하지 
            않습니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="91" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">퀘스트코드</span></b></p>
        </td>
        <td width="300" height="91" bgcolor="#999999"><input type=text name=qcode1 value='$qcode1'></td>
        <td width="393" height="91" bgcolor="#999999">
            <p><span style="font-size:9pt;">퀘스트의 코드번호입니다.</span></p>
            <p><span style="font-size:9pt;">퀘스트의 코드번호는 A0~A9 다음에 
            B0~B9, C0~C9식으로 입력합니다.</span></p>
            <p><span style="font-size:9pt;">절대 9이상을 넘어가면 다음 알파벳으로 
            교체해줘야 합니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">NPC얼굴이미지</span></b></p>
        </td>
        <td width="300" bgcolor="#999999"><input type=text name=qface1 value='$qface1'></td>
        <td width="393" bgcolor="#999999">
            <p><span style="font-size:9pt;">NPC의 얼굴 이미지입니다. 현재 등록된 
            인물은 다음과 같습니다.</span></p>
            <p><span style="font-size:9pt;">npc1 : 살수 흑칠랑</span></p>
            <p><span style="font-size:9pt;">npc2 : 신참 문관</span></p>
            <p><span style="font-size:9pt;">npc3 : 친절한 왕서방</span></p>
            <p><span style="font-size:9pt;">npc4 : 마담 설비향</span></p>
            <p><span style="font-size:9pt;">npc5 : 무관 왕진명</span></p>
            <p><span style="font-size:9pt;">npc6 : 창비호</span></p>
            <p><span style="font-size:9pt;">npc7 : 장인 조종천</span></p>
            <p><span style="font-size:9pt;">npc8 : 고참 문관</span></p>
            <p><span style="font-size:9pt;">npc9 : 애인 곽미령</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">NPC이름명</span></b></td>
        <td width="300" bgcolor="#999999"><input type=text name=qname1 value='$qname1'></td>
        <td width="393" bgcolor="#999999">
            <p><span style="font-size:9pt;">NPC의 이름은 위에 얼굴 이미지와 
            맞춰서 해주시면 됩니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">제한레벨</span></b></p>
        </td>
        <td width="300" bgcolor="#999999"><input type=text name=qlevel1 value='$qlevel1'></td>
        <td width="393" bgcolor="#999999">
            <p><span style="font-size:9pt;">이 퀘스트를 깨기 위해 필요한 레벨입니다.</span></p>
            <p><span style="font-size:9pt;">이 레벨에 도달하지 않으면 퀘스트가 
            보이지 않습니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="34" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">퀘스트제목</span></b></p>
        </td>
        <td width="300" height="34" bgcolor="#999900"><input type=text name=quest1 value='$quest1' size="84"></td>
        <td width="393" height="34" bgcolor="#999900">
            <p><span style="font-size:9pt;">퀘스트의 제목을 표시합니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">퀘스트대사前</span></b></td>
        <td width="300" height="56" bgcolor="#999900"><textarea name=qtalka1 rows="15" cols="54">$not1</textarea></td>
        <td width="393" height="56" bgcolor="#999900">
            <p><span style="font-size:9pt;">퀘스트를 수주받기 전의 대사가 나타냅니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">퀘스트대사後</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#999900"><textarea name=qtalkb1 rows="15" cols="54">$not2</textarea></td>
        <td width="393" height="56" bgcolor="#999900">
            <p><span style="font-size:9pt;">퀘스트를 수주를 받았으나 완료되지 
            않았을 때 대사를 나타냅니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">퀘스트완료대사</span></b></td>
        <td width="300" height="56" bgcolor="#999900"><textarea name=qtalkc1 rows="15" cols="54">$not3</textarea></td>
        <td width="393" height="56" bgcolor="#999900">
            <p><span style="font-size:9pt;">퀘스트가 완료되었을 때 대사를 나타냅니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="92" bgcolor="#999900">
            <p align="center"><span style="font-size:9pt;"><b>개인로그출력</b></span></p>
        </td>
        <td width="300" height="92" bgcolor="#999900"><input type=text name="qtalkd1" value="$qtalkd1" size="40"></td>
        <td width="393" height="92" bgcolor="#999900">
            <p><span style="font-size:9pt;">퀘스트를 수행 중에 개인로그에 출력되는 
            문장을 나타냅니다.</span></p>
            <p><span style="font-size:9pt;">상황에 맞춰서 대사를 넣어주시면 
            됩니다.</span></p>
            <p><span style="font-size:9pt;">출력을 원치 않으면 아무 것도 적지 
            않으면 됩니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">금액보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qgold1 value='$qgold1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 금액을 설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">군량보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qrice1 value='$qrice1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 군량을 설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">무력경험보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qstr1 value='$qstr1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 무력경험보상을 
            설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">지력경험보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qint1 value='$qint1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 지력경험보상을 
            설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">통솔경험보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qlea1 value='$qlea1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 통솔경험보상을 
            설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">매력경험보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qcha1 value='$qcha1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 매력경험보상을 
            설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">공헌치보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qcex1 value='$qcex1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 공헌치 보상을 
            설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">경험치보상</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qexp1 value='$qexp1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">퀘스트완료시 보상받는 경험치 보상을 
            설정합니다.</span></p>
            <p><span style="font-size:9pt;">원치않으면 0으로 설정.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#FF6600">
            <p align="center"><b><span style="font-size:9pt;">개인정보창제목</span></b></p>
        </td>
        <td width="300" bgcolor="#FF6600"><input type=text name=qseal1 value='$qseal1'></td>
        <td width="393" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">개인 스테이터스 화면 창에 해당 퀘스트의 
            정보를 간략하게 요약해서 표시합니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#FF6600">
            <p align="center"><b><span style="font-size:9pt;">필수퀘스트코드</span></b></p>
        </td>
        <td width="300" bgcolor="#FF6600"><input type=text name=qflag1 value='$qflag1'></td>
        <td width="393" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">이 퀘스트를 깨기 위해서 필요한 퀘스트 
            코드를 기입합니다.</span></p>
            <p><span style="font-size:9pt;">기입한 필수퀘스트를 클리어하지 않으면 
            해당 퀘스트가 보이지 않습니다.</span></p>
            <p><span style="font-size:9pt;">단, 절대 한 개의 퀘스트 코드만 기입해야 
            합니다.</span></p>
            <p><select name=questlist>$list</select></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="92" bgcolor="#FF6600">
            <p align="center"><b><span style="font-size:9pt;">퀘스트종류</span></b></p>
        </td>
        <td width="300" height="92" bgcolor="#FF6600"><input type=text name=qcategory1 value='$qcategory1'></td>
        <td width="393" height="92" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">퀘스트의 종류를 기입합니다.</span></p>
            <p><span style="font-size:9pt;">수주할 수 있는 퀘스트의 종류는 한 
            개만 설정해야 하고&nbsp;다음과 같습니다.</span></p>
            <p><span style="font-size:9pt;">농업 : 농업개발</span></p>
            <p><span style="font-size:9pt;">상업 : 상업개발</span></p>
            <p><span style="font-size:9pt;">기술 : 기술개발</span></p>
            <p><span style="font-size:9pt;">민심 : 쌀을 베품</span></p>
            <p><span style="font-size:9pt;">전쟁 : 출병</span></p>
            <p><span style="font-size:9pt;">요격 : 요격</span></p>
            <p><span style="font-size:9pt;">방어 : 방어시설구축</span></p>
            <p><span style="font-size:9pt;">서신 : 다른 장수에게 서신</span></p>
            <p><span style="font-size:9pt;">밀서 : 다른 장수에게 밀서</span></p>
            <p><span style="font-size:9pt;">하야 : 하야</span></p>
            <p><span style="font-size:9pt;">일기토 : 겨루기에서 일기토입력시</span></p>
            <p><span style="font-size:9pt;">설전 : 겨루기에서 설전입력시</span></p>
	<p><span style="font-size:9pt;">수색 : 수색</span></p>
	<p><span style="font-size:9pt;">훈련 : 훈련,맹훈</span></p>
	<p><span style="font-size:9pt;">송금 : 송금</span></p>
	<p><span style="font-size:9pt;">휴식 : 휴식</span></p>
	<p><span style="font-size:9pt;">숙박 : 숙박</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#FF6600">
            <p align="center"><span style="font-size:9pt;"><b>퀘스트확률</b></span></p>
        </td>
        <td width="300" height="56" bgcolor="#FF6600"><input type=text name="qrate1" value="$qrate1"></td>
        <td width="393" height="56" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">해당 퀘스트를 진행시 성공하는 확률을 
            기입합니다.</span></p>
            <p><span style="font-size:9pt;">100%로 설정하면 무조건 성공합니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#FF6600">
            <p align="center"><span style="font-size:9pt;"><b>퀘스트상한치</b></span></p>
        </td>
        <td width="300" height="56" bgcolor="#FF6600"><input type=text name="qlimit1" value="$qlimit1"></td>
        <td width="393" height="56" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">퀘스트를 클리어하기 위해 필요한 상한치를 설정합니다.</span></p>
            <p><span style="font-size:9pt;">퀘스트증가폭에 맞춰서 상한치를 설정해야 합니다.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#FF6600">
            <p align="center"><span style="font-size:9pt;"><b>퀘스트증가폭</b></span></p>
        </td>
        <td width="300" height="56" bgcolor="#FF6600"><input type=text name="qup1" value="$qup1"></td>
        <td width="393" height="56" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">퀘스트를 실행시에 늘어나는 폭을 설정합니다.</span></p>
            <p><span style="font-size:9pt;">숫자로 설정하면 숫자만큼 늘어나지만 다음과 같이 글자를 넣으면 해당 수치만큼 오릅니다.</span></p>
		<p><span style="font-size:9pt;">농업 : 자신의 농업치만큼 상승</span></p>
		<p><span style="font-size:9pt;">상업 : 자신의 상업치만큼 상승</span></p>
		<p><span style="font-size:9pt;">기술 : 자신의 기술치만큼 상승</span></p>
		<p><span style="font-size:9pt;">민심 : 자신의 민심치만큼 상승</span></p>
		<p><span style="font-size:9pt;">징병 : 자신의 징병수만큼 상승</span></p>
	<p><span style="font-size:9pt;">수비 : 자신의 수비대수만큼 상승</span></p>
	<p><span style="font-size:9pt;">방어 : 자신의 방어시설구축만큼 상승</span></p>
	<p><span style="font-size:9pt;">훈련 : 자신의 훈련만큼 상승</span></p>
	<p><span style="font-size:9pt;">송금 : 자신의 송금액수만큼 상승</span></p>
        </td>
    </tr>
</table>
</table>
<br>
<input type=hidden name=mode value=QUEST_ADD_COM>
<input type=hidden name=questlist value=$in{'questlist'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='퀘스트 생성'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='퀘스트생성중지'>
</form>
EOM

	&FOOTER;
	exit;
}


sub QUEST_ADD_COM {
	open(IN,"$QUEST_DATA");
	@QUEST_DATA = <IN>;
	close(IN);
	my @NEW_QUEST=();

	foreach(@QUEST_DATA){
		($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
		if("$in{'qnum1'}" eq "$qnum"){
			&ERR2("<font color=red>퀘스트 번호가 이미 있습니다.</font>");
			}else{
			push(@NEW_QUEST,"$_");
			}
		}

	unshift(@NEW_QUEST,"$in{'qnum1'}<>$in{'qcode1'}<>$in{'qface1'}<>$in{'qname1'}<>$in{'qlevel1'}<>$in{'quest1'}<>$in{'qlimit1'}<>$in{'qtalka1'}<>$in{'qtalkb1'}<>$in{'qtalkc1'}<>$in{'qgold1'}<>$in{'qrice1'}<>$in{'qstr1'}<>$in{'q$int1'}<>$in{'qlea1'}<>$in{'qcha1'}<>$in{'qcex1'}<>$in{'qexp1'}<>$in{'qseal1'}<>$in{'qflag1'}<>$in{'qcategory1'}<>$in{'qrate1'}<>$in{'qtalkd1'}<>$in{'qup1'}<>\n");
	open(OUT,">$QUEST_DATA");
	print OUT @NEW_QUEST;
	close(OUT);
	&ADMIN_LOG("<font color=blue>퀘스트 $in{'quest1'}를 생성했습니다.</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>퀘스트 $in{'quest1'}를 생성했습니다.</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='돌아온다'>
</form>
EOM

	&FOOTER;
	exit;
}



sub QUEST_EDIT_COM {
	open(IN,"$QUEST_DATA");
	@QUEST_DATA = <IN>;
	close(IN);


	$qtalka3 = "$in{'qtalka1'}";
	$qtalkb3 = "$in{'qtalkb1'}";
	$qtalkc3 = "$in{'qtalkc1'}";	
	


	
	@NEW_QUEST_DATA=();
	$dnum = 0;
	foreach(@QUEST_DATA){
	($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
		if($in{'questlist'} eq "$qnum"){
		splice(@NEW_QUEST_DATA,$dnum,1,"$in{'qnum1'}<>$in{'qcode1'}<>$in{'qface1'}<>$in{'qname1'}<>$in{'qlevel1'}<>$in{'quest1'}<>$in{'qlimit1'}<>$qtalka3<>$qtalkb3<>$qtalkc3<>$in{'qgold1'}<>$in{'qrice1'}<>$in{'qstr1'}<>$in{'qint1'}<>$in{'qlea1'}<>$in{'qcha1'}<>$in{'qcex1'}<>$in{'qexp1'}<>$in{'qseal1'}<>$in{'qflag1'}<>$in{'qcategory1'}<>$in{'qrate1'}<>$in{'qtalkd1'}<>$in{'qup1'}<>\n");
		}else{
		push(@NEW_QUEST_DATA,"$_");
		}
		$dnum++;
	}
	open(OUT,">$QUEST_DATA");
	print OUT @NEW_QUEST_DATA;
	close(OUT);
	&ADMIN_LOG("<font color=blue>퀘스트 $in{'quest1'}를 갱신했습니다.</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>퀘스트 $in{'quest1'}를 갱신했습니다.</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='돌아온다'>
</form>
EOM

	&FOOTER;
	exit;
}



sub CHANGE1 {

	$dir="./charalog/main";
	if(!open(page,"$dir/$in{'fileno'}")){
		$datames .= "$dir/$file가 발견되지 않았습니다.<br>\n";
		return 1;
	}
	@page = <page>;
	close(page);
	
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$page[0]);
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($edate);
	$year += 1900;
	$mon++;
	$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
	$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);
	
	&HEADER;
	print <<"EOM";
<h3><img src="$IMG/$echara.gif" width="$img_wid" height="$img_height" border=0> <font size=5 color=orange>$ename</font>의 정보</h3>
<table>
<tr>
<th>ID</th><td>$eid</td>
<th>NAME</th><td>$ename</td>
<th>그림 ID</th><td>$echara</td>
<th></th><td></td>
<tr>
<th>무력</th><td>$estr</td>
<th>지력</th><td>$eint</td>
<th>통솔력</th><td>$elea</td>
<th>매력</th><td>$echa</td>
</TR>
<tr>
<th>호스트</th><td>$ehost</td>
<th>갱신일시</th><td>$edate</td>
<th>MAIL</th><td>$email</td>
<th>인증(Yes:1,No:0)</th><td>$eos</td>
</TR>
<tr>
<th>경험치</th><td>$eexp</td>
<th></th><td></td>
<th></th><td></td>
<th></th><td></td>
</TR>


</table>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=GG>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='인증확인'>
<br></form><form method="post" action="admin.cgi">
<input type=hidden name=mode value=GG1>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='접속차단'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='편집을 그만둔다'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

sub CHANGE2 {

	$dir="./charalog/main";
	
	$newdata = "$in{'eid'}<>$in{'epass'}<>$in{'ename'}<>$in{'echara'}<>$in{'estr'}<>$in{'eint'}<>$in{'elea'}<>$in{'echa'}<>$in{'esol'}<>$in{'egat'}<>$in{'econ'}<>$in{'egold'}<>$in{'erice'}<>$in{'ecex'}<>$in{'eclass'}<>$in{'earm'}<>$in{'ebook'}<>$in{'ebank'}<>$in{'esub1'}<>$in{'esub2'}<>$in{'epos'}<>$in{'emes'}<>$in{'ehost'}<>$in{'edate'}<>$in{'email'}<>$in{'eos'}<>$in{'eskill'}<>$in{'epoint'}<>$in{'ect'}<>$in{'elevel'}<>$in{'eexp'}<>$in{'ecodea'}<>$in{'ecodeb'}<>$in{'eqpoint'}<>\n";

	open(page,">$dir/$in{'fileno'}");
	print page $newdata;
	close(page);
&HOST_NAME;
	
&ADMIN_LOG("<font color=blue>$in{'ename'} $dir/$in{'fileno'}를 갱신했습니다. 「$host」</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>$in{'ename'} 의 파일 $dir/$in{'fileno'}를 갱신했습니다.</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='돌아온다'>
</form>
EOM

	&FOOTER;
	exit;
}

sub GG {
	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("파일 오픈 에러!");
			}
			@page = <page>;
			close(page);
			($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct,$klevel,$kexp,$kcodea,$kcodeb,$kqpoint) = split(/<>/,$page[0]);
			if("$in{'fileno'}" eq "$kid\.cgi"){
			$kos = 1;
			$goodi = $kname;
			}
			&CHARA_MAIN_INPUT;
				}
	}
	closedir(dirlist);
		if($in{'id'} eq "$adminid"){
	$goodname = "[Gm]칠랑";
	}elsif($in{'id'} eq "$adminid1"){
	$goodname = "[Gm]조운";
	}elsif($in{'id'} eq "$adminid2"){
	$goodname = "[Gm]춘추";
	}elsif($in{'id'} eq "$adminid3"){
	$goodname = "[Gm]마초";
	}

&ADMIN_LOG("<font color=blue>$goodname님이 $goodi님을 인증완료했습니다.</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>$goodname님이 $goodi님을 인증완료했습니다.</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='돌아온다'>
</form>
EOM

	&FOOTER;
	exit;
}

sub GG1 {
	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("파일 오픈 에러!");
			}
			@page = <page>;
			close(page);
			($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct,$klevel,$kexp,$kcodea,$kcodeb,$kqpoint) = split(/<>/,$page[0]);
			if("$in{'fileno'}" eq "$kid\.cgi"){
			$kos = 0;
			$goodi = $kname;
			}
			&CHARA_MAIN_INPUT;
				}
	}
	closedir(dirlist);
	
&ADMIN_LOG("<font color=blue>$goodi님을 접속차단했습니다. 「$host」</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>$goodi님을 접속차단했습니다.</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='돌아온다'>
</form>
EOM

	&FOOTER;
	exit;
}

sub DEL {

&HOST_NAME;
	open(IN,"./charalog/main/$in{'filename'}") or &ERR2('이 파일을 삭제할 수 없습니다.');
	@CN_DATA = <IN>;
	close(IN);
	($kid,$kpass,$kname) = split(/<>/,$CN_DATA[0]);
			&BONG_DEL;
			$dir2="./charalog/main";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/log";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/command";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/log2";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/history";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/per";
			unlink("$dir2/$in{'filename'}");

&ADMIN_LOG("<font color=red>$kname를 삭제했습니다. 「$host」 </font>");

	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	&TIME_DATA;
	open(IN,"$DEF_LIST");
	@DEF_LIST = <IN>;
	close(IN);

	@NEW_DEF_LIST_DEL=();
	foreach(@DEF_LIST){
		($tid,$tname,$ttown_id,$ttown_flg,$tcon) = split(/<>/);
		if("$tid" eq "$kid"){
		}else{
			push(@NEW_DEF_LIST_DEL,"$_");
		}
	}
	open(OUT,">$DEF_LIST");
	print OUT @NEW_DEF_LIST_DEL;
	close(OUT);

	unshift(@S_MOVE,"<img src=$IMG/j17.gif> $kname는 삭제되었습니다.($mday일$hour시$min분)\n");
	splice(@S_MOVE,20);

	open(OUT,">$MAP_LOG_LIST") or &ERR2('LOG 새로운 데이터를 기입할 수 없습니다.');
	print OUT @S_MOVE;
	close(OUT);

	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$kname를 삭제했습니다.</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='돌아온다'>
<br></form>
EOM

	&FOOTER;
	exit;
}

sub DEL2 {

&HOST_NAME;
	open(IN,"./charalog/main/$in{'filename'}") or &ERR2('파일을 삭제할 수 없습니다.');
	@CN_DATA = <IN>;
	close(IN);
	($kid,$kpass,$kname) = split(/<>/,$CN_DATA[0]);

			$dir2="./charalog/main";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/log";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/command";
			unlink("$dir2/$in{'filename'}");
&ADMIN_LOG("<font color=red>$kname를 삭제했습니다. 「$host」 </font>");

	open(IN,"$DEF_LIST");
	@DEF_LIST = <IN>;
	close(IN);

	@NEW_DEF_LIST_DEL=();
	foreach(@DEF_LIST){
		($tid,$tname,$ttown_id,$ttown_flg,$tcon) = split(/<>/);
		if("$tid" eq "$kid"){
		}else{
			push(@NEW_DEF_LIST_DEL,"$_");
		}
	}
	open(OUT,">$DEF_LIST");
	print OUT @NEW_DEF_LIST_DEL;
	close(OUT);

	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$kname를 삭제했습니다.</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='돌아온다'>
<br></form>
EOM

	&FOOTER;
	exit;
}

sub ADMIN_LOG {

	if($lockkey) { &F_LOCK; }
	open(IN,"$ADMIN_LIST");
	@A_LOG = <IN>;
	close(IN);
	&TIME_DATA;

	unshift(@A_LOG,"$_[0]($mday일$hour시$min분)<BR>\n");
	splice(@A_LOG,20);

	open(OUT,">$ADMIN_LIST") or &ERR2('LOG 새로운 데이터를 기입할 수 없습니다');
	print OUT @A_LOG;
	close(OUT);
	if (-e $lockfile) { unlink($lockfile); }
}


sub INIT_DATA {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("패스워드 에러 $num ");}

	require "reset.cgi";
	&RESET_MODE;
&HOST_NAME;

	&ADMIN_LOG("전데이터를 초기화했습니다.[$host]");
	
	&HEADER;
	print <<"EOM";
<h2><font color=red>전데이터를 초기화했습니다.</h2></font>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='돌아온다'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}
1;
