sub QUEST2 {

	&CHARA_MAIN_OPEN;
	open(IN,"$QUEST_DATA");
	@QUEST_DATA = <IN>;
	close(IN);
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);


	&GWAN2;

	foreach(@QUEST_DATA){
		($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
		if($qnum eq $in{'num'}){
		$questf = "$qface";
		$questn = "$qname";
		$questt = "$quest";
		$questl = "$qlevel";
		if($kcodea =~ /$qcode/ && $kqpoint >= $qlimit){
		$quest_list = "$qtalkb";
		$quest_list1 = "<form action=\"./quest0.cgi\" method=\"POST\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=num value=$qnum><input type=hidden name=mode value=QUEST4><p align=center><input type=submit value=\"����Ʈ�Ϸ�\"></p></form>";
		}else{
		$quest_list = "$qtalka";
		if(!$kcodea){
		$quest_list1 = "<form action=\"./quest0.cgi\" method=\"POST\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=num value=$qnum><input type=hidden name=mode value=QUEST3><p align=center><input type=submit value=\"����Ʈ����\"></p></form>";
		}
		}

		if($qgold){$cgold="�� $qgold,";}
		if($qrice){$crice="�� $qrice,";}
		if($qstr){$cstr="���°���ġ $qstr,";}
		if($qint){$cint="���°���ġ $qint,";}
		if($qlea){$clea="��ְ���ġ $qlea,";}
		if($qcha){$ccha="�ŷ°���ġ $qcha,";}
		if($qcex){$ccex="����ġ $qcex,";}
		if($qexp){$cexp="����ġ $qexp,";}



		}


	}

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
        <td width="945" height="500" background="$IMG/backg.gif">
<p>&nbsp;</p>
            <table align="center" cellpadding="0" cellspacing="0" width="700">
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law1.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="940" height="300" background="$IMG/law3.gif">

<table align="center" cellpadding="0" cellspacing="0" width="500" height="811">
    <tr>
        <td width="1101" background="$IMG/quest03.jpg">
            <table align="center" cellpadding="0" cellspacing="0" width="90%">
                <tr>
                    <td width="80" height="100">
                        <img src="$IMG/$questf.gif">
                    </td>
                    <td width="15" height="100">
                        &nbsp;
                    </td>
                    <td width="355" height="100">
                       <font color=black><span style="font-size:13pt;"><b>$questn���� �Ƿ��Դϴ�.</b><br><br>[Lv.$questl] ��$questt��</span></font>
                    </td>
                </tr>
                <tr>
                    <td width="450" height="600" colspan="3" valign="up">
                        <span style="font-size:11pt;"><font color=black>$quest_list<br><br><br><b>����:$cgold$crice$cstr$cint$clea$ccha$ccex$cexp</b></font></span>
                    </td>
                </tr>
                <tr>
                    <td width="450" height="40" colspan="3">
<table align="center">
    <tr>
        <td>
<font color=black>$quest_list1</font>
        </td>
        <td>
<form action="quest0.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=mode value=QUEST>
<p align="center"><input type=submit value="�ָ����� ���ư���"></p></form>
        </td>
    </tr>
</table>                    
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
                    </td>
                </tr>
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law2.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
            </table>
<p>&nbsp;</p>
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