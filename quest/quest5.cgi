sub QUEST5 {


	&CHARA_MAIN_OPEN;
	open(IN,"$QUEST_DATA");
	@QUEST_DATA = <IN>;
	close(IN);
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	$kcodea = "";
	$kqpoint = 0;

	&CHARA_MAIN_INPUT;

	&HEADER;
	print <<"EOM";
<body bgcolor="white" text="white" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" cellpadding="0" cellspacing="0" width="945">
    <tr>
        <td width="945">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="945" height="600" background="$IMG/backg.gif">
            <table align="center" cellpadding="0" cellspacing="0" width="700">
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law1.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="940" height="400" background="$IMG/law3.gif" valign="up">
<table align="center" cellpadding="0" cellspacing="0" width="500" height="186" background="$IMG/quest04.jpg">
    <tr>
        <td width="1101">
            <table cellpadding="0" cellspacing="0" width="100%">
                <tr>
                    <td width="205" height="64">
                    </td>
                    <td width="295" height="64">
                    </td>
                </tr>
                <tr>
                    <td width="205" height="120">
                    </td>
                    <td width="295" height="120" valign="up">
                        <font color=black>����Ʈ�� ����ϽŰſ���?<br>������� ����� ���� �������ôٴ�..<br>�������ʹ� �̷� ���� �������� ���ڳ׿�.</font>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<p align="center"><b>����Ʈ�� ��ҵǾ����ϴ�.</b></p><br>
<form action="quest0.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=mode value=QUEST>
<p align="center"><input type=submit value="Ȯ��"></p></form>
                    </td>
                </tr>
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law2.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td width="945">
            <p><img src="$IMG/down.gif" width="950" height="26" border="0"></p>
        </td>
    </tr>
</table>
</body>
EOM

	&FOOTER;
	exit;

}
1;