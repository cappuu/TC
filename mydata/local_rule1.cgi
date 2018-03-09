
sub LOCAL_RULE1 {

	&CHARA_MAIN_OPEN;

	&COUNTRY_DATA_OPEN("$kcon");
	if($xcid eq "0"){&ERR("재야인사는 실행할 수 없습니다.");}
	$sno = $kcex / $LANK;
	if($sno > 43){$sno = 43;}
	$xxins = "<font color=green size=1>$kunit군 $LANK[$sno] $kname</font>";

	open(IN,"$LOCAL_LIST") or &ERR('파일을 열지 않았습니다.err no :country_bbs');
	@LOCAL_DATA = <IN>;
	close(IN);


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
                    <td width="438" height="50">
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
            <font color="white" face="돋움"><span style="font-size:9pt;"><b>법전제작실</b><br>이 곳은 $xname국의 군주,참모,승상의 직위를 가진 분들만 들어올 수 있습니다.<br>이 곳에서는 자국의 모든 장수분들이 보시는 법을 제작하는 곳 입니다.<br>그러므로 불필요한 잡담을 금하고 오로지 국가에 관련된 사항의 법만 제작해주십시오.</span></font>
        </td>
    </tr>
</table>
<br><center><form action="$FILE_MYDATA" method="post">
<textarea name=ins cols=90 rows=30 style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele];">
</textarea>
<br><br>
<table align="center" cellpadding="0" cellspacing="0">
    <tr>
        <td>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=L_RULE_WRITE>
<input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;" value=국법제정>
</form>
        </td>
        <td>
<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=LOCAL_RULE>
<input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;" value="국가법전실로 돌아간다"></form>
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
                    <td width="438" height="50">
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