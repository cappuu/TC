sub ATTESTATION {

	&HEADER;
print <<NEW;
<center>�� ���Ͽ� ÷�ε� ����Ű�� ID�� �н����带 �Է����ֽʽÿ�.<BR>
�� ���� Ű�� ��ϵǸ� ������ ������ ���� �ֽ��ϴ�.<p>

<center><form method=$method action=$FILE_ENTRY>
<table bgcolor=$TABLE_C><tbody bgcolor=$TD_C3>
<TR><TH bgcolor=$TD_C2 colspan=2>����</TH></TR>
<TR><TH>ID</TH><TD>
<input type=text name=id class=text size=10></TD></TR>
<TR><TH>�н�����</TH><TD>
<input type=password name=pass class=text size=10></TD></TR>
<TR><TH>���� Ű</TH><TD>
<input type=password name=key class=text size=10></TD></TR>
</TD></TR>
<input type=hidden name=mode value="SET_ENTRY">
<TR><TD bgcolor=$TD_C4 colspan=2 align=center><input type=submit value="����"></TD></TR>
</TBODY></TABLE>
</form>

NEW
	&FOOTER;
	exit;
}

sub SET_ENTRY {

	&HOST_NAME;
	&CHARA_MAIN_OPEN;
	$akey = crypt("$kpass",wd);

	if($akey ne $in{'key'}){&ERR2("���� Ű�� �ٸ��ϴ�.\n");}
	if(($kos & 1) eq 1){&ERR2("�̹� ������ ���� �����Դϴ�.");}

	&MAP_LOG("<img src=$IMG/j14.gif> $kname���� �������������� �Ϸ��ϼ̽��ϴ�..");
	$kos|=1;

	&CHARA_MAIN_INPUT;
	&HEADER;

	print qq|������ �Ϸ��߽��ϴ�.<br>\n|;
	print qq|ID�� $kid�Դϴ�.<br>\n|;
	print qq|�н������ $kpass�Դϴ�.<br><br>\n|;

	print qq|���������� �̰����� �Ϸ��Դϴ�.<br>\n|;
	print qq|����ȭ�鿡�� �α������ֽñ� �ٶ��ϴ�..<br>\n|;

	print qq|<a href="$FILE_TOP">[���ƿ´�]</a>\n|;
	&FOOTER;
	exit;
}

1;