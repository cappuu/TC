sub QUEST4 {

	&CHARA_MAIN_OPEN;
	open(IN,"$QUEST_DATA");
	@QUEST_DATA = <IN>;
	close(IN);
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	&GWAN2;
	open(IN,"$member_list") or &ERR2('파일을 열지 않았습니다. err no :country');
	@MEMBER_DATA = <IN>;
	close(IN);

	foreach(@MEMBER_DATA){
		($mname,$mpass)=split(/<>/);
		if($kname eq "$mname"){
			$questbonus = 1;
		}
	}


	foreach(@QUEST_DATA){
		($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
		if($qnum eq $in{'num'}){
		if($kcodeb =~ /$qcode/){
			&ERR("새로고침 장난은 안되겠죠? ^-^");
		}


		if($questbonus){
		$kgold += int($qgold*1.2);
		$krice += int($qrice*1.2);
		$kstr_ex += int($qstr*1.2);
		$kint_ex += int($qint*1.2);
		$klea_ex += int($qlea*1.2);
		$kcha_ex += int($qcha*1.2);
		$kcex += int($qcex*1.2);
		$kexp += int($qexp*1.2);
		}else{
		$kgold += $qgold;
		$krice += $qrice;
		$kstr_ex += $qstr;
		$kint_ex += $qint;
		$klea_ex += $qlea;
		$kcha_ex += $qcha;
		$kcex += $qcex;
		$kexp += $qexp;
		}
		$kcodea = "";
		$kcodeb .= $qcode;
		$kqpoint = 0;
		$questf = "$qface";
		$questn = "$qname";
		$questl = "$qlevel";
		$questt = "$quest";
		$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
		$quest_list = "$qtalkc";
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
        <td width="945" height="857" background="$IMG/backg.gif">
            <table align="center" cellpadding="0" cellspacing="0" width="700">
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law1.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="940" height="785" background="$IMG/law3.gif">
<table align="center" cellpadding="0" cellspacing="0" width="500" height="811">
    <tr>
        <td width="1101" background="$IMG/quest03.jpg">
            <table align="center" cellpadding="0" cellspacing="0" width="90%">
                <tr>
                    <td width="80" height="100">
                        <img src="$IMG/$questf.gif">
                    </td>
                    <td width="15" height="100">
                    </td>
                    <td width="355" height="100">
                       <font color=black><span style="font-size:13pt;"><b>$questn님의 의뢰를 달성!</b><br><br>[레벨$questl퀘스트] - $questt</span></font>
                    </td>
                </tr>
                <tr>
                    <td width="450" height="600" colspan="3" valign="up">
                        <span style="font-size:11pt;"><font color=black>$quest_list</font></span>
                    </td>
                </tr>
                <tr>
                    <td width="450" height="40" colspan="3">
<form action="quest0.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=mode value=QUEST>
<p align="center"><input type=submit value="주막으로 돌아간다"></p></form>
</td>
                </tr>
            </table>
        </td>
    </tr>
</table>
        </td>
    </tr>
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