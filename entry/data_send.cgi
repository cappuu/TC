sub DATA_SEND {

	open(IN,"$TOWN_LIST") or &ERR2("������ ������ ������ �ʽ��ϴ�.");
	@TOWN = <IN>;
	close(IN);

	&CHARA_MAIN_OPEN;
	&HEADER;

	print <<"EOM";
<CENTER><h3>-- ��� �Ϸ� --</h3>
<hr size=0>
$kname�� $GAME_TITLE�� ���迡 ��ϵǾ����ϴ�.<BR>���̵�� ��й�ȣ�� ���� �ʰ� �޸��صνðų� ����Ͻñ� �ٶ��ϴ�.
<hr size=0>
ID : <font color=red>$in{'id'}</font><BR>
PASS : <font color=red>$in{'pass'}</font><BR>
<p>
�������ͽ�<BR><table border=0 bgcolor=$TABLE_C cellspacing=1><TBODY bgcolor=$TD_C4>
<tr><td rowspan="8" align="center"><img src="$IMG/$in{'chara'}.gif"></td>
<td class="b1">�̸�</td><td width=50>$hi[$in{'chara'}]</td>
<td class="b1">����</td><td>$cou_name</td></tr>
<tr><td class="b1">���</td><td>$LANK[0]</td>
<td class="b1">�ʱ���ġ</td><td>$z2name</td></tr>
<tr><td class="b1">����</td><td width=50>$in{'str'}</td>
<td class="b1">����</td><td>$in{'int'}</td></tr>
<tr><td>��ַ�</td><td>$in{'tou'}</td>
<td>�ŷ�</td><td>$in{'cha'}</td></tr>
</table><p>
<form action="$FILE_ENTRY" method="post">
<input type="hidden" name=mode value=RESISDENTS>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=num value="0">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" value="������ ����">
</form><p>
<form action="$FILE_STATUS" method="post">
<input type="hidden" name=mode value=STATUS>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" value="������ ����">
</form><p>

</form>
<form action="$FILE_ENTRY" method="post" name=para>
<input type="hidden" name="mode" value="ENTRY2">
<input type="hidden" name="mail" value="$in{'mail'}">
<input type="hidden" name="id" value="$in{'id'}">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="chara_name" value="$in{'chara_name'}">
<input type="hidden" name="chara" value="$in{'chara'}">
<input type="hidden" name="type" value="$in{'type'}">
<td align="center">
</CENTER>
EOM

		&FOOTER;

		exit;
}
1;