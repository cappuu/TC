sub QUEST3 {

	&CHARA_MAIN_OPEN;
	open(IN,"$QUEST_DATA");
	@QUEST_DATA = <IN>;
	close(IN);
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	if($kcodea){&ERR("퀘스트를 이미 실행 중 입니다. ");}

	&GWAN2;

	foreach(@QUEST_DATA){
		($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
		if($qnum eq $in{'num'}){
		$quest_name = "$qname";
		$kcodea .= $qcode;
		$aquest = "$quest";
		}
	}
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
                        <font color=black>$quest_name님의<br>「$aquest」를 받으셨네요.<br>보상도 보상이니 만큼 우리 도룡주막을 위해서라도<br>열심히 해주셨으면 좋겠네요.</font>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<p align="center"><b>「$aquest」퀘스트를 입수하였습니다.</b></p><br>
<form action="quest0.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=mode value=QUEST>
<p align="center"><input type=submit value="확인"></p></form>
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