sub TANREN {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;

	&HEADER;
	$no = $in{'no'} + 1;

	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}
	$get_sol = $klea - $ksol;
	print <<"EOM";
<TABLE border=0 width=100% height=80%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH>
<img src="$IMG/b10.gif">
</TH></TR>
<TR><TD>

<center><TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>����</TD><TH>$kstr</TH><TD>����</TD><TH>$kint</TH><TD>��ַ�</TD><TH>$klea</TH></TR>
<TR><TD>��</TD><TH>$kgold</TH><TD>��</TD><TH>$krice</TH><TD>����</TD><TH>$kcex</TH></TR>
<TR><TD>�Ҽӱ�</TD><TH colspan=2>$cou_name[$kcon]��</TH><TD>����</TD><TH>$ksol</TH><TD>�Ʒ�</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<center><font color=white>������ �״� ������ ������ �����ϴ�.<BR>������ �����Դϴ�.<BR>����ġ�� 10 ����Ʈ�� ������ �ɷ�ġ�� ����մϴ�.<br><b>��, �ø����� �ϴ� �ɷ�ġ�� 90 �̻��� �Ǿ������ ������ �� �� �ֽ��ϴ�.</b></font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<center>��� �ɷ��� �����մϱ�?
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<select name=num>
<option value=1>����
<option value=2>����
<option value=3>��ַ�
<option value=4>�ŷ�
</select>
$no_list
<input type=hidden name=mode value=27>
<input type=submit value="�����Ѵ�"></form>


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