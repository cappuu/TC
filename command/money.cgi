sub MONEY {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}
	&CHARA_MAIN_OPEN;

	&TIME_DATA;
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	&HEADER;
	$no = $in{'no'} + 1;


	$get_sol = $klea - $ksol;
	print <<"EOM";
<TABLE border=0 width=100% height=80%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH>
<img src="$IMG/b12.gif">
</TH></TR>
EOM
	if("$ENV{'HTTP_REFERER'}" eq "$SANGOKU_URL/status.cgi"){ 

print <<"EOM";

<TR><TD>
<center><TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>����</TD><TH>$kstr</TH><TD>����</TD><TH>$kint</TH><TD>��ַ�</TD><TH>$klea</TH></TR>
<TR><TD>��</TD><TH>$kgold</TH><TD>��</TD><TH>$krice</TH><TD>����</TD><TH>$kcex</TH></TR>
<TR><TD>�Ҽӱ�</TD><TH colspan=2>$cou_name[$kcon]��</TH><TD>����</TD><TH>$ksol</TH><TD>�Ʒ�</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
EOM
	}
print <<"EOM";

<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<center><font color=white>�ٸ� ���÷� �̵��մϴ�.<BR></font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<center>���� �̵��Ͻðڽ��ϱ�?
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<select name=num>
EOM

	$xx=0;
	foreach(@town_name){
		if($xx < 53){
		print "<option value=$xx>$town_name[$xx]";
		}else{}
		$xx++;
	}

	foreach(@z){
		if("$_" ne ""){
			$move_list .= "$town_name[$_]<BR>";
		}
	}
print <<"EOM";
</select>


<p><font color=red>[$zname�κ��� �̵������� �Ÿ�]</font><br><BR>$move_list
$no_list
<br>
<center><input type=hidden name=mode value=20>
<input type=submit value="�̵��Ѵ�"></form>


<center><form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="���ƿ´�"></form></CENTER>
</TD></TR></TABLE>
</TD></TR></TABLE>

EOM

	&FOOTER;

	exit;

}
1;