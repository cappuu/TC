sub RESISDENTS {

	&CHARA_MAIN_OPEN;

$P_MES[0] = "�������!<br>Ȥ�� �߿����� ó�� �����ô� ��������?<br>����~ �� �⺻���� ������ ����� �帧, �÷��̾��� ������ ���� �������ٰԿ�.";
$P_MES[1] = "�� ������ ��ǥ�� ���ֿ� ���ϵ��� �ս��Ͽ� �ڽ��� ������ õ�����Ͻ�Ű�°ſ���.<br>��? �� ������ �˰� ��ôٱ���?<br>������ �������� ������� ���ս�Ų�ٴ� �� �������� �ƴҲ�����.";
$P_MES[2] = "�� ������ 2�ð����� 1�Ͼ� ���ŵſ�<BR>2�ð� ����ϸ� ������ ������ ����ȴ�ϴ�.<br>�� 1���� 12�����̸� 1���� �Ϸ簡 �Ǵ°ſ���.<br>�� �Ϸ縶�� 1�⾿ �������ٰ� ���� �ǿ�.";
$P_MES[3] = "���� ����Ǹ� �����Ŀ�ǵ忡 �����Ǿ��� ������� ������ �ൿ�� ����Ű�� �ȴ�ϴ�.<BR>�ִ� 24�ϱ��� ������ �����ϴϱ� �ൿ�� ������ �ʰ� �Ϸ翡 �ѹ����� ����� �����ּžߵǿ�.<br>������ ���ϰ� ��� ĳ���͸� ��ġ�ϸ� ���������ϰ� �Ǵ� �����Ͻñ���.";
$P_MES[4] = "�ʺ����Ӹ� �ƴ϶� �Ǳ� �ʱ⿡�� ���� Ŀ�ǵ带 ������ ���ּž� �ؿ�.<BR>������ ������ �ٰ��̿�! �����̴ϱ��..<br>�ο�� �͸��� �ɻ簡 �ƴ϶��ϴ�.<br>�������� ���, ����, ��, ������ �־��.";
$P_MES[5] = "������ 7���� �ķ� ��Ȯ��, ����� 1���� ���� ���Կ� ������ ��Ĩ�ϴ�.<BR>������ �����ϰ� �־� ���ݹ��� �� ���� ���輺�� �����ÿ��� ���� ��ȭ��Ű�� �͵� ���� ����Դϴ�.";
$P_MES[6] = "������ ��� ���� źź�ϰ� ������ ����� ���ٸ� Ÿ������ ������ �ɾ����!<BR>�ܵ����� �����ϴ� �ͺ��ٵ� �ڱ��� ������ ȸ�Ǹ� ���� �߼��źδ�� �⺴�δ�, �����δ븦 �����ؼ� �����ϴ� ���� ȿ�����̶��ϴ�.";
$P_MES[7] = "�����ϼ̾��. �⺻���� ������ �����׿�.<br>��� �̰� �⺻���ΰŰ� �߿����� �ο�ٺ��� �����ٵ� �ɼ������ǰſ���!";
	&HEADER;

	print <<"EOM";
<TABLE WIDTH="100%" height=100%>
<TBODY><TR>
<TD WIDTH=100% height=5> <font size=4>����������<B> * ������ ���� *</B>����</font></TD>
</TR><TR>
<TD bgcolor=$TD_C4 height=5>
<TABLE border="0"><TBODY>
<TR>
<TD bgcolor=$TD_C1><img src="$IMG/$kchara.gif"></TD>
<TD bgcolor=$TD_C2>$simg</TD>
<TD bgcolor=$TD_C3>$timg</TD>
<TD bgcolor=$TD_C4 WIDTH=100% align=center>
<TABLE bgcolor=$TABLE_C border="0">
<TBODY>
<TR>
<TD bgcolor=$TD_C2>�̸�</TD>
<TD bgcolor=$TD_C3>����</TD>
<TD bgcolor=$TD_C2>�Ӽ�</TD>
<TD bgcolor=$TD_C3>����</TD>
</TR>
<TR>
<TD bgcolor=$TD_C2>$kname</TD>
<TD bgcolor=$TD_C3 align=right>$klv</TD>
<TD bgcolor=$TD_C2>$ELE[$kele]��</TD>
<TD bgcolor=$TD_C3>$SYOKU[$kclass]</TD>
</TR>
<TR>
<TD bgcolor=$TD_C2>������</TD>
<TD bgcolor=$TD_C1 colspan=3 align=right>$kgold GOLD</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD height="5">
<TABLE  border="0"><TBODY>
<TR><TD bgcolor=$TD_C4><img src="$IMG/wiz.gif" title="�ﱹ�� �������� NET ���̵�"></TD><TD width="100%" height=100 bgcolor=$TALK_BG><font size=3 color=$TALK_FONT>$P_MES[$in{'num'}]</font></TD>

</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD>
EOM
	$new_num = $in{'num'}+1;
if($new_num < @P_MES){
print "<form action=\"$FILE_ENTRY\" method=\"post\">
<input type=hidden name=id value=$kid>
<input type=hidden name=num value=$new_num>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=RESISDENTS>
<input type=submit value=\"������\"></form>";
}
print<<"EOM";
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="������ �����Ѵ�"></form>

</TD>
</TR>
</TBODY></TABLE>
EOM

	&FOOTER;
	exit;
}
1;