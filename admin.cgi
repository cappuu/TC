#!/usr/bin/perl


require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR2("�ε����Դϴ�. ��ø� ��ٷ� �ֽʽÿ�"); }
&DECODE;
$adminid = "�����ھ��̵�1";
$adminpass = "�������н�����1";

$adminid2 = "�����ھ��̵�2";
$adminpass2 = "�����ھ��̵�2";

$adminid3 = "�����ھ��̵�3";
$adminpass3 = "�����ھ��̵�3";

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
<h2>������</h2>
<CENTER>
<table width=80% cellspacing=1 border=0 bgcolor=$TABLE_C><TBODY bgcolor=$TD_C4>
<TR><TH colspan=2>�����޴�</TH></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=MENTE>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='ĳ���� ����'>
</Th></form><TD>
�÷��̾���� �����͸� �����մϴ�. ��ҿ� ���ʿ��� �������ּ���.
�������� ���� �����ϸ� ����� �� �� ���� �Ǵ� ���ɼ��� ������ ���ǹٶ��ϴ�.
</TD></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=INIT_DATA>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�ʱ�ȭ'>
</Th></form><TD>
��� �����͸� �ʱ�ȭ�մϴ�.
</TD></TD></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=QUEST_ENTRY>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����Ʈ�ۼ�'>
</Th></form><TD>
����Ʈ�� �ۼ��մϴ�.
</TD></TD></TR>

</TBODY></TABLE>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=EVENT_ON>
<input type=hidden name=mode1 value=1>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�̺�Ʈ��������'></form>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=EVENT_ON>
<input type=hidden name=mode1 value=2>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�̺�Ʈ��ȸ����'></form>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=EVENT_ON>
<input type=hidden name=mode1 value=3>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�̺�Ʈ����'></form>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=BBS>
��������:<input type=text name=message size=40>
����URL��ũ:<input type=text name=message1 size=40>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�۾���'>
<br></form>

<form method="post" action="dkajlfjeioaefhoiwqhfeouihwefwefksdjklfjwe.cgi">
</select><input type=submit value='������ ������'>
<br></form>
</CENTER>

EOM
}elsif(("$adminid3" eq $in{'id'} && $in{'pass'} eq "$adminpass3")){
	&HEADER;
	print <<"EOM";
<h2>������</h2>
<CENTER>
<table width=80% cellspacing=1 border=0 bgcolor=$TABLE_C><TBODY bgcolor=$TD_C4>
<TR><TH colspan=2>�ο�� �����޴�</TH></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=MENTE1>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='ĳ���� ����'>
</Th></form><TD>
�÷��̾���� �����͸� �����մϴ�. ��ҿ� ���ʿ��� �������ּ���.
�������� ���� �����ϸ� ����� �� �� ���� �Ǵ� ���ɼ��� ������ ���ǹٶ��ϴ�.
</TD>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=QUEST_ENTRY>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����Ʈ�ۼ�'>
</Th></form><TD>
����Ʈ�� �ۼ��մϴ�.
</TD></TD></TR>
</TBODY></TABLE>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=BBS>
��������:<input type=text name=message size=40>
����URL��ũ:<input type=text name=message1 size=40>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�۾���'>
<br></form>

<form method="post" action="dkajlfjeioaefhoiwqhfeouihwefwefksdjklfjwe.cgi">
</select><input type=submit value='������ ������'>
<br></form>
</CENTER>

EOM
}elsif(("$adminid2" eq $in{'id'} && $in{'pass'} eq "$adminpass2")){
	&HEADER;
	print <<"EOM";
<h2>������</h2>
<CENTER>
<table width=80% cellspacing=1 border=0 bgcolor=$TABLE_C><TBODY bgcolor=$TD_C4>
<TR><TH colspan=2>����Ʈ����Ŀ �����޴�</TH></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=QUEST_ENTRY>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����Ʈ�ۼ�'>
</Th></form><TD>
����Ʈ�� �ۼ��մϴ�.
</TD></TD></TR>
</TBODY></TABLE>

<form method="post" action="dkajlfjeioaefhoiwqhfeouihwefwefksdjklfjwe.cgi">
</select><input type=submit value='������ ������'>
<br></form>
</CENTER>

EOM
}else{&ERR2("ID, �н����� ���� $num ");}
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
	open(OUT,">./log_file/event_on.cgi") or &ERR('MAIN ���ο� �����͸� ������ �� �����ϴ�.');
	print OUT @EVENT_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>���ִ�ȸ�̺�Ʈ�� ����Ǿ����ϴ�.</h2><p>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='���ƿ´�'>
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
		$datames = "�˻� : $dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file�� �߰ߵ��� �ʾҽ��ϴ�.<br>\n";
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
<h2>ĳ���� ������</h2>
<br>
ID�� ���ϸ�� ���� �Ǿ����� �������� �����ּ���.<br>
ȣ��Ʈ���� ���÷� �����ϰ� �ֽ��ϴ�.<br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CHANGE>�����ϴ� ���� : 
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
	print "<option value=$eid\.cgi>������:$eos�ݣ�ID:$eid�ݣ��̸�:$ename�ݣ�ȣ��Ʈ:$ehost�ݣۺ��:$epass�ݣ��̸�:$email��\n";
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
<input type=submit value='����'>
<br></form>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=MENTE>
<br><input type=radio name=no value="1">ȣ��Ʈ�� ����(<font color=red>2�� ��� üũ</font>)<br>
<input type=radio name=no value="2">�̸���<br>
<input type=radio name=no value="3">ID����<br>
<input type=radio name=no value="4">���<br>
<input type=radio name=no value="5">�̸���<br>
<input type=radio name=no value="6">���� (Yes:1 | No:0)<br>
�̸��˻�<input type=text name=serch size=20><br>
<input type=submit value='��������'>
<br></form>

<h2>���� ����</h2>
2�ߵ���ڸ� ���� �����մϴ�.<BR>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=DEL_LIST>
<input type=submit value='������ ����Ʈ'>
<br></form>


2�ߵ�� �ǽ���(�̰� �ߴ� ����� �������� ���������Դϴ�. by ĥ��)<p>
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
		$datames = "�˻� : $dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file�� �߰ߵ��� �ʾҽ��ϴ�.<br>\n";
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
<h2>ĳ���� ������</h2>
<br>
ID�� ���ϸ�� ���� �Ǿ����� �������� �����ּ���.<br>
ȣ��Ʈ���� ���÷� �����ϰ� �ֽ��ϴ�.<br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CHANGE1>�����ϴ� ���� : 
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
	print "<option value=$eid\.cgi>������:$eos�ݣ�ID:$eid�ݣ��̸�:$ename�ݣ�ȣ��Ʈ:$ehost�ݣ��̸�:$email��\n";
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
<input type=submit value='����'></form>
<br>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=MENTE1>
<br><input type=radio name=no value="1">ȣ��Ʈ�� ����(<font color=red>2�� ��� üũ</font>)<br>
<input type=radio name=no value="2">�̸���<br>
<input type=radio name=no value="3">ID����<br>
<input type=radio name=no value="5">�̸���<br>
<input type=radio name=no value="6">����(Yes:1 | No:0)<br>
�̸��˻�<input type=text name=serch size=20><br>
<input type=submit value='��������'>
<br></form>

<h2>���� ����</h2>
2�ߵ���ڸ� ���� �����մϴ�.<BR>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=DEL_LIST>
<input type=submit value='������ ����Ʈ'>
<br></form>


2�ߵ�� �ǽ���(�̰� �ߴ� ĳ���͵� ������ ���ܹٶ��ϴ�. by ĥ��)<p>
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
	$goodname = "[Gm]����";
	$goodname1 = "b20";
	}elsif($in{'id'} eq "$adminid1"){
	$goodname = "[Gm]����";
	$goodname1 = "gm1";
	}elsif($in{'id'} eq "$adminid2"){
	$goodname = "[Gm]����";
	$goodname1 = "gm2";
	}elsif($in{'id'} eq "$adminid3"){
	$goodname = "[Gm]����";
	$goodname1 = "gm3";
	}

	open(IN,"$ADMIN_BBS");
	@AD_DATA = <IN>;
	close(IN);

	if($in{'message'} eq "") { &ERR2("�޼����� ���ԵǾ� ���� �ʽ��ϴ�."); }
	if(length($in{'message'}) > 50) { &ERR2("�� �� �����ϰ� ���� ���ּ���"); }

	$bbs_num = @AD_DATA;
	if($bbs_num > 40) { pop(@AD_DATA); }

	&MAP_LOG3("[$goodname] <a href=$in{'message1'} target=_blank>$in{'message'}</a>");

	unshift(@AD_DATA,"<font color=red>$in{'message'}</font> $goodname�� ($mday��$hour��$min��)<BR><hr size=0>\n");

	open(OUT,">$ADMIN_BBS");
	print OUT @AD_DATA;
	close(OUT);

	&HEADER;
	print <<"EOM";
<h2>�����߽��ϴ�.</h2>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='���ƿ´�'>
<br></form>
EOM
	&FOOTER;
	exit;
}

sub CHANGE {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("ID, �н����� ���� $num ");}
	$dir="./charalog/main";
	if(!open(page,"$dir/$in{'fileno'}")){
		$datames .= "$dir/$file�� �߰ߵ��� �ʾҽ��ϴ�.<br>\n";
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
<h3><img src="$IMG/$echara.gif" width="$img_wid" height="$img_height" border=0> <font size=5 color=orange>$ename</font>�� ����</h3>
<table>
<tr>
<th>ID</th><td><input type=text name=eid value='$eid'></td>
<th>PASS</th><td><input type=text name=epass value='$epass'></td>
<th>NAME</th><td><input type=text name=ename value='$ename'></td>
<th>�׸� ID</th><td><input type=text name=echara value='$echara'></td>
<tr>
<th>����</th><td><input type=text name=estr value='$estr'></td>
<th>����</th><td><input type=text name=eint value='$eint'></td>
<th>��ַ�</th><td><input type=text name=elea value='$elea'></td>
<th>�ŷ�</th><td><input type=text name=echa value='$echa'></td>
</TR>
<tr>
<th>�����</th><td><input type=text name=esol value='$esol'></td>
<th>�Ʒ�</th><td><input type=text name=egat value='$egat'></td>
<th>��</th><td><input type=text name=econ value='$econ'></td>
<th>��</th><td><input type=text name=egold value='$egold'></td>
</TR>
<tr>
<th>������</th><td><input type=text name=erice value='$erice'></td>
<th>����</th><td><input type=text name=ecex value='$ecex'></td>
<th>���ġ</th><td><input type=text name=eclass value='$eclass'></td>
<th>����</th><td><input type=text name=earm value='$earm'></td>
</TR>
<tr>
<th>����</th><td><input type=text name=ebook value='$ebook'></td>
<th>�漺</th><td><input type=text name=ebank value='$ebank'></td>
<th>����1</th><td><input type=text name=esub1 value='$esub1'></td>
<th>����2</th><td><input type=text name=esub2 value='$esub2'></td>
</TR>
<tr>
<th>���� ��ġ</th><td><input type=text name=epos value='$epos'></td>
<th>�޽���</th><td><input type=text name=emes value='$emes'></td>
<th>ȣ��Ʈ</th><td><input type=text name=ehost value='$ehost'></td>
<th>�����Ͻ�</th><td><input type=text name=edate value='$edate'></td>
</TR>
<tr>
<th>MAIL</th><td><input type=text name=email value='$email'></td>
<th>�ൿ üũ</th><td><input type=text name=eos value='$eos'></td>
<th>Ư��</th><td><input type=text name=eskill value='$eskill'></td>
<th>Ư������Ʈ</th><td><input type=text name=epoint value='$epoint'></td>
</TR>
<tr>
<th>����</th><td><input type=text name=ect value='$ect'></td>
<th>����</th><td><input type=text name=elevel value='$elevel'></td>
<th>����ġ</th><td><input type=text name=eexp value='$eexp'></td>
<th>����Ʈ��</th><td><input type=text name=ecodea value='$ecodea'></td>
</TR>
<tr>
<th>����Ʈ��</th><td><input type=text name=ecodeb value='$ecodeb'></td>
<th>����Ʈ����Ʈ</th><td><input type=text name=eqpoint value='$eqpoint'></td>
<th></th><td></td>
<th></th><td></td>
</TR>



</table>
<br>
<input type=hidden name=mode value=CHANGE2>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����'>
<br></form><form method="post" action="admin.cgi">
<input type=hidden name=mode value=GG>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����Ȯ��'>
<br></form><form method="post" action="admin.cgi">
<input type=hidden name=mode value=GG1>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��������'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='������ �׸��д�'>
</form>
<br>
<br>
<br>
<br>
MAP �α� ����<br>
<form method="post" action="admin.cgi">
<input type=hidden name=filename value=$in{'fileno'}>
<input type=hidden name=mode value=DEL>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�� ������ ����'>
</form>
<br>
<br>
<br>
MAP �α� ����<br>
<form method="post" action="admin.cgi">
<input type=hidden name=filename value=$in{'fileno'}>
<input type=hidden name=mode value=DEL2>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�� ������ ����'>
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
		$list .= "<option value=$qnum>������Ʈ����:$quest�����Ƿ���:$qname�������෹��:$qlevel�����ڵ�:$qcode�����ʼ��ڵ�:$qflag��";
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
<input type=submit value='����Ʈ ����'>
<br></form><form method="post" action="admin.cgi">
<input type=hidden name=mode value=QUEST_ADD>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����Ʈ ����'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����Ʈ�ۼ�����'>
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

		$list .= "<option value=$qnum>������Ʈ����:$quest�����Ƿ���:$qname�������෹��:$qlevel�����ڵ�:$qcode��";

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
<h3><font size=5 color=orange>����Ʈ $quest1</font>�� ����</h3>
<table border="1" cellspacing="0" width="900" bordercolordark="white" bordercolorlight="black">
    <tr>
        <td width="200" height="60" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ��ȣ</span></b></p>
        </td>
        <td width="300" height="60" bgcolor="#999999"><input type=text name=qnum1 value='$qnum1'></td>
        <td width="393" height="60" bgcolor="#999999">
            <p><span style="font-size:9pt;">����Ʈ�� ������ȣ�Դϴ�.</span></p>
            <p><span style="font-size:9pt;">�ٸ� ����Ʈ ��ȣ�� ���� ��ġ�� ���� 
            �ʽ��ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="91" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ�ڵ�</span></b></p>
        </td>
        <td width="300" height="91" bgcolor="#999999"><input type=text name=qcode1 value='$qcode1'></td>
        <td width="393" height="91" bgcolor="#999999">
            <p><span style="font-size:9pt;">����Ʈ�� �ڵ��ȣ�Դϴ�.</span></p>
            <p><span style="font-size:9pt;">����Ʈ�� �ڵ��ȣ�� A0~A9 ������ 
            B0~B9, C0~C9������ �Է��մϴ�.</span></p>
            <p><span style="font-size:9pt;">���� 9�̻��� �Ѿ�� ���� ���ĺ����� 
            ��ü����� �մϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">NPC���̹���</span></b></p>
        </td>
        <td width="300" bgcolor="#999999"><input type=text name=qface1 value='$qface1'></td>
        <td width="393" bgcolor="#999999">
            <p><span style="font-size:9pt;">NPC�� �� �̹����Դϴ�. ���� ��ϵ� 
            �ι��� ������ �����ϴ�.</span></p>
            <p><span style="font-size:9pt;">npc1 : ��� ��ĥ��</span></p>
            <p><span style="font-size:9pt;">npc2 : ���� ����</span></p>
            <p><span style="font-size:9pt;">npc3 : ģ���� �ռ���</span></p>
            <p><span style="font-size:9pt;">npc4 : ���� ������</span></p>
            <p><span style="font-size:9pt;">npc5 : ���� ������</span></p>
            <p><span style="font-size:9pt;">npc6 : â��ȣ</span></p>
            <p><span style="font-size:9pt;">npc7 : ���� ����õ</span></p>
            <p><span style="font-size:9pt;">npc8 : ���� ����</span></p>
            <p><span style="font-size:9pt;">npc9 : ���� ���̷�</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">NPC�̸���</span></b></td>
        <td width="300" bgcolor="#999999"><input type=text name=qname1 value='$qname1'></td>
        <td width="393" bgcolor="#999999">
            <p><span style="font-size:9pt;">NPC�� �̸��� ���� �� �̹����� 
            ���缭 ���ֽø� �˴ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">���ѷ���</span></b></p>
        </td>
        <td width="300" bgcolor="#999999"><input type=text name=qlevel1 value='$qlevel1'></td>
        <td width="393" bgcolor="#999999">
            <p><span style="font-size:9pt;">�� ����Ʈ�� ���� ���� �ʿ��� �����Դϴ�.</span></p>
            <p><span style="font-size:9pt;">�� ������ �������� ������ ����Ʈ�� 
            ������ �ʽ��ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="34" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ����</span></b></p>
        </td>
        <td width="300" height="34" bgcolor="#999900"><input type=text name=quest1 value='$quest1' size="40"></td>
        <td width="393" height="34" bgcolor="#999900">
            <p><span style="font-size:9pt;">����Ʈ�� ������ ǥ���մϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ�����</span></b></td>
        <td width="300" height="56" bgcolor="#999900"><textarea name=qtalka1 rows=15 cols=54>$not1</textarea></td>
        <td width="393" height="56" bgcolor="#999900">
            <p><span style="font-size:9pt;">����Ʈ�� ���ֹޱ� ���� ��簡 ��Ÿ���ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ�����</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#999900"><textarea name=qtalkb1 rows="15" cols="54">$not2</textarea></td>
        <td width="393" height="56" bgcolor="#999900">
            <p><span style="font-size:9pt;">����Ʈ�� ���ָ� �޾����� �Ϸ���� 
            �ʾ��� �� ��縦 ��Ÿ���ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ�Ϸ���</span></b></td>
        <td width="300" height="56" bgcolor="#999900"><textarea name=qtalkc1 rows="15" cols="54">$not3</textarea></td>
        <td width="393" height="56" bgcolor="#999900">
            <p><span style="font-size:9pt;">����Ʈ�� �Ϸ�Ǿ��� �� ��縦 ��Ÿ���ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="92" bgcolor="#999900">
            <p align="center"><span style="font-size:9pt;"><b>���ηα����</b></span></p>
        </td>
        <td width="300" height="92" bgcolor="#999900"><input type=text name="qtalkd1" value="$qtalkd1" size="40"></td>
        <td width="393" height="92" bgcolor="#999900">
            <p><span style="font-size:9pt;">����Ʈ�� ���� �߿� ���ηα׿� ��µǴ� 
            ������ ��Ÿ���ϴ�.</span></p>
            <p><span style="font-size:9pt;">��Ȳ�� ���缭 ��縦 �־��ֽø� 
            �˴ϴ�.</span></p>
            <p><span style="font-size:9pt;">����� ��ġ ������ �ƹ� �͵� ���� 
            ������ �˴ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">�ݾ׺���</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qgold1 value='$qgold1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� �ݾ��� �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">��������</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qrice1 value='$qrice1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� ������ �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">���°��躸��</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qstr1 value='$qstr1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� ���°��躸���� 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">���°��躸��</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qint1 value='$qint1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� ���°��躸���� 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">��ְ��躸��</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qlea1 value='$qlea1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� ��ְ��躸���� 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">�ŷ°��躸��</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qcha1 value='$qcha1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� �ŷ°��躸���� 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">����ġ����</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qcex1 value='$qcex1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� ����ġ ������ 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">����ġ����</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qexp1 value='$qexp1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� ����ġ ������ 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#FF6600">
            <p align="center"><b><span style="font-size:9pt;">��������â����</span></b></p>
        </td>
        <td width="300" bgcolor="#FF6600"><input type=text name=qseal1 value='$qseal1'></td>
        <td width="393" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">���� �������ͽ� ȭ�� â�� �ش� ����Ʈ�� 
            ������ �����ϰ� ����ؼ� ǥ���մϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#FF6600">
            <p align="center"><b><span style="font-size:9pt;">�ʼ�����Ʈ�ڵ�</span></b></p>
        </td>
        <td width="300" bgcolor="#FF6600"><input type=text name=qflag1 value='$qflag1'></td>
        <td width="393" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">�� ����Ʈ�� ���� ���ؼ� �ʿ��� ����Ʈ 
            �ڵ带 �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">������ �ʼ�����Ʈ�� Ŭ�������� ������ 
            �ش� ����Ʈ�� ������ �ʽ��ϴ�.</span></p>
            <p><span style="font-size:9pt;">��, ���� �� ���� ����Ʈ �ڵ常 �����ؾ� 
            �մϴ�.</span></p>
            <p><select name=questlist>$list</select></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="92" bgcolor="#FF6600">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ����</span></b></p>
        </td>
        <td width="300" height="92" bgcolor="#FF6600"><input type=text name=qcategory1 value='$qcategory1'></td>
        <td width="393" height="92" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">����Ʈ�� ������ �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">������ �� �ִ� ����Ʈ�� ������ �� 
            ���� �����ؾ� �ϰ�&nbsp;������ �����ϴ�.</span></p>
            <p><span style="font-size:9pt;">��� : �������</span></p>
            <p><span style="font-size:9pt;">��� : �������</span></p>
            <p><span style="font-size:9pt;">��� : �������</span></p>
            <p><span style="font-size:9pt;">�ν� : ���� ��ǰ</span></p>
            <p><span style="font-size:9pt;">���� : �⺴</span></p>
            <p><span style="font-size:9pt;">��� : ���</span></p>
            <p><span style="font-size:9pt;">��� : ���ü�����</span></p>
            <p><span style="font-size:9pt;">���� : �ٸ� ������� ����</span></p>
            <p><span style="font-size:9pt;">�м� : �ٸ� ������� �м�</span></p>
            <p><span style="font-size:9pt;">�Ͼ� : �Ͼ�</span></p>
            <p><span style="font-size:9pt;">�ϱ��� : �ܷ�⿡�� �ϱ����Է½�</span></p>
            <p><span style="font-size:9pt;">���� : �ܷ�⿡�� �����Է½�</span></p>
	<p><span style="font-size:9pt;">���� : ����</span></p>
	<p><span style="font-size:9pt;">�Ʒ� : �Ʒ�,���Ʒ�</span></p>
	<p><span style="font-size:9pt;">�۱� : �۱�</span></p>
	<p><span style="font-size:9pt;">�޽� : �޽�</span></p>
	<p><span style="font-size:9pt;">���� : ����</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#FF6600">
            <p align="center"><span style="font-size:9pt;"><b>����ƮȮ��</b></span></p>
        </td>
        <td width="300" height="56" bgcolor="#FF6600"><input type=text name="qrate1" value="$qrate1"></td>
        <td width="393" height="56" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">�ش� ����Ʈ�� ����� �����ϴ� Ȯ���� 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">100%�� �����ϸ� ������ �����մϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#FF6600">
            <p align="center"><span style="font-size:9pt;"><b>����Ʈ����ġ</b></span></p>
        </td>
        <td width="300" height="56" bgcolor="#FF6600"><input type=text name="qlimit1" value="$qlimit1"></td>
        <td width="393" height="56" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">����Ʈ�� Ŭ�����ϱ� ���� �ʿ��� ����ġ�� �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">����Ʈ�������� ���缭 ����ġ�� �����ؾ� �մϴ�.</span></p>
        </td>
    </tr>    <tr>
        <td width="200" height="56" bgcolor="#FF6600">
            <p align="center"><span style="font-size:9pt;"><b>����Ʈ������</b></span></p>
        </td>
        <td width="300" height="56" bgcolor="#FF6600"><input type=text name="qup1" value="$qup1"></td>
        <td width="393" height="56" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">����Ʈ�� ����ÿ� �þ�� ���� �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">���ڷ� �����ϸ� �ش� ���ڸ�ŭ �þ���� ������ ���� ���ڸ� ������ �ش� ��ġ��ŭ �����ϴ�.</span></p>
		<p><span style="font-size:9pt;">��� : �ڽ��� ���ġ��ŭ ���</span></p>
		<p><span style="font-size:9pt;">��� : �ڽ��� ���ġ��ŭ ���</span></p>
		<p><span style="font-size:9pt;">��� : �ڽ��� ���ġ��ŭ ���</span></p>
		<p><span style="font-size:9pt;">�ν� : �ڽ��� �ν�ġ��ŭ ���</span></p>
		<p><span style="font-size:9pt;">¡�� : �ڽ��� ¡������ŭ ���</span></p>
		<p><span style="font-size:9pt;">���� : �ڽ��� ��������ŭ ���</span></p>
	<p><span style="font-size:9pt;">��� : �ڽ��� ���ü���ŭ ���</span></p>
	<p><span style="font-size:9pt;">�Ʒ� : �ڽ��� �Ʒø�ŭ ���</span></p>
	<p><span style="font-size:9pt;">�۱� : �ڽ��� �۱ݾ׼���ŭ ���</span></p>
        </td>
    </tr>
</table>
<br>
<input type=hidden name=mode value=QUEST_EDIT_COM>
<input type=hidden name=questlist value=$in{'questlist'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����Ʈ ����'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����Ʈ�ۼ�����'>
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
		$list .= "<option value=$qnum>������Ʈ����:$quest�����Ƿ���:$qname�������෹��:$qlevel�����ڵ�:$qcode��";
		}

	&HEADER;
	print <<"EOM";
<form method="post" action="admin.cgi">
<h3><font size=5 color=orange>����Ʈ $quest1</font>�� ����</h3>
<table border="1" cellspacing="0" width="1111" bordercolordark="white" bordercolorlight="black">
    <tr>
        <td width="200" height="60" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ��ȣ</span></b></p>
        </td>
        <td width="300" height="60" bgcolor="#999999"><input type=text name=qnum1 value='$qnum1'></td>
        <td width="393" height="60" bgcolor="#999999">
            <p><span style="font-size:9pt;">����Ʈ�� ������ȣ�Դϴ�.</span></p>
            <p><span style="font-size:9pt;">�ٸ� ����Ʈ ��ȣ�� ���� ��ġ�� ���� 
            �ʽ��ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="91" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ�ڵ�</span></b></p>
        </td>
        <td width="300" height="91" bgcolor="#999999"><input type=text name=qcode1 value='$qcode1'></td>
        <td width="393" height="91" bgcolor="#999999">
            <p><span style="font-size:9pt;">����Ʈ�� �ڵ��ȣ�Դϴ�.</span></p>
            <p><span style="font-size:9pt;">����Ʈ�� �ڵ��ȣ�� A0~A9 ������ 
            B0~B9, C0~C9������ �Է��մϴ�.</span></p>
            <p><span style="font-size:9pt;">���� 9�̻��� �Ѿ�� ���� ���ĺ����� 
            ��ü����� �մϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">NPC���̹���</span></b></p>
        </td>
        <td width="300" bgcolor="#999999"><input type=text name=qface1 value='$qface1'></td>
        <td width="393" bgcolor="#999999">
            <p><span style="font-size:9pt;">NPC�� �� �̹����Դϴ�. ���� ��ϵ� 
            �ι��� ������ �����ϴ�.</span></p>
            <p><span style="font-size:9pt;">npc1 : ��� ��ĥ��</span></p>
            <p><span style="font-size:9pt;">npc2 : ���� ����</span></p>
            <p><span style="font-size:9pt;">npc3 : ģ���� �ռ���</span></p>
            <p><span style="font-size:9pt;">npc4 : ���� ������</span></p>
            <p><span style="font-size:9pt;">npc5 : ���� ������</span></p>
            <p><span style="font-size:9pt;">npc6 : â��ȣ</span></p>
            <p><span style="font-size:9pt;">npc7 : ���� ����õ</span></p>
            <p><span style="font-size:9pt;">npc8 : ���� ����</span></p>
            <p><span style="font-size:9pt;">npc9 : ���� ���̷�</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">NPC�̸���</span></b></td>
        <td width="300" bgcolor="#999999"><input type=text name=qname1 value='$qname1'></td>
        <td width="393" bgcolor="#999999">
            <p><span style="font-size:9pt;">NPC�� �̸��� ���� �� �̹����� 
            ���缭 ���ֽø� �˴ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#999999">
            <p align="center"><b><span style="font-size:9pt;">���ѷ���</span></b></p>
        </td>
        <td width="300" bgcolor="#999999"><input type=text name=qlevel1 value='$qlevel1'></td>
        <td width="393" bgcolor="#999999">
            <p><span style="font-size:9pt;">�� ����Ʈ�� ���� ���� �ʿ��� �����Դϴ�.</span></p>
            <p><span style="font-size:9pt;">�� ������ �������� ������ ����Ʈ�� 
            ������ �ʽ��ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="34" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ����</span></b></p>
        </td>
        <td width="300" height="34" bgcolor="#999900"><input type=text name=quest1 value='$quest1' size="84"></td>
        <td width="393" height="34" bgcolor="#999900">
            <p><span style="font-size:9pt;">����Ʈ�� ������ ǥ���մϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ�����</span></b></td>
        <td width="300" height="56" bgcolor="#999900"><textarea name=qtalka1 rows="15" cols="54">$not1</textarea></td>
        <td width="393" height="56" bgcolor="#999900">
            <p><span style="font-size:9pt;">����Ʈ�� ���ֹޱ� ���� ��簡 ��Ÿ���ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ�����</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#999900"><textarea name=qtalkb1 rows="15" cols="54">$not2</textarea></td>
        <td width="393" height="56" bgcolor="#999900">
            <p><span style="font-size:9pt;">����Ʈ�� ���ָ� �޾����� �Ϸ���� 
            �ʾ��� �� ��縦 ��Ÿ���ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#999900">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ�Ϸ���</span></b></td>
        <td width="300" height="56" bgcolor="#999900"><textarea name=qtalkc1 rows="15" cols="54">$not3</textarea></td>
        <td width="393" height="56" bgcolor="#999900">
            <p><span style="font-size:9pt;">����Ʈ�� �Ϸ�Ǿ��� �� ��縦 ��Ÿ���ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="92" bgcolor="#999900">
            <p align="center"><span style="font-size:9pt;"><b>���ηα����</b></span></p>
        </td>
        <td width="300" height="92" bgcolor="#999900"><input type=text name="qtalkd1" value="$qtalkd1" size="40"></td>
        <td width="393" height="92" bgcolor="#999900">
            <p><span style="font-size:9pt;">����Ʈ�� ���� �߿� ���ηα׿� ��µǴ� 
            ������ ��Ÿ���ϴ�.</span></p>
            <p><span style="font-size:9pt;">��Ȳ�� ���缭 ��縦 �־��ֽø� 
            �˴ϴ�.</span></p>
            <p><span style="font-size:9pt;">����� ��ġ ������ �ƹ� �͵� ���� 
            ������ �˴ϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">�ݾ׺���</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qgold1 value='$qgold1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� �ݾ��� �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">��������</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qrice1 value='$qrice1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� ������ �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">���°��躸��</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qstr1 value='$qstr1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� ���°��躸���� 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">���°��躸��</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qint1 value='$qint1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� ���°��躸���� 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">��ְ��躸��</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qlea1 value='$qlea1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� ��ְ��躸���� 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">�ŷ°��躸��</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qcha1 value='$qcha1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� �ŷ°��躸���� 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">����ġ����</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qcex1 value='$qcex1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� ����ġ ������ 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#00CC00">
            <p align="center"><b><span style="font-size:9pt;">����ġ����</span></b></p>
        </td>
        <td width="300" height="56" bgcolor="#00CC00"><input type=text name=qexp1 value='$qexp1'></td>
        <td width="393" height="56" bgcolor="#00CC00">
            <p><span style="font-size:9pt;">����Ʈ�Ϸ�� ����޴� ����ġ ������ 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">��ġ������ 0���� ����.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#FF6600">
            <p align="center"><b><span style="font-size:9pt;">��������â����</span></b></p>
        </td>
        <td width="300" bgcolor="#FF6600"><input type=text name=qseal1 value='$qseal1'></td>
        <td width="393" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">���� �������ͽ� ȭ�� â�� �ش� ����Ʈ�� 
            ������ �����ϰ� ����ؼ� ǥ���մϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" bgcolor="#FF6600">
            <p align="center"><b><span style="font-size:9pt;">�ʼ�����Ʈ�ڵ�</span></b></p>
        </td>
        <td width="300" bgcolor="#FF6600"><input type=text name=qflag1 value='$qflag1'></td>
        <td width="393" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">�� ����Ʈ�� ���� ���ؼ� �ʿ��� ����Ʈ 
            �ڵ带 �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">������ �ʼ�����Ʈ�� Ŭ�������� ������ 
            �ش� ����Ʈ�� ������ �ʽ��ϴ�.</span></p>
            <p><span style="font-size:9pt;">��, ���� �� ���� ����Ʈ �ڵ常 �����ؾ� 
            �մϴ�.</span></p>
            <p><select name=questlist>$list</select></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="92" bgcolor="#FF6600">
            <p align="center"><b><span style="font-size:9pt;">����Ʈ����</span></b></p>
        </td>
        <td width="300" height="92" bgcolor="#FF6600"><input type=text name=qcategory1 value='$qcategory1'></td>
        <td width="393" height="92" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">����Ʈ�� ������ �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">������ �� �ִ� ����Ʈ�� ������ �� 
            ���� �����ؾ� �ϰ�&nbsp;������ �����ϴ�.</span></p>
            <p><span style="font-size:9pt;">��� : �������</span></p>
            <p><span style="font-size:9pt;">��� : �������</span></p>
            <p><span style="font-size:9pt;">��� : �������</span></p>
            <p><span style="font-size:9pt;">�ν� : ���� ��ǰ</span></p>
            <p><span style="font-size:9pt;">���� : �⺴</span></p>
            <p><span style="font-size:9pt;">��� : ���</span></p>
            <p><span style="font-size:9pt;">��� : ���ü�����</span></p>
            <p><span style="font-size:9pt;">���� : �ٸ� ������� ����</span></p>
            <p><span style="font-size:9pt;">�м� : �ٸ� ������� �м�</span></p>
            <p><span style="font-size:9pt;">�Ͼ� : �Ͼ�</span></p>
            <p><span style="font-size:9pt;">�ϱ��� : �ܷ�⿡�� �ϱ����Է½�</span></p>
            <p><span style="font-size:9pt;">���� : �ܷ�⿡�� �����Է½�</span></p>
	<p><span style="font-size:9pt;">���� : ����</span></p>
	<p><span style="font-size:9pt;">�Ʒ� : �Ʒ�,����</span></p>
	<p><span style="font-size:9pt;">�۱� : �۱�</span></p>
	<p><span style="font-size:9pt;">�޽� : �޽�</span></p>
	<p><span style="font-size:9pt;">���� : ����</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#FF6600">
            <p align="center"><span style="font-size:9pt;"><b>����ƮȮ��</b></span></p>
        </td>
        <td width="300" height="56" bgcolor="#FF6600"><input type=text name="qrate1" value="$qrate1"></td>
        <td width="393" height="56" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">�ش� ����Ʈ�� ����� �����ϴ� Ȯ���� 
            �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">100%�� �����ϸ� ������ �����մϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#FF6600">
            <p align="center"><span style="font-size:9pt;"><b>����Ʈ����ġ</b></span></p>
        </td>
        <td width="300" height="56" bgcolor="#FF6600"><input type=text name="qlimit1" value="$qlimit1"></td>
        <td width="393" height="56" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">����Ʈ�� Ŭ�����ϱ� ���� �ʿ��� ����ġ�� �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">����Ʈ�������� ���缭 ����ġ�� �����ؾ� �մϴ�.</span></p>
        </td>
    </tr>
    <tr>
        <td width="200" height="56" bgcolor="#FF6600">
            <p align="center"><span style="font-size:9pt;"><b>����Ʈ������</b></span></p>
        </td>
        <td width="300" height="56" bgcolor="#FF6600"><input type=text name="qup1" value="$qup1"></td>
        <td width="393" height="56" bgcolor="#FF6600">
            <p><span style="font-size:9pt;">����Ʈ�� ����ÿ� �þ�� ���� �����մϴ�.</span></p>
            <p><span style="font-size:9pt;">���ڷ� �����ϸ� ���ڸ�ŭ �þ���� ������ ���� ���ڸ� ������ �ش� ��ġ��ŭ �����ϴ�.</span></p>
		<p><span style="font-size:9pt;">��� : �ڽ��� ���ġ��ŭ ���</span></p>
		<p><span style="font-size:9pt;">��� : �ڽ��� ���ġ��ŭ ���</span></p>
		<p><span style="font-size:9pt;">��� : �ڽ��� ���ġ��ŭ ���</span></p>
		<p><span style="font-size:9pt;">�ν� : �ڽ��� �ν�ġ��ŭ ���</span></p>
		<p><span style="font-size:9pt;">¡�� : �ڽ��� ¡������ŭ ���</span></p>
	<p><span style="font-size:9pt;">���� : �ڽ��� ��������ŭ ���</span></p>
	<p><span style="font-size:9pt;">��� : �ڽ��� ���ü����ุŭ ���</span></p>
	<p><span style="font-size:9pt;">�Ʒ� : �ڽ��� �Ʒø�ŭ ���</span></p>
	<p><span style="font-size:9pt;">�۱� : �ڽ��� �۱ݾ׼���ŭ ���</span></p>
        </td>
    </tr>
</table>
</table>
<br>
<input type=hidden name=mode value=QUEST_ADD_COM>
<input type=hidden name=questlist value=$in{'questlist'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����Ʈ ����'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����Ʈ��������'>
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
			&ERR2("<font color=red>����Ʈ ��ȣ�� �̹� �ֽ��ϴ�.</font>");
			}else{
			push(@NEW_QUEST,"$_");
			}
		}

	unshift(@NEW_QUEST,"$in{'qnum1'}<>$in{'qcode1'}<>$in{'qface1'}<>$in{'qname1'}<>$in{'qlevel1'}<>$in{'quest1'}<>$in{'qlimit1'}<>$in{'qtalka1'}<>$in{'qtalkb1'}<>$in{'qtalkc1'}<>$in{'qgold1'}<>$in{'qrice1'}<>$in{'qstr1'}<>$in{'q$int1'}<>$in{'qlea1'}<>$in{'qcha1'}<>$in{'qcex1'}<>$in{'qexp1'}<>$in{'qseal1'}<>$in{'qflag1'}<>$in{'qcategory1'}<>$in{'qrate1'}<>$in{'qtalkd1'}<>$in{'qup1'}<>\n");
	open(OUT,">$QUEST_DATA");
	print OUT @NEW_QUEST;
	close(OUT);
	&ADMIN_LOG("<font color=blue>����Ʈ $in{'quest1'}�� �����߽��ϴ�.</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>����Ʈ $in{'quest1'}�� �����߽��ϴ�.</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='���ƿ´�'>
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
	&ADMIN_LOG("<font color=blue>����Ʈ $in{'quest1'}�� �����߽��ϴ�.</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>����Ʈ $in{'quest1'}�� �����߽��ϴ�.</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='���ƿ´�'>
</form>
EOM

	&FOOTER;
	exit;
}



sub CHANGE1 {

	$dir="./charalog/main";
	if(!open(page,"$dir/$in{'fileno'}")){
		$datames .= "$dir/$file�� �߰ߵ��� �ʾҽ��ϴ�.<br>\n";
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
<h3><img src="$IMG/$echara.gif" width="$img_wid" height="$img_height" border=0> <font size=5 color=orange>$ename</font>�� ����</h3>
<table>
<tr>
<th>ID</th><td>$eid</td>
<th>NAME</th><td>$ename</td>
<th>�׸� ID</th><td>$echara</td>
<th></th><td></td>
<tr>
<th>����</th><td>$estr</td>
<th>����</th><td>$eint</td>
<th>��ַ�</th><td>$elea</td>
<th>�ŷ�</th><td>$echa</td>
</TR>
<tr>
<th>ȣ��Ʈ</th><td>$ehost</td>
<th>�����Ͻ�</th><td>$edate</td>
<th>MAIL</th><td>$email</td>
<th>����(Yes:1,No:0)</th><td>$eos</td>
</TR>
<tr>
<th>����ġ</th><td>$eexp</td>
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
<input type=submit value='����Ȯ��'>
<br></form><form method="post" action="admin.cgi">
<input type=hidden name=mode value=GG1>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��������'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='������ �׸��д�'>
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
	
&ADMIN_LOG("<font color=blue>$in{'ename'} $dir/$in{'fileno'}�� �����߽��ϴ�. ��$host��</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>$in{'ename'} �� ���� $dir/$in{'fileno'}�� �����߽��ϴ�.</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='���ƿ´�'>
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
				&ERR2("���� ���� ����!");
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
	$goodname = "[Gm]ĥ��";
	}elsif($in{'id'} eq "$adminid1"){
	$goodname = "[Gm]����";
	}elsif($in{'id'} eq "$adminid2"){
	$goodname = "[Gm]����";
	}elsif($in{'id'} eq "$adminid3"){
	$goodname = "[Gm]����";
	}

&ADMIN_LOG("<font color=blue>$goodname���� $goodi���� �����Ϸ��߽��ϴ�.</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>$goodname���� $goodi���� �����Ϸ��߽��ϴ�.</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='���ƿ´�'>
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
				&ERR2("���� ���� ����!");
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
	
&ADMIN_LOG("<font color=blue>$goodi���� ���������߽��ϴ�. ��$host��</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>$goodi���� ���������߽��ϴ�.</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='���ƿ´�'>
</form>
EOM

	&FOOTER;
	exit;
}

sub DEL {

&HOST_NAME;
	open(IN,"./charalog/main/$in{'filename'}") or &ERR2('�� ������ ������ �� �����ϴ�.');
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

&ADMIN_LOG("<font color=red>$kname�� �����߽��ϴ�. ��$host�� </font>");

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

	unshift(@S_MOVE,"<img src=$IMG/j17.gif> $kname�� �����Ǿ����ϴ�.($mday��$hour��$min��)\n");
	splice(@S_MOVE,20);

	open(OUT,">$MAP_LOG_LIST") or &ERR2('LOG ���ο� �����͸� ������ �� �����ϴ�.');
	print OUT @S_MOVE;
	close(OUT);

	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$kname�� �����߽��ϴ�.</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='���ƿ´�'>
<br></form>
EOM

	&FOOTER;
	exit;
}

sub DEL2 {

&HOST_NAME;
	open(IN,"./charalog/main/$in{'filename'}") or &ERR2('������ ������ �� �����ϴ�.');
	@CN_DATA = <IN>;
	close(IN);
	($kid,$kpass,$kname) = split(/<>/,$CN_DATA[0]);

			$dir2="./charalog/main";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/log";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/command";
			unlink("$dir2/$in{'filename'}");
&ADMIN_LOG("<font color=red>$kname�� �����߽��ϴ�. ��$host�� </font>");

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
<center><h2><font color=red>$kname�� �����߽��ϴ�.</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='���ƿ´�'>
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

	unshift(@A_LOG,"$_[0]($mday��$hour��$min��)<BR>\n");
	splice(@A_LOG,20);

	open(OUT,">$ADMIN_LIST") or &ERR2('LOG ���ο� �����͸� ������ �� �����ϴ�');
	print OUT @A_LOG;
	close(OUT);
	if (-e $lockfile) { unlink($lockfile); }
}


sub INIT_DATA {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�н����� ���� $num ");}

	require "reset.cgi";
	&RESET_MODE;
&HOST_NAME;

	&ADMIN_LOG("�������͸� �ʱ�ȭ�߽��ϴ�.[$host]");
	
	&HEADER;
	print <<"EOM";
<h2><font color=red>�������͸� �ʱ�ȭ�߽��ϴ�.</h2></font>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='���ƿ´�'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}
1;
