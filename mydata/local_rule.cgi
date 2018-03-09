
sub LOCAL_RULE {

	&CHARA_MAIN_OPEN;

	&COUNTRY_DATA_OPEN("$kcon");
	if($xcid eq "0"){&ERR("재야인사는 실행할 수 없습니다.");}
	$sno = $kcex / $LANK;
	if($sno > 43){$sno = 43;}
	$xxins = "<font color=green size=1>$kunit군 $LANK[$sno] $kname</font>";

	if($xking eq $kid || $x0 eq $kid || $x17 eq $kid){
		$rule = "<input type=submit value=국법제정>;"
	}

	open(IN,"$LOCAL_LIST") or &ERR('파일을 열지 않았습니다.err no :country_bbs');
	@LOCAL_DATA = <IN>;
	close(IN);

        if($xking eq $kid || $x0 eq $kid || $x17 eq $kid){
                $rule1 = "<input type=submit style=\"font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;\" value=국법삭제>";
        	$rule2 = "<input type=submit style=\"font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;\" value=국법제정>";
	}


	&HEADER;

	print <<"EOM";
<body bgcolor="white" text="black" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" cellpadding="0" cellspacing="0" width="945">
    <tr>
        <td width="945">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="945" height="545" background="$IMG/backg.gif">
            <table align="center" cellpadding="0" cellspacing="0" width="448">
                <tr>
                    <td width="438" height="30">
                    </td>
                </tr>
                <tr>
                    <td width="438" height="9">
                        <p align="center"><img src="$IMG/law1.gif" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td background="$IMG/law3.gif">
<table bgcolor="black" width="98%" align="center">
    <tr>
        <td>
            <font color="white" face="돋움"><span style="font-size:9pt;"><b>국가법전실</b><br>$xname국의 정해진 독자적인 특별한 룰이나 중요한 기밀을 남겨두기 위한 장소입니다.<BR>그 나라의 참가자는 $xname국에 몸을 담고 있는 한은 이 법에 따라 행동하셔야 합니다.<BR>잘 읽고 숙지한 뒤 의문사항이 있는 경우는 $xname국의 국왕,참모,승상에게 문의해주세요.(최대 20건까지 등록가능)</span></font>
        </td>
    </tr>
</table>
<br>
EOM
	$s_n = 0;
	foreach(@LOCAL_DATA){
		($bbid,$bbno,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype)=split(/<>/);
		if($kcon eq "$bbcon" && $bbtype eq "0"){
            $mes .= "<TR><TD><input type=radio name=del_id value=$bbno></td><td><font size=2 color=FFFFFF>$bbmes <font size=2>[제정 : $bbname]</TD></TR>\n";
		$s_n++;
		if($s_n > 15){last;}
		}
	}
print <<"EOM";
<form action="$FILE_MYDATA" method="post">
<TABLE border=0 width=99%  align="center">
  <TBODY>
    <TR>
      <TD>
      <TABLE border=0 width=100% bgcolor=$ELE_C[$xele]>
        <TBODY bgcolor=$ELE_BG[$xele]>
	$mes
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE>
<br>
<table align="center" cellpadding="0" cellspacing="0">
    <tr>
        <td>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=L_RULE_DEL>
$rule1
</form>
        </td>
<td>
<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=LOCAL_RULE1>
$rule2
</form>
</td>
        <td>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;" value="메뉴로 돌아온다"></form>
        </td>
    </tr>
</table>
                    </td>
                </tr>
                <tr>
                    <td width="438" height="10">
                        <p><img src="$IMG/law2.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="438" height="30">
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