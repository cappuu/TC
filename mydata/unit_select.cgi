
sub UNIT_SELECT {

	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&COUNTRY_DATA_OPEN($kcon);


	open(IN,"$TOWN_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
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
				&ERR("���� ���� ����!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);


	open(IN,"$UNIT_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
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
				$u_mes = "�Դ�ź�";
			}else{
				$u_mes = "�Դ�³�";
			}
			$unit_party .= "<TR><TD bgcolor=$TD_C3><input type=radio name=unit_id value=$unit_id></TD><TD bgcolor=$TD_C2><img src=\"$IMG/$uchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$uname\"></TD><TD bgcolor=$TD_C1><center><b>$uunit_name�δ�</b><BR>�δ��� : <a href=\"javascript:info('$uid')\">��$uname��</a><br>��ġ:$zname��</TD><td bgcolor=$TD_C1>$unit_list</td><td bgcolor=$TD_C2><center>$unit_num / <font color=red>$good</font></td><td bgcolor=$TD_C2>$umes</td><TD bgcolor=$TD_C1><center>$u_mes</TD></tr>";
		}

		if($uid eq $kid){
			$k_hit=1;
			$kunit_name = $uunit_name;
		}
	}

	if(!$k_hit){
		$kunit_name = "����";
	}

	if($xking eq $kid || $x0 eq $kid || $x1 eq $kid || $x2 eq $kid|| $x3 eq $kid || $x4 eq $kid || $x5 eq $kid ||$x6 eq $kid ||$x7 eq $kid ||$x8 eq $kid || $x9 eq $kid || $x10 eq $kid|| $x11 eq $kid || $x12 eq $kid || $x13 eq $kid || $x14 eq $kid || $x15 eq $kid || $x16 eq $kid || $x17 eq $kid || $x18 eq $kid || $x19 eq $kid || $x20 eq $kid || $x21 eq $kid || $x22 eq $kid || $x23 eq $kid || $x24 eq $kid || $x25 eq $kid || $x26 eq $kid){
		$come ="<input type=submit value=�δ�â��>";
		}else{$come = "���������ε鸸 â���� �� �ֽ��ϴ�.";}


	&HEADER;

	print <<"EOM";
<table width="100%" cellpadding="0" cellspacing="0" border=0><tr><td>
<TABLE WIDTH="100%" border=0>
<TBODY><TR>
<TD BGCOLOR=$ELE_BG[$kele] WIDTH=100% height=5> <font color=$ELE_C[$kele] size=4>����������<B> * �δ� ��ӡ���*</B>����</font></TD>
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
<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>����</TD><TH>$kstrt</TH><TD>����</TD><TH>$kintt</TH><TD>��ַ�</TD><TH>$kleat</TH></TR>
<TR><TD>��</TD><TH>$kgold</TH><TD>��</TD><TH>$krice</TH><TD>����</TD><TH>$kcex</TH></TR>
<TR><TD><center>$kname</TD><TH colspan=2></TH><TD>����</TD><TH>$ksol</TH><TD>�Ʒ�</TD><TH>$kgat</TH></TR>
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
<TR><TD width="100%" bgcolor=$TALK_BG><font color=$TALK_FONT><center>���⿡���� �ڱ��� �Ҽ��ϴ� �δ븦 ����� ���� �ֽ��ϴ�.<BR> �δ뿡 �Ҽ��ϸ� �δ� ä���̳� ���� Ŀ�ǵ�� ������ �ϱ� �������ϴ�.<br>����� ���� <font color=red>$kunit_name</font> �δ뿡 �Ҽ��� �ֽ��ϴ�.<BR>�δ�â���� ���������ε鸸 �� �� �ְ� ������ ������ �� �� �ֽ��ϴ�.<br>�δ�â����� <font color=red>�� 1000 ��</font>�Դϴ�.<br>�δ����� ���������ο��� �ڽ��� �ŷ�/8 ��ŭ ������ �� �ֽ��ϴ�.<br>���ս� ���տ����� �Ƿε��� �ö󰡰� �Ǹ� ���� 500���̻� ������ �ִ� �δ������ ������ �� �����ϴ�.</font></TD>
<TD bgcolor=$TD_C4></TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD><BR><BR>
<form action="$FILE_MYDATA" method="post">
<CENTER><TABLE bgcolor=$TABLE_C><TBODY><TR>
<TD bgcolor=$TD_C3>����</TD><TD bgcolor=$TD_C2><center>����</TD><TD bgcolor=$TD_C1><center>�δ��</TD><TD bgcolor=$TD_C1><center>��ӵ� �δ����</TD><TD bgcolor=$TD_C1><center>�δ��/��������</TD><TD bgcolor=$TD_C2><center>�δ� ���� �޼���</TD><TD bgcolor=$TD_C1><center>�Դ���������</TD></TR>
EOM


print <<"EOM";
$unit_party
</TR></TBODY></TABLE></CENTER>
�ڽ��� �δ����� ��<br>$com_list
<BR>
<center><input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=UNIT_ENTRY>
<input type=submit value="�ش� �δ뿡 �Ҽӵ˴ϴ�."></form>
<HR size=0>
<h3><font color=3355AA><img src="$IMG/b6.gif"></h3>

<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=UNIT_CHANGE>
<input type=submit value="�Դ� �źΡ��㰡"></form>
* �����ϸ� �ٸ� ����� �� �δ뿡 �Դ��� �� ���� �˴ϴ�.<p>

<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<select name=did>$u_member</select>
<input type=hidden name=mode value=UNIT_OUT>
<input type=submit value="�δ�� �ذ�"></form>
* �����ϸ� �� �δ���� ������մϴ�.<p>


<HR size=0>

<b class=\"clit\"><img src="$IMG/b7.gif">
<form action="$FILE_MYDATA" method="post">
<TABLE bgcolor=$TABLE_C><TR><TD bgcolor=$TD_C3><center>�δ��</TD><TD bgcolor=$TD_C2><input type=text name=name size=30><BR>[���� �빮�ڷ� 2~8���� �̳�]</TD></TR>
<TD bgcolor=$TD_C3>�δ� ������ �ڸ�Ʈ</TD><TD bgcolor=$TD_C2><input type=text name=mes size=30><BR>[���� �빮�ڷ� 0~20 ���� �̳�]</TD>
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
<input type=submit value="�δ� Ż�� & �ػ�"></form>
<HR size=0>


<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�޴��� ���ƿ´�"></form>
</TD>
</TR>
</TBODY></TABLE>
</td></tr></table>
EOM

	&FOOTER;
	exit;
}
1;