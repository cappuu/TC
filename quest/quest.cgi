sub QUEST {


	&CHARA_MAIN_OPEN;
	open(IN,"$QUEST_DATA");
	@QUEST_DATA = <IN>;
	close(IN);
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	&GWAN2;

	$p=0;
	foreach(@QUEST_DATA){
		($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
		if($kcodea =~ /$qcode/){
		if($kqpoint >= $qlimit){
			$gogogo = "<input type=image src=\"$IMG/quest02b.jpg\">";
		}else{
			$gogogo = "<input type=image src=\"$IMG/quest02a.jpg\">";
		}	
		}else{
			$gogogo = "<input type=image src=\"$IMG/quest02.jpg\">";
		}		

		if($qlevel <= $klevel && $kcodeb =~ /$qflag/){
			if($kcodeb =~ /$qcode/){
			}else{
		$quest_list .= "<tr><td width=64 height=80><img src=\"$IMG/$qface.gif\"></td><td width=29 height=80 background=$IMG/quest011.jpg></td><td width=321 height=80 background=$IMG/quest012.jpg><font color=black><b>[$qname]</b><br>[Lv.$qlevel]「$quest」</font></td><form action=\"./quest0.cgi\" method=\"POST\"><td width=80 height=80><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=num value=$qnum><input type=hidden name=mode value=QUEST2>$gogogo</td></form></tr>";
		$p++;
			}
		}
		if($kcodea =~ /$qcode/){
		$quest_list1 = "<form action=\"./quest0.cgi\" method=\"POST\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=num value=$qnum><input type=hidden name=mode value=QUEST5><p align=center><input type=submit value=\"퀘스트 「$quest」을 취소\"></p></form>";
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
        <td width="945" height="857" background="$IMG/backg.gif">
            <table align="center" cellpadding="0" cellspacing="0" width="700">
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law1.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="940" height="785" background="$IMG/law3.gif" valign="up">
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
                        <font color=black>어머, $kname님 오셨네요.<br>이 곳 도룡주막에 오신 것을 환영합니다.<br>많은 분들이 의뢰를 
                        맡기실만한 분을 찾았는데<br>잘됬네요.<br>하지만 의뢰는 한번에 한 개 밖에 하질 못한답니다.<br>현재 들어온 의뢰는 
                        총 $p건이에요.</font>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<br>
<table align="center" cellpadding="0" cellspacing="0" width="500">
	$quest_list
	</table><br>
$quest_list1
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=mode value=STATUS>
<p align="center"><input type=submit value="주막에서 나간다"></p></form>
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